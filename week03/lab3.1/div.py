#lab 3.1
#a program that divides the first number by the second

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the number you want to divide by: "))

#dividing the first number by the second number

answer = int(first_number//second_number)

#getting the remainder

remainder = first_number%second_number

#printing the result

print("{} divided by {} is {} with a remainder of {}".format(first_number, second_number, answer, remainder))