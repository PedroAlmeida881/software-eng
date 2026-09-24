import matplotlib.pyplot as plt

class Produtos:
    def __init__(self, nome, preco, categoria, estoque):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.estoque = estoque

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Categoria: {self.categoria}, Estoque: {self.estoque}"

# Listas globais fora da classe (ou podes transformá-las em atributos de classe)
catalogo = []
categorias = []

def adicionar_produto(nome, preco, categoria, estoque):
    novo_produto = Produtos(nome, preco, categoria, estoque)
    catalogo.append(novo_produto)
    categorias.append(categoria)
    print(f"Produto {nome} adicionado ao catálogo.")

def listar_catalogo():
    print("\n----- Catálogo da MinhaLoja -----")
    for produto in catalogo:
        print(produto)  

adicionar_produto("Notebook", 3500.00, "Informática", 12)
adicionar_produto("Smartphone", 2200.00, "Informática", 18)
adicionar_produto("Cafeteira", 350.00, "Eletrodoméstico", 7)
adicionar_produto("Geladeira", 2900.00, "Eletrodoméstico", 4)
adicionar_produto("Fone Bluetooth", 180.00, "Acessorio", 30)

listar_catalogo()

categorias_unicas = list(set(categorias))
categorias_unicas.sort()

contagem = [categorias.count(cat) for cat in categorias_unicas]

plt.bar(categorias_unicas, contagem, color='royalblue')
plt.xlabel('Categorias')
plt.ylabel('Número de Produtos')
plt.title('MinhaLoja - Produtos por Categoria')