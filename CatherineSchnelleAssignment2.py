# INF360 Programming in Python
# Catherine Schnelle
# Week 2 Assignment

#x (1 point) - Initial comments*
#x (1 points) - Use at least 2 comparison operators.
#x (1 points) - Use at least 1 boolean operator (and, or, not).
#x (2 points) - Write at least 1 if statement that contains 2 elif statements and 1 else statement.
#x (2 points) - Write at least 1 while statement that contains a break and continue.
#x (2 points) - Write at least 1 for loop using the range() method.
#x (1 point) - Use the import keyword to import the random module. Use the random.randint() function somewhere in your script.

# Import random function
import random

# Set variable 'play' for loop, will close out game when game is over.
play = True

# Main loop - use of 1 comparison operator
while play == True:

    # Creates a random number between 1-50
    winNum = random.randint(1, 50)

    # Sets the number of chances to 3
    numChance = 3

    # for loop header using range function
    for i in range(1):
        print('#####P#I#C#K##3##N#U#M#B#E#R#S###')
    #initial prompt
    print("Welcome to the Pick 3 State Lottery!")
    print("Enter a number between 1 - 50, guess correctly to win. You have 3 chances.")
 
 #checks remaining chances - use 1 comparison operator.
    while numChance > 0:
        #prints remaining chances
        print(str(numChance) + ' chances remain.')
        #prompts user to enter a number
        myNum = input('Enter a number: ')
        # Subtract a chance after each entry.
        numChance = numChance - 1

        # Winning statement
        if int(myNum) == winNum:
            print('Congratulations, you have a winning number! You get a bonus play!')
            #continue loop for bonus play
            continue
        # Out of range statement - 2 comparison operators 1 boolean operator
        elif int(myNum) < 1 or int(myNum) > 50:
            print('Invalid! Start over!')
            #break out of loop
            break
        #Exhausted chances statement
        elif numChance ==0:
            print('Thanks for playing the State Lottery.')
            #end loop 
            play = False
        # losing statement
        else:
             print('You lose.')