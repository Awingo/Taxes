""" Anthony Wingo
    CS Introduction into Computation
    Laboratory 5"""
import random

products = input("What is items do you have? ")
product_list = products.split(", ")
location = input("What is your location? ")  # Setting the second input

def output(location, product_list):
    print("SALES TAX CALCULATION PROGRAM")
    if get_sales_tax(location) == 0.08:
        print("You are in Birmingham so the sales tax is 0.08")
    else:
        print("You are outside Birmingham so the sales tax is 0.04")
    i = 1
    total = 0
    for product in product_list:
        print("The price of product " + str(i)  + " is " + str(get_price(product)))
        if get_excise_tax(product) > 0:
            print("     The excise tax is " + str(get_excise_tax(product)))
        else:
            print("     There are no excise taxes on this product")
        total = (total + get_total(location, product))
        print("     The total price is " + str(get_total(location, product)))
        print("The overall price is " + str(total))
        print("")
        i = i + 1

def get_price(product):
    if product.lower() == "gasoline":
        price = 20
    elif product.lower() == "tobacco":
        price = 10
    elif product.lower() == "alcohol":
        price = 15
    else:
        price = int(input("What is the price?"))
    return price


def get_excise_tax(product):
    """ Parameters: product
        Input: product
        output:product of get_price
        return:price"""

    if get_price(product) == 20:
        tax = 1.60
    elif get_price(product) == 10:
        tax = 5.00
    elif get_price(product) == 15:
        tax =  2.00
    else:
        tax = 0
    return tax


def get_sales_tax(location):                                      #Defining the parameter for get_loc function
    """ Parameters: Location
        Input: location/input
        output: salestax of the location
        return: salestax"""
    if location.lower() == "birmingham":                    #IF BIRMINGHAM is the city, it will return a higher tax
        sales_tax = 0.08
    else:
        sales_tax = 0.04
    return sales_tax


def get_total(location,product):
    """ Parameters: Location and Product
        input: all of the functions previously made
        output: total price of the three functions listed
        return: None"""
    return price + get_excise_tax(product) + (price * get_sales_tax())                         #Calling each function so that it will provide the total

output(location, product_list)
