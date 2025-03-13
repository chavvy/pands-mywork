#lab 3.1
#Showing variable types and their values
#int, float, boolean, str, list

i = 3
fl = 3.5
isa = True
memo = "how now Brown Cow"
lots = []

#can use .format to fill out empty brackets in a line
#putting \033[1m at the start to make text bold, \033[0m to reset text format

print("variable \033[1m{}\033[0m is of type: {} and value: {}".format('i', type(i), i))
print("variable \033[1m{}\033[0m is of type: {} and value: {}".format('fl', type(fl), fl))
print("variable \033[1m{}\033[0m is of type: {} and value: {}".format('isa', type(isa), isa))
print("variable \033[1m{}\033[0m is of type: {} and value: {}".format('memo', type(memo), memo))
print("variable \033[1m{}\033[0m is of type: {} and value: {}".format('lots', type(lots), lots))