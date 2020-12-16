import random

#greet the user
print("Welcome to my rolling dice game!")
print("the rules are simple, try and guess the number (from 1 - 12) of the two di added together")

#request number of guesses from the user
num_guesses = int(input("please enter the number of chances you would like and then click enter:"))

#generate a random number for dice 1
dice = []
dice.append(random.randint(1,6))

#generate random number for dice 2
dice.append(random.randint(1,6))

#sum the total of the two dice
total = sum(dice)

#request guess from the user based on the # of guesses requested
for i in range(num_guesses):
    guess = int(input("what is your guess for the total of the two dice:"))
    if guess == total:
        print("you win!")
        break
    elif guess > total:
        print("your guess is too high! try again")
    else:
        print("your guess is too low... try again")



                  
    




