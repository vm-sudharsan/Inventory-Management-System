class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class InventoryManagementSystem:
    def __init__(self):
        self.products = {}
        self.admin_password = "admin123"
        self.admin_logged_in = False
        self.users = {}
        self.user_logged_in = None

    def add_product(self, name, price, quantity):
        if name in self.products:
            print(f"Product {name} already exists.")
        else:
            self.products[name] = Product(name, price, quantity)
            print(f"Product {name} added successfully.")

    def update_product(self, name, price=None, quantity=None):
        if name in self.products:
            if price is not None:
                self.products[name].price = price
            if quantity is not None:
                self.products[name].quantity = quantity
            print(f"Product {name} updated successfully.")
        else:
            print(f"Product {name} does not exist.")

    def delete_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f"Product {name} deleted successfully.")
        else:
            print(f"Product {name} does not exist.")

    def inventory(self):
        if not self.products:
            print("No products in inventory.")
        else:
            for name, product in self.products.items():
                print(f"Name: {name}, Price: {product.price}, Quantity: {product.quantity}")

    def admin_login(self):
        password = input("Enter admin password: ")
        if password == self.admin_password:
            print("Login successful!")
            self.admin_logged_in = True
        else:
            print("Incorrect password. Access denied.")

    def admin_menu(self):
        while self.admin_logged_in:
            print("\nAdmin Menu")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Delete Product")
            print("4. Inventory")
            print("5. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                self.add_product(name, price, quantity)
            elif choice == '2':
                name = input("Enter product name: ")
                price = float(input("Enter new product price: "))
                quantity = int(input("Enter new product quantity: "))
                self.update_product(name, price, quantity)
            elif choice == '3':
                name = input("Enter product name to delete: ")
                self.delete_product(name)
            elif choice == '4':
                self.inventory()
            elif choice == '5':
                self.admin_logged_in = False
                print("Logged out.")
            else:
                print("Invalid choice. Please try again.")

    def user_login(self):
        user_id = input("Enter user ID or mobile number: ")
        if user_id in self.users:
            print("Login successful!")
            self.user_logged_in = user_id
        else:
            print("User not found. Please register first.")

    def user_bill(self):
        if self.user_logged_in:
            total_price = 0
            while True:
                product_name = input("Enter product name to purchase (or 'done' to finish): ")
                if product_name.lower() == 'done':
                    break
                if product_name in self.products:
                    quantity = int(input("Enter quantity: "))
                    if quantity <= self.products[product_name].quantity:
                        self.products[product_name].quantity -= quantity
                        total_price += self.products[product_name].price * quantity
                    else:
                        print("Not enough quantity available.")
                else:
                    print("Product not found.")

            print(f"Total bill for user {self.user_logged_in}: ${total_price}")
        else:
            print("User not logged in. Please login first.")

    def register_user(self):
        user_id = input("Enter user ID or mobile number: ")
        if user_id in self.users:
            print("User already exists.")
        else:
            self.users[user_id] = {}
            print(f"User {user_id} registered successfully.")

    def main_menu(self):
        while True:
            print("\nWelcome to Inventory Management System")
            print("1. Admin Login")
            print("2. User Login")
            print("3. Register User")
            print("4. Exit")

            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                self.admin_login()
                if self.admin_logged_in:
                    self.admin_menu()
            elif user_choice == "2":
                self.user_login()
                if self.user_logged_in:
                    self.user_bill()
                    self.user_logged_in = None
            elif user_choice == "3":
                self.register_user()
            elif user_choice == "4":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    inventory_system = InventoryManagementSystem()
    inventory_system.main_menu()
