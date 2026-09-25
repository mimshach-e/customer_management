# Importing Everything; Dictionary, Customer Class and its Methods from profile.py Module
from profile import *

# Checks

def read_customer_id(prompt="Enter Customer ID: "):
    while True:
        raw_id = input(prompt).strip()
        if raw_id == "":
            return None
        if raw_id.isdigit():
            return int(raw_id)
        print(f"{raw_id} is not a valid ID. Enter a whole number") 
    
    
            


def ask_fields(existing=None):
    values = {}
    """ looping over fields in the dictionary to ask user to create or update customer"""
    for fields in FIELDS:
        current = getattr(existing, fields, "") if existing else ""
        hint = f"[{current}]: " if current else ": "
        while True:
            answer = input(fields.capitalize() + hint).strip()
            if answer:
                values[fields] = answer
                break
            if current:
                values[fields] = current
                break
            print(f"{fields.capitalize()} cannot be empty")
    return values   


# Customer Creation
def create_customer():
    print("\n CREATE NEW CUSTOMER")
    while True:
        values = ask_fields()
        if not email_exists(values["email"]):
            break
        print(f"{values['email']} already belongs to another customer. Enter a different one.")
     
    customer = Customer(next_id(), values["name"], values["email"], values["phone"], values["address"])
    customer.create()
    

# Updating Customer
def update_customer():
    customer_id = read_customer_id("Enter the ID of the customer you want to update: ")
    if customer_id is None:
        return
    customer = get_customer(customer_id)
    if customer is None:
        return
    print("Leave blank to keep the current value.")
    customer.update(**ask_fields(existing=customer))
    print("Customer updated successfully! \n")
    customer.display()   
         



# Deleting a Customer
def delete_customer():
    customer_id = read_customer_id("Enter the ID of the customer you want to update: ")
    if customer_id is None:
        return
    customer = get_customer(customer_id)
    if customer:
        confirm = input(f"Are you sure you want to delete {customer.name}? (y/n): ").strip().lower()
        if confirm == "y":
            customer.delete()
        else:
            print("Deletion cancelled.")


# Searching for a Customer
def find_customer():
    print("\n Search by 1. ID or 2. name")
    if input("Choice: ").strip() == "1":
        customer_id = read_customer_id()
        if customer_id is not None:
            search_customer(customer_id)
    else:
        term = input("Enter full name of part of name: ").strip()
        if term:
            search_by_name(term)        
    



# Dashboard Menu Display
def dashboard_menu():
    while True:
        print("\n CUSTOMER MANAGEMENT SYSTEM")
        print("1. Create a Customer")
        print("2. View Customer List")
        print("3. Update a Customer")
        print("4. Delete a Customer")
        print("5. Search for a Customer")
        print("0. Quit")
    


        choice = input("\n Please select an option: ").strip()
        if choice == "1":
            create_customer()
        elif choice == "2":
            display_all()
        elif choice == "3":
            update_customer()
        elif choice == "4":
            delete_customer()
        elif choice == "5":
            find_customer()
        elif choice == "0":
            print("Application closed")
            break
        else:
            print(f"'{choice}' is not a valid option.")






if __name__ == "__main__":
    dashboard_menu()



    

































# # Customer Creation
# customer1 = Customer("1", "Ernest", "ernest@gmail.com", "0549129007", "Acrra, Ghana")
# customer1.create()

# customer2 = Customer("2", "Mimshach", "mims@gmail.com", "0549866708", "Weija, Ghana")
# customer2.create()

# customer3 = Customer("3", "Felix", "felix@gmail.com", "0208356790", "Hohoe, Ghana")
# customer3.create()



# # Customer List
# print("CUSTOMER MANAGEMENT SYSTEM")
# print("ID NAME   EMAIL           PHONE       ADDRESS")
# customer1.display()
# customer2.display()
# customer3.display()

# print("\n")


# #Updating a Customer
# print("UPDATING A CUSTOMER")
# print("ID NAME   EMAIL           PHONE       ADDRESS")
# customer1.update(name="Bless")
# customer1.display()
# print("Customer updated successfully! \n")  



# #Deleting a Customer
# print("DELETING A CUSTOMER")
# customer2.delete()
# print(customers_data)         
# print(len(customers_data))

# print("\n")

# #Searching for a Customer
# print("SEARCHING FOR A CUSTOMER")
# customer1.search_customer("2")