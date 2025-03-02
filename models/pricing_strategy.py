from datetime import date

class PricingStrategy:
    @staticmethod
    def calculate_discount(expiration_date, current_price):
        days_to_expire = (expiration_date - date.today()).days
        
        if days_to_expire <= 2:
            discount = 0.30
        elif days_to_expire <= 5:
            discount = 0.10
        else:
            discount = 0.0

        return round(current_price * (1 - discount), 2)