from services.data_loader import load_dataset
from services.pricing_service import apply_discounts
from services.reporting_service import generate_report
from models.product import Product
from datetime import datetime
import pandas as pd

# Carregar o dataset
df = pd.read_csv('data/dairy_dataset.csv')

# Solicitar ao usuário a região desejada
region = input("Digite a região ou fazenda para análise (ex: Fazenda A): ")

df_filtered = df[df['Location'].str.lower() == region.lower()]

if df_filtered.empty:
    print(f"Nenhum produto encontrado para a região: {region}")
else:
    products = []
    
    print(f"\nProdutos encontrados para a região: {region}\n")
    print("ID | Nome | Validade | Preço Anterior | Estoque")
    print("-" * 60)
    
    for _, row in df_filtered.iterrows():
        product = Product(
            row['Product ID'], 
            row['Product Name'], 
            datetime.strptime(row['Expiration Date'], '%Y-%m-%d').date(), 
            row['Price per Unit'], 
            row['Quantity in Stock (liters/kg)']
        )
        
        # Calcular desconto com base na proximidade da validade
        days_to_expire = (product.expiration_date - datetime.now().date()).days
        
        if days_to_expire <= 2:
            discount_percent = 30
        elif days_to_expire <= 5:
            discount_percent = 10
        else:
            discount_percent = 0
        
        new_price = product.price * (1 - discount_percent / 100)
        
        # Exibir informações
        print(f"{product.id} | {product.name} | {product.expiration_date} | R${product.price:.2f} | {product.stock_quantity}")
        
        # Armazenar o produto com preço atualizado
        products.append({
            'id': product.id,
            'name': product.name,
            'old_price': product.price,
            'new_price': new_price,
            'discount_percent': discount_percent,
            'expiration_date': product.expiration_date,
            'stock_quantity': product.stock_quantity
        })
    
    print("\nResultados após a precificação dinâmica:\n")
    print("ID | Nome | Preço Anterior | Preço Novo | % Desconto")
    print("-" * 60)
    
    for p in products:
        print(f"{p['id']} | {p['name']} | R${p['old_price']:.2f} | R${p['new_price']:.2f} | {p['discount_percent']}%")

updated_products = apply_discounts(products)
generate_report(updated_products)