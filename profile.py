#Customer Dataset
customers_data = {}

# Customer Class
class Customer:
    
    # Method to Assign Property Values to Objects
    def __init__(self, customer_id, name, email, phone, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        

    # Customer Creation Method
    def create(customer):
        customers_data[customer.customer_id] = customer
        print(f"Added {customer.name} as a new customer \n")


    # Method for Displaying Customer
    def display(self):
        print(f"{self.customer_id} {self.name} {self.email} {self.phone}  {self.address} \n")     

    
    # Method for Updating Customers
    def update(self, name=None, email=None, phone=None, address=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address

  
    # Method for Deleting Customers
    def delete(customer):
        del customers_data[customer.customer_id] 
        print(f"Customer {customer.customer_id} {customer.name} deleted successfully! \n")  
    
    def __repr__(self):
        return f"Customer({self.customer_id}, {self.name}, {self.email}, {self.phone}, {self.address})"



    # Method for Searching Customers 
    def search_customer(self, customer_id):
        if customer_id in customers_data:
            customer = customers_data[customer_id]
            print(f"Customer found: {customer.customer_id} {customer.name} {customer.email} {customer.phone} {customer.address} \n")
        else:
            print(f"The Customer with the ID {customer_id} does not exist!")    
  

    