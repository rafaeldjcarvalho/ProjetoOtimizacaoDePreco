from datetime import date

class PricingStrategy:
    
    @staticmethod
    def calculate_discount(expiration_date, current_price, reference_date=None):
        """
        Calcula o desconto baseado na data de vencimento do produto.

        :param expiration_date: Data de vencimento do produto (datetime.date)
        :param current_price: Preço original do produto (float)
        :param reference_date: Data de referência para cálculo do desconto (datetime.date)
        :return: Novo preço com desconto aplicado (float)
        """

        # Se nenhuma data de referência for fornecida, usamos a data atual
        if reference_date is None:
            reference_date = date.today()

        # Calcula a quantidade de dias até o vencimento
        days_to_expire = (expiration_date - reference_date).days

        # Define o desconto com base nos dias restantes
        if days_to_expire <= 2:
            discount = 0.30  # 30% de desconto
        elif days_to_expire <= 5:
            discount = 0.10  # 10% de desconto
        elif days_to_expire <= 10:
            discount = 0.05  # 5% de desconto
        else:
            discount = 0.0  # Sem desconto

        # Aplica o desconto no preço original e arredonda
        return round(current_price * (1 - discount), 2)
