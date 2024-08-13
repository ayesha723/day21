inventory=[{"id" : "#12" , "name" : "Tshirt" , "quantity" :"100 "},
           {"id" : "#13" , "name" : "pillows" , "quantity" :"50"},
           {"id" : "#14" , "name" : "shoes" , "quantity" :"200 "}]

def add_item():
    print("For adding an item in inventory , Enter these details :")
    id = int(input("Enter the id of item"))
    name =input("Enter the name of item")
    quantity = int(input("Enter the quantity of item"))

    inventory.append({"id": "" , "name" :"" , "quantity" : ""})


def view_inventory():
    print("Current Inventory:")
    for item in inventory:
        print(f"ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}")

def remove_product():

    id = int(input("Enter product ID to remove: "))
    
    global inventory
    inventory = [item for item in inventory if item["id"] != id]
    print("Product removed successfully.")
def main():
    while True:
        print("\nMain Menu:")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Update Product Quantity")
        print("4. Remove Product")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()

        elif choice == '3':
            remove_product()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()




