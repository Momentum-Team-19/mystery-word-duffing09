# imports the random module, used to generate random numbers or make random selections
import random

# def categorize_words(filename):
#     easy_words = [word for word in words_list if 4 <=len(word) <=6]
#     medium_words = [word for word in words_list if 6 <= len(word) <=8]
#     hard_words = [word for word in words_list if len(word) > 8]

    # return easy_words, medium_words, hard_words
# this line starts the definition of a function named 'select_word' that takes a single argument 'filename'
def select_word(difficulty_words):
    with open("words.txt", 'r') as file:
        file = file.read()
    words_list = file.split()
    if difficulty_words == "easy_words":
        easy_words = [word for word in words_list if 4 <= len(word) <= 6]
        random_word = random.choice(easy_words)
        return random_word
    if difficulty_words == "medium_words":
        medium_words = [word for word in words_list if 6 <= len(word) <= 8]
        random_word = random.choice(medium_words)
        return random_word
    if difficulty_words == "hard_words":
        hard_words = [word for word in words_list if len(word) > 8]
        random_word = random.choice(hard_words)
        return random_word
# uses 'with' statement to open specified 'filename' in read mode. ensures that the file is properly closed after block of code is executed
    #with open(filename, 'r') as file:
#reads the entire content of the opened file and assigns it to the variable 'file'.
        #file = file.read()
#splits the content of the 'file' variable into list of words using whitespace as separator. resulting list is sorted in the variable words_list
    #words_list = file.split()
#uses 'random.choice()' function from the 'random' module to randomly select 1 word from the 'words_list' and assigns it to the variable 'random_word'.
    random_word = random.choice(words_list)
#returns the randomly selected 'random_word' as result of 'select_word' function.
    return random_word

# eventually function will take in the file and return a word in the list at random
def select_difficulty():
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        return "easy_words"
    elif choice == "2":
        return "medium_words"
    elif choice == "3":
        return "hard_words"
    else:
        print("Invalid choice. Defaulting to medium difficulty")
        return "medium_words"

# starts definition of function "display_word_board" that takes 2 arguments: 'word'(word to be guessed) and 'guessed_letters (list of letters the player guessed)
def display_word_board(word, guessed_letters):
#initializes an empty string 'chosen_word' which is used to build the word with guessed letters and underscores
    chosen_word = ""
#starts a for loop that goes through each character(letter) in the 'word' parameter
    for letter in word:
#checks if the current 'letter' has been guessed and is present in 'guessed_letters' list
        if letter in guessed_letters:
#if letter has been guessed, it is added to 'chosen_word' string
            chosen_word += letter
# part of 'if' statement. if current 'letter' has not been guessed, following block of code will be executed
        else:
# if letter has not been guessed, an underscore character added to 'chosen_word' string instead of actual letter
            chosen_word += "_"
# returns 'chosen_word' string which represents current state of word with guessed letters and underscores
    return chosen_word

    # this function can display the word as underscores or letter that were guessed correctly

# starts definition of a function named 'user_guess' that take one argument: 'counter' (representing number of remaining guesses)
def user_guess(counter):
# starts a while loop that continues as long as the 'counter' is greater than 0
    while counter > 0:
#checks if 'counter' is not equal to 0. 'If' statement is redundant here since the 'while' loop alrady ensures the 'counter' is greater than 0
        if counter != 0:
# prints remaining number of guesses to the user
            print(f"You have {counter} guesses left")

# prompts user to input a letter, converts input to lowercase using 'lower()'. Removes leading/trailing whitespace using 'strip()' and assigned to 'guess'
        guess = input("Guess a letter: ").lower().strip()
# checks if length of 'guess' is not equal to 1(no letter guessed) or if the 'guess' contains non-alphabetical characters.
        if len(guess) != 1 or not guess.isalpha():
# if previous condition is met, this line prints an error message.
            print("Please enter only one letter.")
# if 'guess' input is valid(single letter), following block of code will be executed.
        else:
# line returns the valid 'guess' as the result of the 'user_guess' function
            return guess
    # take in user input and compare it to the word, will return if it was wrong or the correct letter


# starts the definition of a function named 'play_game' which represents main game loop
def display_game_over():
    print('Game over!')
    replay = input('Play again? (y/n): ')
    return replay.lower() == 'y'


def restart_game():
    replay = display_game_over()
    if replay:
        play_game()
    else:
        exit()


def play_game():
    # easy_words, medium_words, hard_words = categorize_words("words.txt")

    difficulty_words = select_difficulty()
    random_word = select_word(difficulty_words)
# calls 'select_word' function with the argument '"test-word.txt"' to randomly select a word from the list of words in the specified file. selected word is assigned to the variable 'random_word'
#initialize an empty list 'guessed_letters' to store the guessed letters and set initial value of 'counter' to 8(number of guesses)
    guessed_letters = []
    counter = 8
# starts infinite loop. will continue until explicitly broken using a 'break' statement.
    while counter > 0:
# calls 'display_word_board' function to generate a representation of the curent state of the word with guessed letters and underscores. result is assigned to 'display'
        display = display_word_board(random_word, guessed_letters)
# prints current state of word to player
        print(display)
# checks if there are no underscores (unrevealed letters) left in 'display'. if all letters have been guessed the following code happens.
        if "_" not in display:
            print("Finally, took you long enough to guess the word", random_word)
            break
# calls 'user_guess' function with current value of 'counter' to get the player's guess.
        guess = user_guess(counter)
#adds the guessed letter to 'guessed_letters' list
        guessed_letters.append(guess)
# checks if the guessed letter is not present in 'random_word'
        if guess not in random_word:
            counter -= 1
    else:
        print("You stink you lost!")
# if guessed letter is incorrect, this line decreases the value of 'counter' by 1, reducing guesses
    restart_game()
            

if __name__ == "__main__":
    play_game()
