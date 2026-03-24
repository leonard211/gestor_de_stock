notas = []

def adicionar_nota():
    nota = float(input("Digite uma nota (0 a 20): "))
    
    while nota < 0 or nota > 20:
        print("Nota inválida.")
        nota = float(input("Digite uma nota (0 a 20): "))
    
    notas.append(nota)
    print("Nota adicionada.")

def listar_notas():
    if len(notas) == 0:
        print("Ainda não há notas.")
    else:
        for n in notas:
            print(n)

def calcular_media():
    if len(notas) == 0:
        print("Não há notas.")
    else:
        soma = 0
        for n in notas:
            soma = soma + n
        media = soma / len(notas)
        print("Média:", round(media,2))

def mostrar_positivas():
    for n in notas:
        if n >= 10:
            print(n)

opcao = -1

while opcao != 0:
    print("\nMENU")
    print("1 - Adicionar nota")
    print("2 - Listar notas")
    print("3 - Calcular média")
    print("4 - Mostrar notas positivas")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        adicionar_nota()
    elif opcao == 2:
        listar_notas()
    elif opcao == 3:
        calcular_media()
    elif opcao == 4:
        mostrar_positivas()
    elif opcao == 0:
        print("Programa terminado.")
    else:
        print("Opção inválida.")