# bounce.py
#
# Exercise 1.5

bounceRatio = 3/5
height = 100

# using for loop
"""for i in range(10):
    height = height * bounceRatio
    print(i, round(height, 4))"""

# using while loop
bounce = 1
while bounce < 10:
    height = height * bounceRatio
    print(bounce, round(height, 4))
    bounce += 1