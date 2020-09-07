import re
import random

word_bank = ['apple', 'basket', 'carrot', 'python', 'java', 'javascript']
hangman = [" ", "O", "O-", "O-'", "O-|", "O-|-", "O-|-'", "O-|-<"]
random_word = ''
word_letters = []
display_list = []
display_word = ''
found_indices = []
guess = ''
guess_count = 0

# It's wild how I felt pretty good about writing more complicated stuff in java and js
# and now we're back to python and I feel like I'm so lost. Code feels messy.

def main():
    # Still understanding this, need global variables, otherwise they're treated as function specific?
    global restart
    global guess
    global guess_count
    # Running the methods, first to choose the random word, then to display how many spaces there are
    choose_word()
    display()
    # while the guess count is below 7, that means a full hangman hasn't been drawn, and they can keep looping
    # through guesses
    while guess_count < 7:
        # first asking them to guess a letter, then checking that letter with the word.
        guess = ask_letter()
        result = guess_check(guess)
        # if the result is true, which means the letter was found in the word, then it re-runs display
        # because the word has to show the correct guessed letters. it runs the win check to see if
        # all the letters have been found, ending the game if so.
        if result:
            display()
            win = win_check()
            if win:
                break
        # If they guess wrong, then the guess count is added and display is run again to show the word spaces 
        # and also the hangman parts
        else:
            print('Letter not found!')
            guess_count += 1
            display()
    # If they run out of guesses, the while loop ends (if they won the while loop ends too)
    # but in this case, they also get the message about losing.
    if guess_count == 7:
        print('Better luck next time.')
    
# main chooses random word and counts out the number of blanks, so the user knows how many letters there are.
def choose_word():
    global random_word
    random_word = random.choice(word_bank)
    for letter in random_word:
        # Also saves the individual letters into a list so they can be searched for later.
        word_letters.append(letter)
        display_list.append('_')

# displays the blanks in a more readable way, and can be used to refresh the view when player gets a letter right or wrong
def display():
    global found_indices
    # If a guess was correct, the index was saved here, so then that letter is placed into the display list at the correct index.
    for n in found_indices:
        display_list[n] = guess
    display_word = (' ').join(display_list)
    # Depending on the guess count, it will display the corresponding index in the hangman section, so it'll progress through
    # like in the game, drawing out the hangman
    print(hangman[guess_count])
    print(display_word)

def ask_letter():
    # Tom helped me with this, reminding me about regular expressions and pattern checking
    guess = ''
    # established pattern of A-Z or a-z, so it only accepts the one entry
    pattern = re.compile(r'\b[A-Za-z]\b')
    check = pattern.search((guess))
    while check is None:
        # If it doesn't match the pattern, it'll ask again repeatedly
        guess = input("Please enter a letter to guess: ")
        check = pattern.search(guess)
    # if it matches the pattern, the lowercase letter is passed back to use later
    return(guess.lower())

def guess_check(guess):
    global found_indices
    found_indices = []

    # after the indices are blanked (otherwise it'd replace all the indicies with the guess letter)
    # it checks to see if the letter is in the word, saving the index if it's correct
    for index, letter in enumerate(word_letters):
        if letter == guess:
            found_indices.append(index)

    # If none were found and the list is empty, then false is returned to the main method.
    if len(found_indices) == 0:
        return False
    else:
        return True

# Checks to see if the User won by searching for underscores (empty letter spots)
# and if none are found, then all the letters are filled in and the User won the game.
def win_check():
    if '_' not in display_list:
        print("Congratulations!!")
        return True
    else:
        return False

main()

