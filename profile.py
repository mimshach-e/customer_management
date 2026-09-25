#Customer Dataset
customers_data = {}

FIELDS = ("name", "email", "phone", "address")
HEADER = f"{'ID':<5}{'NAME':<12}{'EMAIL':<24}{'PHONE':<13}{'ADDRESS'}"


# Generating Next ID Automatically for each Customer
def next_id():
    if not customers_data:
        return 1
    return max(customers_data) + 1    


# Checking if customers email value already exist
def email_exists(email, exclude=None):
    return any(c.email.lower() == email.lower() and c.customer_id != exclude
    for c in customers_data.values())

# Defining what is not found
def get_customer(customer_id):
    customer = customers_data.get(customer_id)
    if customer is None:
        print(f"The Customer with the ID {customer_id} does not exist!")
    return customer    


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
        print(f"{self.customer_id:<5}{self.name:<12}{self.email:<24}"
              f"{self.phone:<13}{self.address}")

    
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
    def delete(self):
        if self.customer_id not in customers_data:
            print(f"Customer {self.customer_id} was already deleted! \n")
            return
        del customers_data[self.customer_id]
        print(f"Customer {self.customer_id} {self.name} deleted successfully! \n")

    def __repr__(self):
        return (f"Customer({self.customer_id}, {self.name}, {self.email}, "
                f"{self.phone}, {self.address})")


# Method for Searching Customers by ID
def search_customer(customer_id):
    customer = get_customer(customer_id)
    if customer:
        print("Customer found: ", end="")
        customer.display()  


# Method for Searching for Customer by name
def search_by_name(term):
    matches = [c for c in customers_data.values() if term.lower() in c.name.lower()]
    if not matches:
        print(f"No customer mactches the name '{term}'!")
        return
    print(f"{len(matches)} match(es)found:")
    print(HEADER)

    for customer in matches:
        customer.display()

  
# Display All Customers
def display_all():
    print(HEADER)
    print("-" * len(HEADER))
    if not customers_data:
        print("No customer added yet")
    for customer in customers_data.values():
        customer.display()
    print(f"\n {len(customers_data)} customer(s) added: \n")    

    
          
    