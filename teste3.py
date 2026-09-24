# Função para cadastrar as notas dos alunos
def inserir_notas():
    notas = []
    print("--- Cadastro de Notas ---")
    while True:
        try:
            nota = float(input("Digite a nota do aluno (ou valor negativo para encerrar): "))
            if nota < 0:
                break
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
    return notas

# Função para calcular a média das notas
def calcular_media(notas):
    if len(notas) == 0:
        return 0.0
    return sum(notas) / len(notas)