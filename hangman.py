
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', -1)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter in lettersGuessed:
            continue
        else:
            return False
    return True

#secretWord = 'apple'
#lettersGuessed = ['a', 'p', 'l', 'e', 's']
#print (isWordGuessed(secretWord, lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    ans=''
    for letter in secretWord:
        if letter in lettersGuessed:
            ans+=letter
        else:
            ans+='_ '
    return ans
            


#secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getGuessedWord(secretWord, lettersGuessed))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ans=''
    for letter in alphabet:
        if letter in lettersGuessed:
            continue
        else:
            ans+=letter
    return ans
            
    
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#lettersGuessed=[]
#print (getAvailableLetters(lettersGuessed))    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed=[]        # 追踪用户猜测过的字母
    mistakesMade=0           # 记录用户猜测错误的次数
    remainChance=8           # 剩余机会
    lens=len(secretWord)
    print("  -------------")
    print ("  Welcome to the game, Hangman!")
    #print(secretWord)
    print("  I am thinking of a word that is %d letters long."%lens)
    while True:
        judge=isWordGuessed(secretWord, lettersGuessed)
        if judge==True:
            print("  Congratulations, you won!")
            break
        if mistakesMade==8:
            print("  Sorry, you ran out of guesses. The word was '%s'."%secretWord)
            break
        
        print("  -------------")
        remainChance=8-mistakesMade
        print("  You have %d guesses left."%remainChance)
        availableLetters=getAvailableLetters(lettersGuessed)  # 还可以用来被猜测的字母
        print("  Available letters: %s"%availableLetters)
        guess=input('  Please guess a letter: ')
        if guess in lettersGuessed:
            ans=getGuessedWord(secretWord, lettersGuessed)
            print("  Oops! You've already guessed that letter: %s"%ans)
        else:
            lettersGuessed+=guess
            if guess in secretWord:
                #lettersGuessed+=guess
                ans=getGuessedWord(secretWord, lettersGuessed)
                print("  Good guess: %s"%ans)
            else:
                mistakesMade+=1
                ans=getGuessedWord(secretWord, lettersGuessed)
                print("  Oops! That letter is not in my word %s"%ans)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
