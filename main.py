# Importing Everything; Dictionary, Customer Class and its Methods from profile.py Module
from profile import *


# Customer Creation
customer1 = Customer("1", "Ernest", "ernest@gmail.com", "0549129007", "Acrra, Ghana")
customer1.create()

customer2 = Customer("2", "Mimshach", "mims@gmail.com", "0549866708", "Weija, Ghana")
customer2.create()

customer3 = Customer("3", "Felix", "felix@gmail.com", "0208356790", "Hohoe, Ghana")
customer3.create()


# Customer List
print("CUSTOMER MANAGEMENT SYSTEM")
print("ID NAME   EMAIL           PHONE       ADDRESS")
customer1.display()
customer2.display()
customer3.display()

print("\n")


#Updating a Customer
print("UPDATING A CUSTOMER")
print("ID NAME   EMAIL           PHONE       ADDRESS")
customer1.update(name="Bless")
customer1.display()
print("Customer updated successfully! \n")  



#Deleting a Customer
print("DELETING A CUSTOMER")
customer2.delete()


#Searching for a Customer
print("SEARCHING FOR A CUSTOMER")
customer1.search_customer("2")