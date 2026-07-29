from menu import food_menu

cart = []


def add_to_cart():

    item = int(input("Enter Item Number : "))

    if item in food_menu:

        cart.append(food_menu[item])

        print(food_menu[item][0], "added to cart")

    else:

        print("Invalid Item")


def view_cart():

    if len(cart) == 0:

        print("\nCart is Empty")

        return

    print("\n====== YOUR CART ======")

    total = 0

    for food in cart:

        print(food[0], "- ₹", food[1])

        total = total + food[1]

    print("-----------------------")

    print("Total Bill : ₹", total)