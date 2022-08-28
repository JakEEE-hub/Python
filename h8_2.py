import random

secret_num = random.randint(0,20)

guess = int(input("Whats your guess: "))
if guess == secret_num:
    print("Congratulate!!")
else:
    print(str(secret_num) + ", close enough!")
