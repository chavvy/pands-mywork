#lab 3.1
#a program that reads two numbers and subtracts the first one from the second one

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

#Subtracting the first from the second number

answer = first_number - second_number

#Outputting the answer using .format

print("{} minus {} is {}".format(first_number, second_number, answer))