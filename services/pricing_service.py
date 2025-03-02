from models.pricing_strategy import PricingStrategy

def apply_discounts(products):
    for product in products:
        new_price = PricingStrategy.calculate_discount(product.expiration_date, product.price)
        product.price = new_price
    return products