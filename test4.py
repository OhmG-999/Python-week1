
# declare variable with exchange rate for both currencies and initialise the float variable 'result'
floatGBP = 0.844859456
floatEUR = 1.18362882
floatResult = 0.0

# prompt users for the amount and convert the string to float
amount = float(input('Enter the amount: \n'))

# prompt users to select the base currency
curr = input('Select your base currency ( - 1 - for GPB and - 2 - for EUR) \n')

# condition based on the user input
if (curr == 1):
    floatResult = round(amount*floatGBP, 2)
    print('€ ',floatResult)
else:
    floatResult = round(amount/floatEUR, 2)
    print('£ ', floatResult)

