#lab 3.2
#a program that takes in an a number and gives its absolute value

#prompt for a number and turning it into its absolute value
prompted_number = float(input("Enter a number: "))
abs_number = abs(prompted_number)

#outputting the absolute number
print("The absolute value of {} is {}".format(prompted_number, abs_number))