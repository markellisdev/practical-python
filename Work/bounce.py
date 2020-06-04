# bounce.py
#
# Exercise 1.5
height = float(100)
bounce = float(3/5)
num_of_rebounds = 1
num_of_falls = 10

while num_of_rebounds <= num_of_falls:
    print(round((height * bounce), 4))
    height = height * bounce
    num_of_rebounds += 1