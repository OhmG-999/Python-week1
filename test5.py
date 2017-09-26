# create 2 variables to hold the temperature and the temperature's scale
floatTemperature = 0.0;
scale = 0.0


# define a function a converting Celsius to Fahrenheit
def converttofahrenheit(temp):
    result = round(((temp * (1.8))+32), 2)
    print('This represent a temperature of °F ', result)
    return;


# define a function a converting Fahrenheit to Celsius
def converttocelsius(temp):
    result = round(((temp - 32)/(1.8)), 2)
    print('This represent a temperature of °C ', result)
    return;


# prompt users for the temperature
floatTemperature = float(input('Enter the temperature: \n'))

# prompt users to select the temperature scale
scale = int(input('Enter the temperature conversion scale: (-1- for Celsius and -2- for Fahrenheit ) \n'))

# condition based on user input
if scale == 1:
    converttofahrenheit(floatTemperature)
else :
    converttocelsius(floatTemperature)