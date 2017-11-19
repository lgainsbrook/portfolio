# GOAL: PLAYER TRIES TO GUESS THE COMPUTER'S NUMBER

#ask if player wants to play again, then quit or restart game
def play_again():
    response = raw_input("Would you like to play again? Enter 'y' for yes, 'n' for no.")
    if response.lower() == 'y':
        print "Alright! Let's get started!"
        game()
    elif response.lower() == 'n':
        print "Thanks for playing. Have a nice day!"
    else:
        print "Error: please enter 'y' to play again or 'n' to quit."
        play_again()

def game():
    import random
    secret_num = random.randint(1,100)

    print """
Instructions: Try to guess the computer's secret number between 1 and 1,000.
At any time, you can type 'hint' to get a hint or 'give up' to see the answer. Good luck!
"""
    count = 1
    while count <= 10:
        guess = raw_input("Your guess: ")
#if the entry is an integer, it's either correct, too high, or too low, then continue
        try:
            guess = int(guess)
            if guess == secret_num:
                print "Congratulations! My number was {}!".format(secret_num)
                print "Number of guesses: {}. Can you use fewer guesses next time?".format(count)
                play_again()
            elif guess < secret_num:
                print "My number is higher than {}.".format(guess)
                count += 1
            elif guess > secret_num:
                print "My number is lower than {}.".format(guess)
                count += 1

#if player enters a word
        except:
            if guess.lower() == "give up":
                print "My number was {}. Next time, keep guessing - you can do it!".format(secret_num)
                play_again()
            else:
                print "Error: Please enter a number."
                continue
    else:
        print "Sorry, you're out of guesses. My number was {}.".format(secret_num)
        play_again()

game()
