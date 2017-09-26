import string

# this program prompt the user for the name and year of birth
# and then print out a message with the user name and the user age

myAge = 0
currentYear = 2017
myName = input('What is your name? ')
yearOfBirth = int(input('Enter the year you were born (e.g. 1980)'))
myAge = currentYear - yearOfBirth
print('Hey', myName, ', you are', myAge)
