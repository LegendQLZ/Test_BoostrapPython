#!/usr/bin/env python3
fruit = "apples"
quantity = 3
pie_crust = "empty"
is_oven_on = False

def prepMyFruit(quantity,fruit,pie_crust):

    print(f"You put {quantity} {fruit} on the crust")
    pie_crust = "filled with delicious apples"
    return(pie_crust)

def turn_on_oven(is_oven_on):

    is_oven_on = "True"
    return(is_oven_on)

pie_crust = prepMyFruit (3, "apple", "empty")
print("my pie is", pie_crust)
print("Is the oven turned on ?", turn_on_oven(is_oven_on))
