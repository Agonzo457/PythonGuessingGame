# See the examples in the provided code
# Use structured programming and indent your code.
# Programmer Name: *****add your name here****

import random

# uses randrange instead of randint for better results in Python 3.7 
# randrange stops just before the upper range, use (1, 11) for 1-10

num = random.randrange(1, 11)
# Ask the player to enter a name or quit to exit
name = input("Please type your name, or 'quit' to exit -> ")
name1 = "quit"

# use a while statement to test when the name is not equal to quit
while name != name1:


    # input enter a number from 1 to 10 for the variable your_guess
    your_guess = int(input("Type a number between 1 and 10 -> "))

   
    # display the number guessed
    print("Your number is", your_guess)

    while num != your_guess:

        # Write an if statement for your_guess is less than num
        if your_guess < num:

            print("Your guess is too low.")
            your_guess = int(input("Guess another number from 1 to 10: "))

        elif your_guess > num:
            print("Your guess is too high")
            your_guess = int(input("Guess another number from 1 to 10: "))

        else:
            break

    print("The correct number was", num)
    # display text with your guess and You won, name
    print(your_guess, "was your guess, and you won ", name, "!!!")


    print("***************************************************************")
    # ask the player to enter a name or quit to exit
    name = input("Please type your name, or 'quit' to exit -> ")

    num = random.randrange(1, 11)
print("Thank you for playing!") 


