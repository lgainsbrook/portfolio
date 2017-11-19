# ADD SETS TO CLEAN CODE UP

import random
import os
import sys

max_strikes = 7


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def welcome():
    ready = raw_input("""
    Welcome to my game! Can you guess the secret word?
    Guess one letter at a time. You are allowed to get {} guesses wrong.
    Enter 'quit' at any time to quit.
    Enter 'solve' if you would like to guess the full word.
    Press enter/return to beign.
    """.format(max_strikes))
    if ready.lower() == 'quit':
        quit()
    else:
        difficulty = int(raw_input("Select your difficulty level. 1 for easy, 2 for medium, 3 for hard: "))
        return difficulty

def end():
    while True:
        play_again = raw_input("""
        Would you like to play again?
        Enter 'y' to play again, 'n' to quit: """)
        print ''
        if play_again.lower() == 'y':
            game(max_strikes)
        elif play_again.lower() == 'n':
            print "Thanks for playing! Have a nice day!\n"
            quit()
        else:
            print "Sorry, I didn't get that.\n"
            continue

def constant_display(bad_guesses, max_strikes, word, growing_word):
    print "{}/{} strikes: {}\n".format(len(bad_guesses), max_strikes, ' '.join(bad_guesses))
    if growing_word != []:
        print ' '.join(growing_word)
        print ''
    else:
        blanks = []
        for letter in word:
            blanks.append('_')
        print ' '.join(blanks)
        print ''

def get_guess(word, good_guesses, bad_guesses, growing_word):
    bad_list = []
    while True:
        constant_display(bad_guesses, max_strikes, word, growing_word)
        guess = raw_input("Guess a letter: ")
        print ''
        if guess == "quit":
            quit()
        elif guess == "solve":
            solve(word)
        elif guess in good_guesses or guess in bad_guesses:
            clear()
            print "You already guessed that letter!\n"
        elif not guess.isalpha():
            clear()
            print "{} is not a letter.\n".format(guess)
        elif len(guess) != 1:
            clear()
            print "You can only guess one letter at time.\n"
        else:
            return guess

def solve(word):
    solution = raw_input("Please enter the full word: ")
    print ''
    if solution == word:
        clear()
        print "Congrats! You got it! My word was {}.\n".format(word)
        end()
    else:
        clear()
        print "Sorry that's not correct.\n"

def game(max_strikes):
    clear()
    file = open('common_words.txt')
    difficult = []
    medium = []
    easy = []
    for word in file:
        word = word.strip()
        if len(word) > 7:
            difficult.append(word)
        elif len(word) > 5:
            medium.append(word)
        elif len(word) > 2:
            easy.append(word)
    difficulty = welcome()
    if difficulty == 1:
        word = random.choice(easy)
    elif difficulty == 2:
        word = random.choice(medium)
    elif difficulty == 3:
        word = random.choice(difficult)
    good_guesses = []
    bad_guesses = []
    growing_word = []
    while True:
        guess = get_guess(word, good_guesses, bad_guesses, growing_word)
        if guess in word:
            growing_word = []
            good_guesses.append(guess)
            for letter in word:
                if letter in good_guesses:
                    growing_word.append(letter)
                else:
                    growing_word.append('_')
            if ''.join(growing_word) == word:
                print "Congrats! You got it! My word was {}.\n".format(word)
                end()
            else:
                clear()
                continue
        elif not guess in word:
            bad_guesses.append(guess)
            clear()
            print "Sorry - no {} in my word.\n".format(guess)
            if len(bad_guesses) == max_strikes:
                constant_display(bad_guesses, max_strikes, word, growing_word)
                print "\nSorry - you're out of guesses! My word was {}.\n".format(word)
                end()
            else: continue


game(max_strikes)
