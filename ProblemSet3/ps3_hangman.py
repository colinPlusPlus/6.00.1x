# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/newuser/Documents/6.00/ProblemSet3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    x = []
    for e in secretWord:
        if e in lettersGuessed:
            x.append(e)
    return len(x) == len(secretWord)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    i = 0
    ans = []
    while i < len(secretWord):
        ans.append('_' ' ')
        i+=1
    i = 0
    for letter in lettersGuessed:
        while i < len(secretWord):
            if letter == list(secretWord)[i]:    
                ans[i] = letter
                i+=1
            else:
                i+=1
        i = 0
    return "".join(ans)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    i = 0
    low = 0
    high = len(string.ascii_lowercase)
    guess = (low + high)/2
    alphabet = list(string.ascii_lowercase)    
    for letter in lettersGuessed:
        while i < len(string.ascii_lowercase):
            if list(string.ascii_lowercase)[guess] == letter:
                alphabet[guess] = ''
                break
            elif list(string.ascii_lowercase)[guess] > letter:
                high = guess
            else:
                low = guess
            guess = (low + high)/2
            i+=1
        i = 0
        low = 0
        high = len(string.ascii_lowercase)
        guess = (low + high)/2
    return "".join(alphabet)
    

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
    i = 0
    guesses = 8
    lettersGuessed = []
    #print welcome message
    print "Welcome to the game, Hangman!"
    print "I'm think of a word that is " + str(len(secretWord)) + " letters long"
    print "-------------"
    
    #start game loop
    while i < guesses:
        print "You have guesses " +str(guesses)+ " left"
        print "Available letters: " + getAvailableLetters(lettersGuessed)
        letter = raw_input("Please guess a letter: ")
        letter = letter.lower()
        
        #check to see if letter has already been guessed
        if letter in lettersGuessed and letter in secretWord:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            print "-------------"
        elif letter not in getAvailableLetters(lettersGuessed):
            print "Oops! You've already guessed that letter: _"
            print "-------------"
        
        #check to see if letter guessed is in secret word
        elif letter in secretWord:
            lettersGuessed.append(letter)
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
            print "-------------"
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print "Congratulations, you won!"
                print "-------------"
                break
        else:
            lettersGuessed.append(letter)
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            print "-------------"
            guesses -= 1
        if guesses == 0:
            print "Sorry, you ran out of guesses. The word was " + secretWord + "."
        






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
#secretWord = 'apple'
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
