## README.md
```markdown
# Sistema de Otimização de Precificação para Produtos Lácteos Próximos ao Vencimento

## Descrição
Este projeto automatiza a gestão de preços de produtos lácteos perecíveis, aplicando descontos progressivos com base na proximidade do vencimento. A ferramenta visa reduzir o desperdício e otimizar a margem de lucro.

## Tecnologias
- **Backend:** Python, Flask/FastAPI
- **Banco de Dados:** MySQL (via SQLAlchemy)
- **Bibliotecas:** Pandas, Matplotlib, SQLAlchemy, SciPy/PuLP

## Como Executar
1. Instale as dependências:
```
pip install -r requirements.txt
```

2. Configure o banco MySQL.

3. Adicione o arquivo `dairy_dataset.csv` à pasta `data/`.

4. Execute o sistema:
```
python main.py
```

O sistema processará os dados, aplicará os descontos e gerará um gráfico com os preços ajustados!
```