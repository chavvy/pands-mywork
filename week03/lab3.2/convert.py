#lab 3.2 extra
#a program that will convert from euro to cents and give an absolute value

#prompt for the euro input and output in cent and absolute value
euro_input = float(input("Please an enter an amount: "))
cent_output = int(abs(euro_input*100))

#printing the result
print("That amount in cent is: {}".format(cent_output))