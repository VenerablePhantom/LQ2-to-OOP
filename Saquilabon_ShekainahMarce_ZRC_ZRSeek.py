# list of reported lost items
items = [
    {
        "name": "Black Wallet",
        "category": "Wallet or Money",
        "location": "Stundents Lounge",
        "status": "Found",
        "reporter": "Vic Fuentes"
    },
    
    {
        "name": "Blue Water Bottle",
        "category": "Waterbottle",
        "location": "Dormitory 1, Lobby",
        "status": "Found",
        "reporter": "Jaime Preciado"
    },
    
    {
        "name": "Scientific Calculator",
        "category": "School Supply",
        "location": "Academic Building 3",
        "status": "Lost",
        "reporter": "Tony Perry"
    }
]

# main menu
def main_menu():
    print("\n================================= MAIN MENU ==================================")
    print("\n1. Search Item")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. View All Items")
    print("6. Exit")
    menu = input("Pick an option: ").strip()

    return menu

# search item
def search_item():
    print("\n================================ SEARCH ITEM =================================")
    print("\n1. Accessory")
    print("2. Electronic")
    print("3. School Supply")
    print("4. Wallet or Money")
    print("5. Waterbottle")
    print("6. Others")
    category_choice = input("Choose a category: ").strip()

    categories = {
        "1": "Accessory",
        "2": "Electronic",
        "3": "School Supply",
        "4": "Wallet or Money",
        "5": "Waterbottle",
        "6": "Others"
    }

    if category_choice not in categories:
        print("\nInvalid category.")
        search_item()

    category = categories[category_choice]

    found_items = []

    for item in items:
        if item["category"].lower() == category.lower():
            found_items.append(item)

    if len(found_items) == 0:
        print("\nNo items found in this category.")
        print("\nWould you like to: ")
        print("1. Go back to SEARCH ITEM")
        print("2. Report missing item to ADD ITEM")
        print("3. Go back to MAIN MENU")
        option_choice = input("Choose an option: ")

        if option_choice == "1":
            print("\nRedirecting to SEARCH ITEM...")
            search_item()

        elif option_choice == "2":
            print("\nRedirecting to ADD ITEM...")
            add_item()

        elif option_choice == "3":
            print("\nRedirecting to MAIN MENU...")

        else:
            print("\nInvalid response.")
            print("\nRedirecting to MAIN MENU...")
            
        return

    print("\n============================== SEARCH RESULTS ===============================")

    for number, item in enumerate(found_items, start=1):
        print("\nItem", number)
        print("Name     :", item["name"])
        print("Category :", item["category"])
        print("Location :", item["location"])
        print("Status   :", item["status"])
        print("Reporter :", item["reporter"])

    claim = input("\nHave you found the item you are looking for? (yes/no): ").strip().lower()

    if claim == "yes":
        print("\nPlease claim the item at the Registrar.")
        
    elif claim == "no":
        print("\nWould you like to: ")
        print("1. Go back to SEARCH ITEM")
        print("2. Report missing item to ADD ITEM")
        print("3. Go back to MAIN MENU")
        option_choice = input("Choose an option: ")

        if option_choice == "1":
            print("\nRedirecting to SEARCH ITEM...")
            search_item()

        elif option_choice == "2":
            print("\nRedirecting to ADD ITEM...")
            add_item()

        elif option_choice == "3":
            print("\nRedirecting to MAIN MENU...")
            main_menu()

        else:
            print("\nInvalid response.")
        
    else:
        print("\nInvalid response.")
        print("\nRedirecting to MAIN MENU...")

# add item
def add_item():
    print("\n================================== ADD ITEM ==================================")

    name = input("\nEnter the item name: ").strip()

    if name == "":
        print("Item name cannot be empty.")
        return

    print("\n1. Accessory")
    print("2. Electronic")
    print("3. School Supply")
    print("4. Wallet or Money")
    print("5. Waterbottle")
    print("6. Others")
    category_choice = input("Choose a category: ").strip()

    categories = {
        "1": "Accessory",
        "2": "Electronic",
        "3": "School Supply",
        "4": "Wallet or Money",
        "5": "Waterbottle",
        "6": "Others"
    }

    if category_choice not in categories:
        print("\nInvalid category.")
        print("\nRedirecting to MAIN MENU...")
        return

    category = categories[category_choice]

    location = input("\nWhere was the item lost/found? ").strip()

    if location == "":
        print("\nLocation cannot be empty.")
        print("\nRedirecting to MAIN MENU...")
        return

    status = input("\nIs the item Lost or Found? ").strip().title()

    if status != "Lost" and status != "Found":
        print("\nInvalid status. Please enter Lost or Found.")
        print("\nRedirecting to MAIN MENU...")
        return

    reporter = input("\nEnter your name: ").strip()

    if reporter == "":
        print("\nName cannot be empty.")
        print("\nRedirecting to MAIN MENU...")
        return

    new_item = {
        "name": name,
        "category": category,
        "location": location,
        "status": status,
        "reporter": reporter
    }

    items.append(new_item)

    print("\nItem successfully added to ZRSeek!")
    print("\nRedirecting to MAIN MENU...")

# update item
def update_item():
    print("\n================================ UPDATE ITEM =================================")

    if len(items) == 0:
        print("\nThere are currently no items.")
        print("\nRedirecting to MAIN MENU...")
        return

    view_all_items()

    try:
        choice = int(input("\nEnter the item number you want to update: "))

        if choice < 1 or choice > len(items):
            print("\nInvalid item number.")
            print("\nRedirecting to MAIN MENU...")
            return

    except ValueError:
        print("\nPlease enter a valid number.")
        print("\nRedirecting to MAIN MENU...")
        return

    item = items[choice - 1]

    print("\nLeave a field blank if you do not want to change it.")

    new_name = input("\nNew item name [" + item["name"] + "]: ").strip()

    if new_name != "":
        item["name"] = new_name

    new_location = input("\nNew location [" + item["location"] + "]: ").strip()

    if new_location != "":
        item["location"] = new_location

    new_status = input("\nNew status (Lost/Found) [" + item["status"] + "]: ").strip().title()

    if new_status == "Lost" or new_status == "Found":
        item["status"] = new_status
        
    elif new_status != "":
        print("\nInvalid status. Previous status was kept.")
        print("\nRedirecting to MAIN MENU...")

    new_reporter = input("\nNew reporter [" + item["reporter"] + "]: ").strip()

    if new_reporter != "":
        item["reporter"] = new_reporter

    print("\nItem successfully updated!")
    print("\nRedirecting to MAIN MENU...")

# remove item
def remove_item():
    print("\n================================ REMOVE ITEM =================================")

    if len(items) == 0:
        print("\nThere are currently no items.")
        print("\nRedirecting to MAIN MENU...")
        return

    view_all_items()

    try:
        choice = int(input("\nEnter the item number you want to remove: "))

        if choice < 1 or choice > len(items):
            print("\nInvalid item number.")
            print("\nRedirecting to MAIN MENU...")
            return

    except ValueError:
        print("\nPlease enter a valid number.")
        print("\nRedirecting to MAIN MENU...")
        return

    item = items[choice - 1]

    print("\nYou selected:", item["name"])

    confirmation = input("Are you sure you want to remove this item? (yes/no): ").strip().lower()

    if confirmation == "yes":
        removed = items.pop(choice - 1)

        print("\n" + removed["name"] + " has been removed from ZRSeek.")

    elif confirmation == "no":
        print("\nRemove operation cancelled.")
        print("\nRedirecting to MAIN MENU...")

    else:
        print("\nInvalid response.")
        print("\nRedirecting to MAIN MENU...")

# view items
def view_all_items():
    print("\n============================== VIEW ALL ITEMS ================================")

    if len(items) == 0:
        print("\nNo items have been recorded.")
        print("\nRedirecting to MAIN MENU...")
        return

    for number, item in enumerate(items, start=1):
        print("\nItem", number)
        print("Name     :", item["name"])
        print("Category :", item["category"])
        print("Location :", item["location"])
        print("Status   :", item["status"])
        print("Reporter :", item["reporter"])
        print("---------------------------------------------")

# introduction
print("==============================================================================")
print("                                    ZRSeek                                    ")
print("==============================================================================")
print("\n'Do you not realize that I'm gone?' - Lost and Found by Xdinary Heroes")
print()
print("This allows the people of ZRC to seek for their lost items")
print("via a simple search system designed to be easy to navigate.")
print()
print("INTENDED USERS: Students, Faculty, and Staff of PSHS-ZRC")

# main program loop
while True:

    choice = main_menu()

    if choice == "1":
        search_item()

    elif choice == "2":
        add_item()

    elif choice == "3":
        update_item()

    elif choice == "4":
        remove_item()

    elif choice == "5":
        view_all_items()

    elif choice == "6":
        print("\nAdios!")
        print("Thank you for using ZRSeek.")
        print("Stan Xdinary Heroes - shek2026")
        break

    else:
        print("\nInvalid option.")
        print("Please choose a number from 1 to 6.")
