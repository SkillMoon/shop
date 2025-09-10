def SaveShopList(shop_list):
    with open('shoplist.txt', 'w') as file:
        for item in shop_list:
            file.write(str(item) + '\n')

while True:
    shop_list = list()
    with open("shoplist.txt", "r") as file:
        items = file.readlines()
        if items:
            shop_list = [item.strip() for item in items]
    print("**Shop List**")
    print("1. View Shop List")
    print("2. Add Shop Item")
    print("3. Remove Shop Item")
    print("4. view shop list")
    print("4. Exit")
    print("-" * 20)
    user_input = input("Enter your choice: ")
    if user_input == "1":
        print("***Shop List***")
        for item in shop_list:
            print(f"- {item}")
        print("-" * 20)
    elif user_input == "2":
        item_name_a = input("Enter item name: ")
        shop_list.append(item_name_a)
        SaveShopList(shop_list)
        print("successfully added")
    elif user_input == "3":
        item_name_r = input("Enter item name: ")
        shop_list.remove(item_name_r)
        SaveShopList(shop_list)
        print("successfully removed")
    elif user_input == "4":
<<<<<<< HEAD
        print("**Shop List**")
=======
        print("Shop List")
>>>>>>> feature
        for item in shop_list:
            print(f"- {item}")
        print("-" * 20)
    elif user_input == "5":
        break
    else:
        print("invalid input")