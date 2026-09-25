from customer import Customer
from manager import CustomerManager
from exceptions import CustomerNotFoundError, InvalidInputError


def read_customer_details(existing=None):
    """
    Prompts the user for each field in Customer.FIELDS (name, email,
    phone, address) using input(). The field list itself is not
    repeated here — it's read straight from Customer.FIELDS, so this
    one loop works for every field, present or future.

    If `existing` is given (an update), pressing Enter keeps the
    current value for that field instead of overwriting it.
    """
    details = {}
    for field in Customer.FIELDS:
        current = getattr(existing, field, "") if existing else ""
        prompt = f"{field.capitalize()}"
        prompt += f" [{current}]: " if existing else ": "
        value = input(prompt).strip()
        if value == "":
            if existing:
                continue  # keep current value
            raise InvalidInputError(f"{field} cannot be empty.")
        details[field] = value
    return details


def create_customer(manager):
    print("\n-- Create Customer --")
    try:
        details = read_customer_details()
        customer = manager.create_customer(**details)
        print(f"Created: {customer}")
    except InvalidInputError as e:
        print(f"Error: {e}")


def list_customers(manager):
    print("\n-- All Customers --")
    customers = manager.list_customers()
    if not customers:
        print("No customers found.")
    for c in customers:
        print(c)


def update_customer(manager):
    print("\n-- Update Customer --")
    try:
        customer_id = int(input("Customer ID to update: ").strip())
        existing = manager.get_customer(customer_id)
        print("Press Enter to keep the current value for a field.")
        details = read_customer_details(existing=existing)
        customer = manager.update_customer(customer_id, **details)
        print(f"Updated: {customer}")
    except ValueError:
        print("Error: ID must be a number.")
    except CustomerNotFoundError as e:
        print(f"Error: {e}")


def delete_customer(manager):
    print("\n-- Delete Customer --")
    try:
        customer_id = int(input("Customer ID to delete: ").strip())
        customer = manager.delete_customer(customer_id)
        print(f"Deleted: {customer}")
    except ValueError:
        print("Error: ID must be a number.")
    except CustomerNotFoundError as e:
        print(f"Error: {e}")


def search_customers(manager):
    print("\n-- Search Customers --")
    print(f"Search by one field ({', '.join(Customer.FIELDS)}).")
    field = input("Field name: ").strip().lower()
    if field not in Customer.FIELDS:
        print(f"Error: '{field}' is not a searchable field.")
        return
    value = input(f"Value for '{field}': ").strip()
    results = manager.search_customers(**{field: value})
    if results:
        for c in results:
            print(c)
    else:
        print("No matches found.")


MENU = {
    "1": ("Create customer", create_customer),
    "2": ("List customers", list_customers),
    "3": ("Update customer", update_customer),
    "4": ("Delete customer", delete_customer),
    "5": ("Search customers", search_customers),
    "6": ("Exit", None),
}


def print_menu():
    print("\n===== Customer Management =====")
    for key, (label, _) in MENU.items():
        print(f"{key}. {label}")


def main():
    manager = CustomerManager()
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        entry = MENU.get(choice)
        if entry is None:
            print("Invalid option, try again.")
            continue
        label, action = entry
        if choice == "6":
            print("Goodbye!")
            break
        action(manager)


if __name__ == "__main__":
    main()