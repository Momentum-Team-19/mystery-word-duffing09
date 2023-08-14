import random


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

    random_word = random.choice(words_list)

    return random_word


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


def display_word_board(word, guessed_letters):

    chosen_word = ""

    for letter in word:

        if letter in guessed_letters:

            chosen_word += letter

        else:

            chosen_word += "_"

    return chosen_word


def user_guess(counter):

    while counter > 0:

        if counter != 0:

            print(f"You have {counter} guesses left")


        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():

            print("Please enter only one letter.")

        else:

            return guess




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
    

    difficulty_words = select_difficulty()
    random_word = select_word(difficulty_words)

    guessed_letters = []
    counter = 8

    while counter > 0:

        display = display_word_board(random_word, guessed_letters)

        print(display)

        if "_" not in display:
            print("Finally, took you long enough to guess the word", random_word)
            break

        guess = user_guess(counter)

        guessed_letters.append(guess)

        if guess not in random_word:
            counter -= 1
    else:
        print("You stink you lost!")
    restart_game()
            

if __name__ == "__main__":
    play_game()
