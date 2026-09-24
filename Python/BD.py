# Importação das bibliotecas necessárias
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================================================================
# PASSO 1: Conectar ao banco de dados SQLite e criar a tabela
# ==============================================================================
conexao = sqlite3.connect('dados_vendas.db')

# Cria o cursor para executar comandos SQL
cursor = conexao.cursor()

# Cria a tabela 'vendas1' com os campos especificados no roteiro
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')

# Insere os dados de exemplo fornecidos na atividade
cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
''')

# Confirma (salva) as alterações no banco de dados
conexao.commit()


# ==============================================================================
# PASSO 2: Explorar e preparar os dados com Pandas
# ==============================================================================
# Carrega os dados da tabela SQL diretamente para um DataFrame do Pandas
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

print("--- EXIBIÇÃO INICIAL DOS DADOS (PRIMEIRAS LINHAS) ---")
print(df_vendas.head())
print("\n")


# ==============================================================================
# PASSO 3: Análise dos dados (Insights e Agrupamentos)
# ==============================================================================
print("--- RESUMO ESTATÍSTICO DOS DADOS DE VENDAS ---")
print(df_vendas.describe())
print("\n")

# Agrupa os dados por categoria para somar o faturamento de cada uma
vendas_por_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().reset_index()
print("--- FATURAMENTO TOTAL POR CATEGORIA ---")
print(vendas_por_categoria)
print("\n")


# ==============================================================================
# PASSO 4: Visualização dos dados com Matplotlib e Seaborn
# ==============================================================================
sns.set_theme(style="whitegrid")

# Configura o tamanho da figura do gráfico
plt.figure(figsize=(10, 6))

# Cria um gráfico de barras (barplot) relacionando a categoria com o valor total de vendas
sns.barplot(data=vendas_por_categoria, x='categoria', y='valor_venda', palette='Blues_d')

# Adiciona títulos e rótulos aos eixos
plt.title('Faturamento Total por Categoria de Produtos', fontsize=14, fontweight='bold')
plt.xlabel('Categoria', fontsize=12, fontweight='bold')
plt.ylabel('Valor Total de Vendas (R$)', fontsize=12, fontweight='bold')

# Ajusta o layout para melhor visualização
plt.tight_layout()

# Exibe o gráfico gerado
plt.show()


# ==============================================================================
# PASSO 5: Conclusão e fechamento da conexão
# ==============================================================================
# Fecha a conexão com o banco de dados SQLite para liberar recursos
conexao.close()