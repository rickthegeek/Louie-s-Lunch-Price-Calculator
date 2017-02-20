#Project: CIS 177 WEEK 5 PROJECT
#Project Location: projects\cis177\louie
#File: louie.py
#Purpose: Lunch ordering System, request type and size of meal
#         repeat as desired, and generate a price w/tax
#Revision: 1.0 / 20 FEB 2017
#Created: 20 FEB 2017
#Author: Rick Miller <rick@rickthegeek.com>

# This function will generate a menu, and allow the user to enter a choice.
# we will use a dict to store the items and prices. 

# these three funnctions return the price of a meal
# based on the size code given
# REQUIRES: lower case letter indicating size (m, l for mini or large)
# REQUIRES: anything else will assume a regular size meal
# RETURNS: float indicating the price for the meal -
# RETURNS: mini is single portion of meat plus one side
# RETURNS: large is double meat plus three sides
# RETURNS: regular (default) is double plus one side

def price_beef_meal(size):
    if size == 'm': # mini size
        return 4.00 # single portion ($3) plus one side ($1) = $4
    elif size == 'l': #large size
        return 9.00 # doubple portion ($6) plus three sides ($1 * 3) = $9
    else: # assume regular size
        return 7.00 # double portion ($6) plus one side ($1) = $7

def price_chicken_meal(size):
    if size == 'm': # mini (same as above...)
        return 3.50 # single portion ($2.50), plus one side ($1)
    elif size == 'l': # large size
        return 8.00 # double plus three sides
    else: # assume regular size
        return 6.00 # double plus one side

def price_pork_meal(size):
    if size == 'm': # mini size
        return 3.00 # single plus one side
    elif size == 'l': # large size etc...
        return 6.00 # double plus three sides
    else: # assume regular size
        return 4.00 # double plus one side

# Return a lower case letter, which is the first letter
# of the user's entry
# REQUIRES: a string to prompt the user with
# RETURNS: a one character string, the first character of the user's entry

def get_a_lowercase_letter(prompt):
    entryString = ''
    while entryString == '': # repeat until something is entered...
        entryString = input(prompt)
    entryString = entryString[0] # cut off all except the first letter
    return entryString


# This function will get the user input and return a single lower case letter
# which is the first character of the user's entry. 
# REQUIRES: a set of letters for allowed entries
# RETURNS: lower case letter, which is the first character of the user's entry.

def get_checked_entry(letters):
    entryString = get_a_lowercase_letter('Enter your choice: ')
    while not entryString in letters:
        print('Sorry, try again!')
        entryString = get_a_lowercase_letter('Enter your choice: ')
    return entryString

# This function generates the tax of the order and adds it to the price
# REQUIRES: order price
# RETURNS: order price plus 8.25%

def addTax(price):
    return price + (price * 0.0825)

# This function prints the store menu. No paramaters or return.

def printMenu():
    print('\nPrices include:')
    print('Mini meal: single portion of meat plus one side')
    print('Regular meal: double portion of meat plus one side')
    print('Large meal: double portion of meat plus three sides\n\n')
    print('Meat\t\tMini\tRegular\tLarge')
    print('B - beef\t$4.00\t$7.00\t$9.00')
    print('C - chicken\t$3.50\t$6.00\t$8.00')
    print('P - pork\t$3.00\t$4.00\t$6.00\n')
    print('X - order complete')
    return

# main code starts here

orderTotal = 0.00 # This is where we store the total of the order
mealChoice = ''
mealPriceList = []
sizeChoice = ''
print('\nWelcome to Louie\'s Lunch Counter')
print('--------------------------------\n')
while not (mealChoice == 'x'): # the whole program repeats until the user enters 'x'
    printMenu()
    mealChoice = get_checked_entry(['b', 'c', 'p', 'x'])
    if not (mealChoice == 'x'): # user entered a valid entry that wasn't X
        sizeChoice = get_a_lowercase_letter('What size? M - mini, L - large, R - regular: ') # ask what size they want
    if mealChoice == 'b':
        mealPrice = price_beef_meal(sizeChoice)
    elif mealChoice == 'c':
        mealPrice = price_chicken_meal(sizeChoice)
    else: 
        mealPrice = price_pork_meal(sizeChoice) # we know it must be a pork meal, because the entry routine only allows b, c, or p
    if not (mealChoice == 'x'): # don't need to display the prices if user choses X
        print('\nMeal Price: $%3.2f' % mealPrice) # print the price, tax, and total
        print('Tax: $%3.2f' % (mealPrice * 0.0825))
        mealPrice = addTax(mealPrice)
        print('Meal Price with Tax: $%3.2f' % mealPrice)
        orderTotal = orderTotal + mealPrice # add the price to the total
        mealPriceList.append(mealPrice) # add the meal price to the list we have going for the prices
print('\nMeal prices:')
orderCount = 1 # computer starts from zero but this won't make sense to the user
while (orderCount - 1) < len(mealPriceList): # but LEN counts from zero....
    print('Order', orderCount, ':\t$%3.2f' % mealPriceList[orderCount -1]) # ... so we display the order price from the list
    orderCount += 1 # then go on to the next order
print('\nFinal Order Total: $%3.2f' % orderTotal) # give the user the final order total


