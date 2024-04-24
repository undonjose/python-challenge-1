# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

order_list = ["menu item name", "item price", "quantity ordered"]

print("Welcome to the variety food truck.")

place_order = True
while place_order:
    
    print("From which menu would you like to order? ")
    
    i = 2
  
    menu_items = {}

    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

      menu_category = input("Type menu number: ")

    if menu_category.isdigit():

        if int(menu_category) in menu_items.keys():
           
            menu_category_name = menu_items[int(menu_category)]
           
            print(f"You selected {menu_category_name}")

            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Line # | Line name                | Cost")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
               
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
        
            menu_choice = input("Type menu number to view or q to quit: ")


            if menu_choice.isdigit():

   
                if int(menu_choice) in menu_items.keys():


                
       
                print(f"You selected {menu_category_name}")

             
                     menu_category_name = menu_items[int(menu_category)]

            
                    menu_choice_name = input("How many units do you want?:")

                  
                    if menu_choice_name.isdigit():
                        print(menu_category_name)
                    else:
                        default = 1
                
                    print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                    print(f"{i}      | {key}{item_spaces} | ${value}")

                    print(f"{menu_choice} was not an option.")

             
                print(f"{menu_category} was not a option.")
        else:
          
            print(f"{menu_category} was not a option.")
    else:

        print("For to choose something.")

    while True:
      
        keep_ordering = input("Do you want more stuff? (Y)es or (N)o ")

       
                if keep_ordering == "Y":
                    print(f' "what else do you want to order: {menu_choice}')
              
                else:
                    print("THANK YOU!!!!!")
                
            
                 
              
                print("Thank you!! Gracias!! Merci!! Danke!!")
               

          
                if keep_ordering == "N":
                    break

  

print("This is what we are preparing for you.\n")


 print("Line # | Line name                | Cost")
print("--------------------------|--------|----------")


for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

    Snacks = menu[Key1, value1]
    Meals = menu[Key2, value2]
    Drinks = menu[Key3, value3]
    Dessert = menu[Key4, value4]


    num_item_spaces = 24 - len(key + key2) - 3


    item_spaces = " " * num_item_space


    print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
    print(f"{i}      | {key}{item_spaces} | ${value}")


if type(value) is dict:
    to_be_paid =  [sum(menu_choice_name)] * {value2}
else:
    to_be_paid =  [sum(menu_choice_name)] * {value}

print(f'Money time! $ {to_be_paid}')
