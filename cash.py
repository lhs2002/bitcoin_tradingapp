#Modified from sample solution

from cs50 import get_float

while True:
    dollars = get_float("Change: ")
    if (dollars >= 0):
        break

#Convert dollars to cents to avoid floating-point imprecision
cents = round(dollars * 100)

#Initialize counter for coins
coins = 0

#Take as many 25-cent bites out of problem as possible, relying on integer division for whole number
coins +=  int(cents /25)

#Amount of changed owed now equals remainder after dividing by 25
cents = cents % 25;

#Repeat for dimes
coins += int(cents / 10)
cents = cents % 10

#Repeat for nickels
coins += int(cents / 5)
cents = cents % 5

#Remainder is now < 5, so handle with pennies
coins += cents;

#Print Counter
print(f"{coins}")