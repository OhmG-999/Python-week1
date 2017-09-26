import math

# little program that gather the user input for the sphere radius to calculate its volume
# the program provide the result and keeps prompting for a new value until
# the user quit by typing 0

radius = input('Enter the radius of your sphere or 0 to quit: \n')
userInput = int(radius)

while userInput != 0:
    result = 4 / 3 * math.pi * userInput ** 3
    print('result: ',result)
    print()
    radius = input('Enter the radius of your sphere or 0 to quit: \n')
    userInput = int(radius)

print('Goodbye!')