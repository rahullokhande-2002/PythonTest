class Product:
    def display_product(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Category: {self.category}"


a = Product()
store = a.display_product(1, "Mobile", 20000, "Electronic")
print(store)


class Cart:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product, "added to cart")

    def view_cart(self):
        print("Items in Cart:")
        for item in self.products:
            print(item)


# Creating cart object
c = Cart()

# Adding products
c.add_product("Laptop")
c.add_product("Mouse")
c.add_product("Keyboard")

# View cart
c.view_cart()