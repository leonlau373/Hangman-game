# Problem Set 2, hangman.py
# Name: nya10
# Collaborators: -
# Time spent: not sure, but it's long!

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # WORK AS INTENDED, no bugs found so far
    '''
    Idea:
    So we iterate every letter on letters_guessed (inner loop) first (assuming no duplicate letters in it)
    If it matches to one entry in secret_word, the count increase by 1.
    Clearly, if count = word length --> We guessed the word!
    '''
    x = len(secret_word)
    count = 0
    for s in secret_word:
        for l in letters_guessed:
            if s == l:
                count = count + 1

    return (count == x)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # WORK AS INTENDED, so far no bug found
    '''
    Idea:
    Again, iterate everything over secret_word, and assign a variable char to it
    If l in letters_guessed matches with char --> Unreveal, by making assignment list_word[s] = char
    The rest unrevealed will be stay '_'
    '''
    word_length = len(secret_word)
    my_word = '_' * word_length
    list_word = list(my_word)

    for s in range(0, word_length, 1):
        char = secret_word[s]
        for l in letters_guessed:
            if char == l:
                list_word[s] = char

    word = ' '.join(list_word)
    return word  # return type is a string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # WORK AS INTENDED, so far no bug found
    '''
    Idea:
    Just delete something from word_available, when there's a letter in letters_guessed
    Then return it by intended format
    '''
    word_available = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
    for s in letters_guessed:
        word_available.remove(s)

    word = ''.join(word_available)
    return word


###################### USEFUL FUNCTIONS ABOVE #############################################

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    mistake = 3
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("You have", mistake, "warning(s) left")
    print("-------------")

    letters_guessed = []
    unique_letter = []  # To count the score, by counting unique letter

    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:  # condition to end the game
        print("You have", guesses, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
        word_length = len(secret_word)

        character = input("Make your guess! ")
        char = character.lower()  # lower string

        if char in get_available_letters(letters_guessed):
            letters_guessed.append(char)
        elif mistake > 0:  # condition for warnings
            print("Sorry, you have guessed this letter!")
            mistake = mistake - 1
            print("You can make", mistake, "warning(s) left")
            print("Available letters:", get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            continue  # go back to while loop
        elif guesses > 1:  # condition for when warnings is over
            print("You have make too many mistakes, you'll lose a guess")
            print("Available letters:", get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            guesses = guesses - 1
            continue
        else:
            print("You lose the game")
            print("The word is", secret_word)
            continue

        word = get_guessed_word(secret_word, letters_guessed)
        print(word)

        vowels = ["a", "e", "i", "o", "u"]

        for i in range(0, word_length, 1):
            if char == secret_word[i]:
                print("Good guess!")
                unique_letter.append(char)
                print("-------------")
                break
            elif i == word_length - 1 and (char != secret_word[i] or mistake < 1) and char in vowels:
                guesses = guesses - 2
                print("Oops! That letter is not in my word")
                print("-------------")
            elif i == word_length - 1 and (char != secret_word[i] or mistake < 1) and (char not in vowels):
                guesses = guesses - 1
                print("Oops! That letter is not in my word")
                print("-------------")
            else:
                continue

        if guesses <= 0:
            print("You lose the game")
            print("The word is", secret_word)
        if is_word_guessed(secret_word, letters_guessed):
            print("You win this game!")
            print("The word is", secret_word)
            print("Your score is", guesses * len(unique_letter))

        print(" ")

    return 0


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Good, no bug, I think
    '''
    Idea: We input my_word with get_guessed_word(secret_word, letters_guessed), which returns string with spaces
    Thus we must get rid of that whitespaces, with .replace function, name that word with "word_nospace"
    Scan the word_nospace and other_word char length, if they are not same --> False, no need to run further
    Else, we iterate from 0 to len(word_nospace) - 1, if one of word_nospace and other_word is not same
    AND word_nospace doesn't contain '_', then we return False, otherwise return True.
    '''
    word_nospace = my_word.replace(" ", "")

    my_word_length = len(word_nospace)
    other_word_length = len(other_word)

    if my_word_length != other_word_length:
        return False

    for i in range(0,my_word_length,1):
        if word_nospace[i] != other_word[i] and word_nospace[i] != '_':
            return False

    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    #Good, no bug
    '''
    So we just initialize possible_word to be an empty string
    Then if we have match_with_gaps(my_word, word) to be true, then we add that word to possible word.
    '''
    possible_word = ""

    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_word = possible_word + " " + word

    print(possible_word)

    pass

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("Here is the rules:")
    print("Try to guess the word, if you guess a vowel wrong, you'll lose two guesses. If you guess a consonant wrong, you'll lose a guess")
    print("If you guess correctly, you don't lose your guess")
    print("Type '*' to use your hints")
    print("-------------")

    difficulty = input("Choose your desired difficulty. Type 1 for Easy, Type 2 for Medium, Type 3 for Hard: ")
    guesses = 10
    mistake = 3
    hints = 2
    if difficulty == '1':
        guesses = 10
        mistake = 3
        hints = 2
    elif difficulty == '2':
        guesses = 8
        mistake = 3
        hints = 2
    elif difficulty == '3':
        guesses = 6
        mistake = 3
        hints = 1
    else:
        print("Goodbye, it seems like you don't want to play the game :(")
        return 0

    print("-------------")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("You have", mistake, "warning(s) left")
    print("-------------")
    letters_guessed = []
    unique_letter = []  # To count the score, by counting unique letter

    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:  # condition to end the game
        print("You have", guesses, "guesses left")
        print("You have", hints, "hint(s) left")
        print("If you want to use your hint, type '*' ")
        print("Available letters:", get_available_letters(letters_guessed))
        word_length = len(secret_word)

        character = input("Make your guess! ")
        char = character.lower()  # lower string

        if char in get_available_letters(letters_guessed):
            letters_guessed.append(char)
        elif char == '*' and hints >= 1:
            print("Show possible matches", get_guessed_word(secret_word, letters_guessed))
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            hints = hints - 1
            print("-------------")
            continue
        elif char == '*' and hints == 0:
            print("You have used your hints")
            print(get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            continue
        elif mistake > 0:  # condition for warnings
            print("Sorry, you have guessed this letter!")
            mistake = mistake - 1
            print("You have", mistake, "warning(s) left")
            print(get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            continue  # go back to while loop
        elif guesses >= 1:  # condition for when warnings is over
            print("You have make too many mistakes, you'll lose a guess")
            print(get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            guesses = guesses - 1
            continue
        else:
            print("You lose the game")
            print("The word is", secret_word)
            continue

        word = get_guessed_word(secret_word, letters_guessed)
        print(word)

        vowels = ["a", "e", "i", "o", "u"]

        for i in range(0, word_length, 1):
            if char == secret_word[i]:
                print("Good guess!")
                unique_letter.append(char)
                print("-------------")
                break
            elif i == word_length - 1 and (char != secret_word[i] or mistake < 1) and char in vowels:
                guesses = guesses - 2
                print("Oops! That letter is not in my word")
                print("-------------")
            elif i == word_length - 1 and (char != secret_word[i] or mistake < 1) and (char not in vowels):
                guesses = guesses - 1
                print("Oops! That letter is not in my word")
                print("-------------")
            else:
                continue

        if guesses <= 0:
            print("You lose the game")
            print("The word is", secret_word)
        if is_word_guessed(secret_word, letters_guessed):
            print("You win this game!")
            print("The word is", secret_word)
            print("Your score is", guesses * len(unique_letter) * (hints + 1))

        print(" ")

    return 0

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
