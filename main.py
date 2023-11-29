order = input("what would you like to order")
pizza_price=40
topping_price=8

if(order=="pizza"):
    print("you ordered pizza")
    toppings = input("do you want any toppings")
    if(toppings == "pineapple" or toppings == "corn"):
        print("your price is: ")
        print(pizza_price+topping_price)
    else:
        print("your price is: ")
        print(pizza_price)
        
