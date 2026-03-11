class Product:

    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def display_product(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)
        print()


class Cart:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product.name, "added to cart")

    def view_cart(self):
        print("\nItems in Cart")
        if not self.products:
            print("Cart is empty")
        else:
            for p in self.products:
                print(p.name)


def calculate_final_price(price, category):

    if category.lower() == "electronics":
        gst = 0.18
    elif category.lower() == "clothing":
        gst = 0.05
    elif category.lower() == "books":
        gst = 0
    else:
        gst = 0

    final_price = price + (price * gst)
    return final_price


def calculate_cart_total(cart):

    total = 0

    for product in cart.products:
        final_price = calculate_final_price(product.price, product.category)
        total += final_price

    return total


# Predefined Products
p1 = Product(101, "Laptop", 50000, "Electronics")
p2 = Product(102, "Mobile", 20000, "Electronics")
p3 = Product(103, "Shirt", 1500, "Clothing")
p4 = Product(104, "Book", 500, "Books")

products = [p1, p2, p3, p4]

cart = Cart()


while True:

    print("\n1 View Products")
    print("2 Add Product to Cart")
    print("3 View Cart")
    print("4 Calculate Cart Total")
    print("5 Exit")

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            print("\nAvailable Products")
            for p in products:
                print(p.product_id, p.name, p.price)

        case 2:
            pid = int(input("Enter Product ID: "))
            found = False

            for p in products:
                if p.product_id == pid:
                    cart.add_product(p)
                    found = True
                    break

            if not found:
                print("Product not found")

        case 3:
            cart.view_cart()

        case 4:
            total = calculate_cart_total(cart)
            print("\nTotal Cart Value:", total)

        case 5:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice")