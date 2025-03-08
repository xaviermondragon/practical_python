# bounce.py
#
# Exercise 1.5

height = 100
height_lose = 3/5

i = 1
while i <= 10:
    height *= height_lose
    print(i, round(height, 4))
    i += 1
