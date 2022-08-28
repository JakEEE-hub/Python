while True:
    kilometer = int(input("Enter number of kilometers: "))
    miles = kilometer * 0.621371

    print("{0} kilometers is {1} miles!".format(kilometer, miles))

    another = input("Your want to do another conversion (y/n)?? ")
    if another != "y":
        print("Ty for using our program!")
        break

