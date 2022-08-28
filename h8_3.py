first_num = int(input("Write first number: "))
operation = input("What arithmetic operation will u use: ")
second_num = int(input("Write second number: "))
result = None

if operation == "+":
    result = first_num + second_num
    print(str(first_num) + " " + operation + " " + str(second_num) + " = " + str(result))

elif operation == "-":
    result = first_num - second_num
    print(str(first_num) + " " + operation + " " + str(second_num) + " = ")

elif operation == "*":
    result = first_num * second_num
    print(str(first_num) + " " + operation + " " + str(second_num) + " = ")

elif operation == "/":
    result = first_num / second_num
    print(str(first_num) + " " + operation + " " + str(second_num) + " = ")

else:
    print("U write the wrong operation!")

