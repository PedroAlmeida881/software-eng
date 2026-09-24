def calcular_desconto(valor, percentual): 
    if percentual < 0 or percentual > 100:
        return None 
    desconto = valor * (percentual / 100)
    return valor - desconto

def registrar_venda(produto, valor_final):
    print(f"Venda registrada: Produto: {produto}, Valor final: R${valor_final:.2f}")

arrendondar = lambda x: round(x, 2)

total_vendas = 0    
qtd_vendas = 0

while True:
    print('\n----- minha loja - pvd -----')
    print('1 - Registrar venda')
    print('2 - Ver relatorio do dia')
    print('3 - Encerrar Caixa')

    opcao = input('Escolha uma opcao: ')

    if opcao == '3':
        print('Encerrando o caixa. Até amanhã!')
        break

    elif opcao == '1':
        produto = input("Digite o nome do produto: ")
        valor = float(input("Digite o valor do produto: R$"))
        percentual = float(input("Desconto (%): "))
        valor_final = calcular_desconto(valor, percentual)

        if valor_final is None:
            print("Percentual de desconto inválido. Tente novamente.")
        else:
            valor_final = arrendondar(valor_final)
            registrar_venda(produto, valor_final)       
            total_vendas = total_vendas + valor_final
            qtd_vendas = qtd_vendas + 1

    elif opcao == '2':
        print(f'\nVendas Hoje: {qtd_vendas}')
        print(f'Total faturado: R$ {arrendondar(total_vendas):.2f}')

    else: 
        print("Opção inválida. Tente novamente.")

import matplotlib.pyplot as plt

class Produtos:
    def _init_(self, nome, preco, categoria, estoque):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.estoque = estoque

    def __str__(self):
        return (f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Categoria: {self.categoria}, Estoque: {self.estoque}")


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
    