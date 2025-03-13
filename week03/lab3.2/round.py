#lab 3.2
#a program that takes in a float number and outputs an int

#prompt for a float number input and the integer output
float_input = float(input("Enter a float number: "))
int_output = round(float_input) #can add a number after the float_input to determine to what decimal place it should output

#outputting the rounded number
print("{} rounded is {}".format(float_input, int_output))