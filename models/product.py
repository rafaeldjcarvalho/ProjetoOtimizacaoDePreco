
class Product:
    def __init__(self, id, name, expiration_date, price, stock_quantity):
        self.id = id
        self.name = name
        self.expiration_date = expiration_date
        self.price = price
        self.stock_quantity = stock_quantity

    def __repr__(self):
        return f"{self.name} - {self.price} (Validade: {self.expiration_date})"