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
    global restart
    global guess
    global guess_count
    choose_word()
    display()
    while guess_count < 7:
        guess = ask_letter()
        result = guess_check(guess)
        if result:
            display()
            win = win_check()
            if win:
                break
        else:
            print('no go')
            guess_count += 1
            display()
    if guess_count == 7:
        print('Better luck next time.')
    
# main chooses random word and counts out blanks
def choose_word():
    global random_word
    random_word = random.choice(word_bank)
    for letter in random_word:
        word_letters.append(letter)
        display_list.append('_')

# displays the blanks in a more readable way, and can be used to refresh the view when player gets a letter right
def display():
    global found_indices
    for n in found_indices:
        display_list[n] = guess
    display_word = (' ').join(display_list)
    print(hangman[guess_count])
    print(display_word)
    # print(*display_list, sep=' ')

def ask_letter():
    # Tom helped me with this, reminding me about regular expressions and pattern checking
    guess = ''
    pattern = re.compile(r'\b[A-Za-z]\b')
    check = pattern.search((guess))
    while check is None:
        guess = input("Please enter a letter to guess: ")
        check = pattern.search(guess)
    return(guess.lower())

def guess_check(guess):
    global found_indices
    found_indices = []

    for index, letter in enumerate(word_letters):
        if letter == guess:
            found_indices.append(index)

    if len(found_indices) == 0:
        return False
    else:
        return True

def win_check():
    if '_' not in display_list:
        print("Congratulations!!")
        return True
    else:
        return False

main()

