import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import pandas as pd
from datetime import datetime
from models.pricing_strategy import PricingStrategy  # Importa a classe de precificação

# Carregar dataset
df = pd.read_csv('data/dairy_dataset.csv')

# Criar a janela principal
root = tk.Tk()
root.title("Otimização de Precificação de Lácteos")
root.geometry("900x500")

# Labels e campos de entrada
lbl_location = tk.Label(root, text="Localidade:")
lbl_location.grid(row=0, column=0, padx=10, pady=5)
cmb_location = ttk.Combobox(root, values=df['Location'].unique().tolist())
cmb_location.grid(row=0, column=1, padx=10, pady=5)

lbl_product = tk.Label(root, text="Produto:")
lbl_product.grid(row=0, column=2, padx=10, pady=5)
cmb_product = ttk.Combobox(root, values=df['Product Name'].unique().tolist())
cmb_product.grid(row=0, column=3, padx=10, pady=5)

lbl_date = tk.Label(root, text="Data de Referência:")
lbl_date.grid(row=0, column=4, padx=10, pady=5)
date_picker = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern="dd/MM/yyyy")
date_picker.grid(row=0, column=5, padx=10, pady=5)

# Tabela para exibir dados
columns = ("Product ID", "Product Name", "Price per Unit", "Quantity in Stock", "Expiration Date", "Desconto (%)", "Novo Preço")
tree = ttk.Treeview(root, columns=columns, show="headings", height=20)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.grid(row=1, column=0, columnspan=7, padx=10, pady=10)

# Função para aplicar filtro
def filter_data():
    location = cmb_location.get().strip()
    product = cmb_product.get().strip()
    selected_date = date_picker.get_date()  # Data escolhida pelo usuário (datetime.date)

    filtered_df = df.copy()

    # Aplicar filtros por localidade e produto
    if location:
        filtered_df = filtered_df[filtered_df['Location'] == location]
    if product:
        filtered_df = filtered_df[filtered_df['Product Name'] == product]

    # Limpar tabela antes de inserir novos dados
    tree.delete(*tree.get_children())

    # Iterar sobre os produtos filtrados
    for _, row in filtered_df.iterrows():
        expiration_date = datetime.strptime(row['Expiration Date'], '%Y-%m-%d').date()  # Converter string para date
        formatted_expiration_date = expiration_date.strftime('%d/%m/%Y')  # Formatar para dd/mm/yyyy
        current_price = row['Price per Unit']

        # Calcular desconto usando a classe PricingStrategy
        new_price = PricingStrategy.calculate_discount(expiration_date, current_price, selected_date)

        # Calcular porcentagem de desconto
        discount_percentage = round(((current_price - new_price) / current_price) * 100, 2)

        # Inserir os dados na tabela
        tree.insert("", tk.END, values=(
            row['Product ID'], row['Product Name'], row['Price per Unit'], 
            row['Quantity in Stock (liters/kg)'], formatted_expiration_date, discount_percentage, new_price
        ))

# Botão para aplicar filtros
tk.Button(root, text="Filtrar", command=filter_data).grid(row=0, column=6, padx=10, pady=5)

# Executar a interface
root.mainloop()
