import random

number= random.randint(1, 9)

print("Number guessing game")

chances = 5

while (chances > 0):
    print("-----------")

    guess = int(input("Enter your guess between (1 to 9) : "))
    
    chances = chances - 1

    if guess > number :
        print("Your guess was too high : guess any number less than " , guess)
        
    elif guess < number :
        print("Your guess is too low : guess any number more than ", guess)
        
    else :
        print("Wow Congratulations you won !!!!!")

if chances == 0 :
    print("You lose!!!")






