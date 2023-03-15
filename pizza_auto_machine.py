print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()

if size==str("S"):
    price=15
    if add_pepperoni==str("Y"):
        price=price+2
        if extra_cheese==str("Y"):
            price=price+1
            print(f"Your final bill is: ${price}.")
        else:
            print(f"Your final bill is: ${price}.")
    else:
        if extra_cheese==str("Y"):
            price=price+1
            print(f"Your final bill is: ${price}.")
        else:
            print(f"Your final bill is: ${price}.")
elif size==str("M"):
    price=20
    if add_pepperoni==str("Y"):
        price=price+3
        if extra_cheese==str("Y"):
            price=price+1
            print(f"Your final bill is: ${price}.")
        else:
            print(f"Your final bill is: ${price}.")
    else:
        if extra_cheese==str("Y"):
            price=price+1
            print(f"Your final bill is: ${price}.")
        else:
            print(f"Your final bill is: ${price}.")
else:
    price=25
    if add_pepperoni==str("Y"):
        price=price+3
        if extra_cheese==str("Y"):
            price=price+1
            print(f"Your final bill is: ${price}.")
        else:
            print(f"Your final bill is: ${price}.")
    else:
        if extra_cheese==str("Y"):
            price=price+1
            print(f"Your final bill is: ${price}.")
        else:
            print(f"Your final bill is: ${price}.")
