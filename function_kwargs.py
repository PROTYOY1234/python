def pizza_order(Name, Address, **Toppings):
    print(f"Pizza was ordered by {Name}")
    print(f"Deliver The Pizza at {Address}")
    price = 18.00
    for topping in Toppings.items():
        price += 2.00
    print("The total Price is:", price)
    return price

total_price = pizza_order("Protyoy", "Kanksa Ganguly Para", jalapenous=True, Extra_Cheese=True, Ham=True)
print(total_price)
