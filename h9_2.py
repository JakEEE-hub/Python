num = int(input("Select a number between 1 and 100: "))
num = num + 1

start = 1

while start != num:
    if start%3 == 0 and start%5 == 0:
        print("fizzbuzz")
        start = start + 1
    elif start%3 == 0:
        print("fizz")
        start = start + 1
    elif start%5 == 0:
        print("buzz")
        start = start + 1
    else:
        print(start)
        start = start + 1
