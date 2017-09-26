# declare 3 variables and initialise the distance variable in km as the value never changes
distance = 0.3
speed = 0.0
time = 0.0

# create a function to calculate the speed based on the time submitted
def calculatespeed(distance, time):

    speed = (distance / time * 3600)
    print('The speed is ', speed, 'km/h \n')
    return

# gather user's input
time = float(input('Enter the time in second between the 2 points: \n'))

# user pass the variables to the function and return the result
calculatespeed(distance, time)


