import random

secret_num = random.randint(1,20)

while True:
    guess = int(input("Whats your guess: "))

    if guess == secret_num:
        print("Congratulate!!")
        break
    elif guess > secret_num:
        print("Your guess is not correct.. try something smaller!")
    elif guess < secret_num:
        print("Your guess is not correct.. try something bigger!")
