def login():

    print("\n===== FoodExpress Login =====")

    username = input("Enter Username : ")
    password = input("Enter Password : ")

    print("\nSelect Role")
    print("1. Customer")
    print("2. Restaurant Owner")
    print("3. Delivery Agent")
    print("4. Admin")

    choice = input("Enter your choice : ")

    if choice == "1":
        role = "Customer"

    elif choice == "2":
        role = "Restaurant Owner"

    elif choice == "3":
        role = "Delivery Agent"

    elif choice == "4":
        role = "Admin"

    else:
        print("Invalid Role")
        return None

    print("\nLogin Successful")
    print("Welcome", username)
    print("Role :", role)

    return role