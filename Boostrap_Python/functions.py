#!/usr/bin/env python3
fruit = "apples"
quantity = 3
pie_crust = "empty"
isOvenOn = False

def prepMyFruit(quantity,fruit,pie_crust):

    print(f"You put {quantity} {fruit} on the crust")
    pie_crust = "filled with delicious apples"
    return(pie_crust)

pie_crust = prepMyFruit(3, "apples", "empty")
print("my pie is", pie_crust)