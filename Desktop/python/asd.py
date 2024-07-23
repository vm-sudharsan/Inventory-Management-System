from pymongo import MongoClient

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class InventoryManagementSystem:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://sudharsanprakalathanvm2023ece:sudharsanprakalathanvm2023ece@cluster0.nlnaqhv.mongodb.net/")
        self.db = self.client["inventory_db"]
        self.products_collection = self.db["products"]
        self.users_collection = self.db["users"]
        self.sales_collection = self.db["sales"]
        self.admin_password = "admin123"
        self.admin_logged_in = False
        self.user_logged_in = None

    def add_product(self, name, price, quantity):
        if self.products_collection.find_one({"name": name}):
            print(f"Product {name} already exists.")
        else:
            self.products_collection.insert_one({"name": name, "price": price, "quantity": quantity})
            print(f"Product {name} added successfully.")

    def update_product(self, name, price=None, quantity=None):
        if self.products_collection.find_one({"name": name}):
            update_fields = {}
            if price is not None:
                update_fields["price"] = price
            if quantity is not None:
                update_fields["quantity"] = quantity
            self.products_collection.update_one({"name": name}, {"$set": update_fields})
            print(f"Product {name} updated successfully.")
        else:
            print(f"Product {name} does not exist.")

    def delete_product(self, name):
        if self.products_collection.find_one({"name": name}):
            self.products_collection.delete_one({"name": name})
            print(f"Product {name} deleted successfully.")
        else:
            print(f"Product {name} does not exist.")

    def view_inventory(self):
        products = self.products_collection.find()
        if products.count() == 0:
            print("No products in inventory.")
        else:
            print("\nInventory:")
            for product in products:
                print(f"Name: {product['name']}, Price: ₹{product['price']}, Quantity: {product['quantity']}")
            print()

    def view_product(self, name):
        product = self.products_collection.find_one({"name": name})
        if product:
            print(f"Name: {product['name']}, Price: ₹{product['price']}, Quantity: {product['quantity']}")
        else:
            print(f"Product {name} does not exist.")

    def search_product(self, keyword):
        products = self.products_collection.find({"name": {"$regex": keyword, "$options": "i"}})
        if products.count() == 0:
            print(f"No products found containing '{keyword}'.")
        else:
            for product in products:
                print(f"Name: {product['name']}, Price: ₹{product['price']}, Quantity: {product['quantity']}")

    def increase_stock(self, name, quantity):
        product = self.products_collection.find_one({"name": name})
        if product:
            new_quantity = product["quantity"] + quantity
            self.products_collection.update_one({"name": name}, {"$set": {"quantity": new_quantity}})
            print(f"Stock increased for product {name} by {quantity}.")
        else:
            print(f"Product {name} does not exist.")

    def decrease_stock(self, name, quantity):
        product = self.products_collection.find_one({"name": name})
        if product:
            if product["quantity"] >= quantity:
                new_quantity = product["quantity"] - quantity
                self.products_collection.update_one({"name": name}, {"$set": {"quantity": new_quantity}})
                print(f"Stock decreased for product {name} by {quantity}.")
                if new_quantity <= 5:
                    self.notify_admin_low_stock(name)
            else:
                print(f"Not enough stock available for product {name}.")
                self.notify_admin_low_stock(name)
        else:
            print(f"Product {name} does not exist.")

    def generate_sales_report(self):
        total_sales = 0
        sales = self.sales_collection.find()
        for sale in sales:
            total_sales += sale["total_price"]
        print(f"Total sales: ₹{total_sales}")

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
            print("4. View Inventory")
            print("5. View Product Details")
            print("6. Search Product")
            print("7. Increase Stock")
            print("8. Decrease Stock")
            print("9. Generate Sales Report")
            print("10. Low Stock Alert")
            print("11. Logout")

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
                self.view_inventory()
            elif choice == '5':
                name = input("Enter product name to view details: ")
                self.view_product(name)
            elif choice == '6':
                keyword = input("Enter keyword to search product: ")
                self.search_product(keyword)
            elif choice == '7':
                name = input("Enter product name to increase stock: ")
                quantity = int(input("Enter quantity to increase: "))
                self.increase_stock(name, quantity)
            elif choice == '8':
                name = input("Enter product name to decrease stock: ")
                quantity = int(input("Enter quantity to decrease: "))
                self.decrease_stock(name, quantity)
            elif choice == '9':
                self.generate_sales_report()
            elif choice == '10':
                self.low_stock_alert()
            elif choice == '11':
                self.admin_logged_in = False
                print("Logged out.")
            else:
                print("Invalid choice. Please try again.")

    def user_login(self):
        user_id = input("Enter user ID or mobile number: ")
        user = self.users_collection.find_one({"user_id": user_id})
        if user:
            password = input("Enter password: ")
            if password == user['password']:
                print("Login successful!")
                self.user_logged_in = user_id
            else:
                print("Incorrect password. Access denied.")
        else:
            print("User not found. Please register first.")

    def purchase(self):
        if self.user_logged_in:
            total_price = 0
            purchase_details = []
            while True:
                product_name = input("Enter product name to purchase (or 'done' to finish): ")
                if product_name.lower() == 'done':
                    break
                product = self.products_collection.find_one({"name": product_name})
                if product:
                    quantity = int(input("Enter quantity: "))
                    if quantity <= product['quantity']:
                        new_quantity = product['quantity'] - quantity
                        self.products_collection.update_one({"name": product_name}, {"$set": {"quantity": new_quantity}})
                        total_price += product['price'] * quantity
                        purchase_details.append({"product_name": product_name, "quantity": quantity})
                    else:
                        print("Not enough quantity available.")
                        self.notify_admin_low_stock(product_name)
                else:
                    print("Product not found.")

            if total_price > 0:
                self.sales_collection.insert_one({"user_id": self.user_logged_in, "purchase_details": purchase_details, "total_price": total_price})
                print(f"Total bill for user {self.user_logged_in}: ₹{total_price}")
        else:
            print("User not logged in. Please login first.")

    def register_user(self):
        user_id = input("Enter user ID or mobile number: ")
        if self.users_collection.find_one({"user_id": user_id}):
            print("User already exists.")
        else:
            password = input("Set password: ")
            self.users_collection.insert_one({"user_id": user_id, "password": password})
            print(f"User {user_id} registered successfully.")

    def low_stock_alert(self):
        threshold = 5  
        print("\nLow Stock Alert:")
        products = self.products_collection.find({"quantity": {"$lte": threshold}})
        for product in products:
            print(f"Product {product['name']} has low stock: Quantity = {product['quantity']}")

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
                    self.purchase()
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
