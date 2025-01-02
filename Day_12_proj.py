from random import randint
print("welcome to the number Guessing game")
print("I'm thinking of a number between 1 and 100.")

# let a user guess a number


rand = randint(1,100)
should_continue = True

while should_continue:
    user_guess = int(input("Make a Guess: "))
    if user_guess > rand:
        print("it is above the number ")
    
    elif user_guess < rand:
        print("it is below the number")
    
    else:
        print("you have got the number.")
       