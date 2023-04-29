
inventory = ["Ketchup" , "Mustard" , "Mayonaise"]

def check_inventory(): #checks inventory
    sorted(inventory)
    for i in range(len(inventory)):  
        print(inventory[i])
        i += 1
    
def add_inventory():
    i = 0
    
    numAdd = int(input("how many Items would you like to add?: "))
    
    while i < numAdd:
        itemAdd = input("Enter an item you would like to add: ") #adds items to Inventory list
        inventory.append(itemAdd)
        i += 1
        
    while True:
        moreAdd = input("Would you like to add more? Y/N: ").lower() #asks if there is more to add and checks for valid response 
        if moreAdd == "n":
            check_inventory()
            main()
        if moreAdd == "y":
            add_inventory()
        

def delete_inventory():
    while True:
        print("Here is your current inventory: ")
        check_inventory()
        itemDelete = input("Enter the item you wish to delete: ") #shows current inventory and asks user to enter items they wish to delete
        inventory.remove(itemDelete)
        
        while True:
            moreDelete = input("Would you like to delete more? Y/N?: ").lower() #checks to see if there is more the user wants to delete
            if moreDelete == "n":
                check_inventory()
                main()
            elif moreDelete == "y":
                delete_inventory()
        






def main():
    print("Hi please check your inventory:  Press 1 to check inventory  Press 2 to add to inventory  Press 3 to delete from inventory")
    
    while True:    # Ensures a Valid response from the user
        userInput = input()
        if userInput == "1":
            check_inventory()
        if userInput == "2":
            add_inventory()
        if userInput== "3":
            delete_inventory()
        print("Please press 1 to check inventory  Press 2 to add to inventory  Press 3 to delete from inventory")
        
        
        
        
if __name__ == "__main__":
  main()