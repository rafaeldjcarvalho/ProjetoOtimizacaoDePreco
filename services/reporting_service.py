import matplotlib.pyplot as plt

def generate_report(products):
    names = [product.name for product in products]
    prices = [product.price for product in products]
    
    plt.figure(figsize=(10, 6))
    plt.bar(names, prices)
    plt.xlabel('Produtos')
    plt.ylabel('Preço com Desconto')
    plt.title('Preços Ajustados para Produtos Próximos ao Vencimento')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('logs/pricing_report.png')
    plt.show()