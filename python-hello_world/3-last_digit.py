#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastdigit = abs(number) % 10 
if lastdigit > 5:
    print("Last digit of", number, "is", lastdigit, "is greater than five")
elif lastdigit == 0:
    print("Last digit of", number, "is", lastdigit, "and is 0")
elif lastdigit < 6  and lastdigit != 0 :
    print("Last digit of", number, "is", lastdigit, "and is less than 6 and not 0")