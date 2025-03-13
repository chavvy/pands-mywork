#lab 3.1
#script that will generate a random fruit from a list

import random

#variables with a list of fruits as well as randomly selecting one

fruit = ["Banana", "Apple", "Strawberry", "Pear", "Blueberry", "Cherry"]
randfruit = random.choice(fruit)

#outputting the random fruit

print("Here is your random fruit: {}".format(randfruit))