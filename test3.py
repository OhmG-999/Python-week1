# Suppose the cover price of a book is $24.95,
# but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and
# 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?

floatBookInitialPrice = 24.95
floatDiscount = 1 - 0.4
floatSingleBookShipping = 3.00
floatAdditionalBookShipping = 0.75
floatTotal = 0.00;

# This calculate the gross price for a book
floatBookGrossPrice = round(floatBookInitialPrice * floatDiscount, 2)

# Get user input for quantity
userInput = input('Please enter the quantity of book needed: \n')

# Create loop until the user enters 0
while userInput != 0 :
    if (int(userInput) > 1):
        floatTotal = (floatBookGrossPrice + floatSingleBookShipping) + (floatBookGrossPrice * (int(userInput) - 1)) +((int(userInput) - 1) * floatAdditionalBookShipping)
    else :
        floatTotal = floatBookGrossPrice + floatSingleBookShipping

    print('Total cost is: ', floatTotal)

    userInput = input('Please enter the quantity of book needed: \n')

print('Thank you for your visit')