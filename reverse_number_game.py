# COMPUTER TRIES TO GUESS PLAYER'S NUMBER

def game():
# Get range from user and give instructions.
    print "First, think of a secret number between 1 and 10, 100, or 1,000."
    upper_limit = int(raw_input("Is the upper limit of your number 10, 100, or 1,000?\n"))
    lower_limit = 1
    print """
    Thank you! Now the computer will try to guess your secret number. After each guess, you will be prompted
    to tell it if the guess is 'too high', 'too low', or 'correct'.
    """
    import random
    all_guesses = []
    while True:
        guess = random.randint(lower_limit, upper_limit)
        if not guess in all_guesses:
            all_guesses.append(guess)
            print "The computer's guess is: {}.".format(guess)
            feedback = raw_input("Enter 'too high', 'too low', or 'correct'\n")
            if feedback == 'too high':
                upper_limit = guess
            elif feedback == 'too low':
                lower_limit = guess
            elif feedback == 'correct':
                break
        else:
            continue
game()
print "Game over. Thanks for playing!"
