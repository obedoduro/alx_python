#last digit file
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastdigit = abs(number) % 10 
#check if number is negative and negate lastdigit
if lastdigit > 5 and number > 0:
    print("Last digit of", number, "is", lastdigit, "and is greater than 5")
elif lastdigit == 0:
    print("Last digit of", number, "is", lastdigit, "and is 0")
elif lastdigit < 6  and lastdigit != 0 and number > 0:
    print("Last digit of", number, "is", lastdigit, "and is less than 6 and not 0")
else : print("Last digit of", number, "is", -lastdigit, "and is less than 6 and not 0")