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

# This function will get the user input and return a single lower case letter
# which is the first character of the user's entry. 
# REQUIRES: a list of letters for allowed entries
# RETURNS: lower case letter, which is the first character of the user's entry.
