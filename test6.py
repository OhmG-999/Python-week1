# declare 2 variables to hold the rectangle width and length and initialised them
length = 0.0
width = 0.0

# create a function which accept the width and length inputed by the user and calculate the area
def calculatearea(length, width):
    area = 0.0
    area = round(width, 2) * round(length, 2)
    print('The area of a rectangle of ', width, 'cm by ', length, 'cm is ', area, 'cm \n')
    return


# prompt user to enter the rectangle width and length
length = float(input('Enter the width of the rectangle: \n'))

width = float(input('Enter the length of the rectangle: \n'))

# pass the 2 variables to the function
calculatearea(width, length)
