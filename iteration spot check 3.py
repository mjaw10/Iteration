import random
guessed = False
number = random.randint(1,100)
no_of_turns = 0
while guessed == False:
    no_of_turns = no_of_turns + 1
    user_guess = int(input("Enter your guess for the number: "))
    if user_guess == number:
        guessed = True
    elif user_guess > number:
        print("The nuber you guessed is too high")
    else:
        print("The number you guessed is too low")
print("You took {0} turns to guess the number".format(no_of_turns))
print("The number was {0}".format(number))

