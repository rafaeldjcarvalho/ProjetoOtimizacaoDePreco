# Otimização de Precificação de Lácteos

Este projeto realiza a análise e otimização de preços para produtos lácteos, considerando a data de validade e aplicando descontos dinâmicos conforme a proximidade do vencimento. Agora, há duas formas de executar o sistema: por meio de uma interface gráfica ou pela execução tradicional com geração de gráficos.

## 📌 Funcionalidades
- **Interface Gráfica (`gui.py`)**: Permite filtrar os produtos por localidade, nome e data, exibindo os preços ajustados dinamicamente.
- **Execução Tradicional (`main.py`)**: Processa os dados e gera gráficos de precificação.

## 📥 Instalação
### **1. Clonar o repositório**
```sh
git clone https://github.com/seu-repositorio.git
cd seu-repositorio
```
### **2. Instalar as dependências**
```sh
pip install -r requirements.txt
```

## 🚀 Como Executar
### **1. Modo Interface Gráfica** (Recomendado)
```sh
python gui.py
```
- Um painel será aberto, permitindo selecionar localidade, produto e data.
- Os preços ajustados serão exibidos em uma tabela dinâmica.

### **2. Modo Tradicional (Gerar Gráficos)**
```sh
python main.py
```
- O script processará os dados e exibirá gráficos de precificação.

## 📊 Lógica de Precificação
A classe `PricingStrategy` calcula descontos baseados na proximidade da data de vencimento:
- **≤ 2 dias** para expirar → **30% de desconto**
- **≤ 5 dias** para expirar → **10% de desconto**
- **≤ 10 dias** para expirar → **5% de desconto**
- **> 10 dias** para expirar → **Sem desconto**

## 📌 Estrutura do Projeto
```
├── data/
│   ├── dairy_dataset.csv  # Dataset de produtos lácteos
├── models/
│   ├── product.py         # Modelo de produto
│   ├── pricing_strategy.py  # Estratégia de precificação
├── services/
│   ├── pricing_service.py # Serviço de cálculo de preço
├── gui.py                 # Interface gráfica (Tkinter)
├── main.py                # Execução tradicional com gráficos
├── requirements.txt       # Dependências do projeto
├── README.md              # Documentação
```

## 🛠 Tecnologias Utilizadas
- **Python 3.9+**
- **Tkinter** (Interface Gráfica)
- **Pandas** (Manipulação de dados)
- **Matplotlib** (Geração de gráficos)

## 📬 Contato
Para dúvidas ou sugestões, entre em contato pelo GitHub.

---
Agora você pode escolher entre visualizar os dados pela interface gráfica ou gerar gráficos com `main.py`. 🚀
