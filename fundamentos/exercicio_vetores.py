import math

def add_vetor():
    # Leitura dos valores do vetor
    x = float(input("Digite o valor de x: "))
    y = float(input("Digite o valor de y: "))
    z = float(input("Digite o valor de z: "))

    # Armazenando o vetor
    vetor = [x, y, z]
    print(f"Vetor adicionado... ({vetor[0]}, {vetor[1]}, {vetor[2]})")
    return vetor

def calcular_tamanho(vetor):
    tam = math.sqrt(vetor[0]**2 + vetor[1]**2 + vetor[2]**2)
    return round(tam)

def normalizar_vetor(vetor):
    tam = calcular_tamanho(vetor)
    vetor_normalizado = [
        vetor[0]/tam,
        vetor[1]/tam,
        vetor[2]/tam
    ]
    return vetor_normalizado

def adicionar_vetor(v1, v2):
    return [
        v1[0] + v2[0],
        v1[1] + v2[1],
        v1[2] + v2[2]   
    ]

def subtrair_vetor(v1, v2):
    return [
        v1[0] - v2[0],
        v1[1] - v2[1],
        v1[2] - v2[2]   
    ]

def multiplicar_escalar(vetor, escalar):
    return [vetor[0]*escalar, vetor[1]*escalar, vetor[2]*escalar]

def dividir_escalar(vetor, escalar):
    if escalar == 0:
        print("Erro: Proibido dividir por 0!")
        return None
    return [vetor[0]/escalar, vetor[1]/escalar, vetor[2]/escalar]

def produto_escalar(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

vetor = add_vetor()

while True:
    print("\n1. Calcular o tamanho do vetor")
    print("2. Normalizar o vetor")
    print("3. Adicionar outro vetor")
    print("4. Subtrair outro vetor")
    print("5. Multiplicar por escalar")
    print("6. Dividir por escalar")
    print("7. Produto escalar")
    print("8. Sair")

    op = int(input("Digite a opção desejada: "))

    if op == 1:
        if vetor is None:
            print("\nNenhum vetor cadastrado!")
        else:
            print(f"\nTamanho do vetor: {calcular_tamanho(vetor)}")

    elif op == 2:
        if vetor is None:
            print("\nNenhum vetor cadastrado!")
        else:
            vetor_normalizado = normalizar_vetor(vetor)
            print(f"\nVetor normalizado: ({vetor_normalizado[0]}, {vetor_normalizado[1]}, {vetor_normalizado[2]})")

    elif op == 3:
        if vetor is None:
            print("\nNenhum vetor cadastrado!")
        else:
            print("\nDigite o segundo vetor para adicionar:")
            vetor2 = add_vetor()
            resultado = adicionar_vetor(vetor, vetor2)
            print(f"Resultado: ({resultado[0]}, {resultado[1]}, {resultado[2]})")

    elif op == 4:
        if vetor is None:
            print("\nNenhum vetor cadastrado!")
        else:
            print("\nDigite o segundo vetor para subtrair:")
            vetor2 = add_vetor()
            resultado = subtrair_vetor(vetor, vetor2)
            print(f"Resultado: ({resultado[0]}, {resultado[1]}, {resultado[2]})")

    elif op == 5:
        if vetor is None:
            print("\nNenhum vetor cadastrado!")
        else:
            escalar = float(input("Digite o valor do escalar: "))
            resultado = multiplicar_escalar(vetor, escalar)
            print(f"\nResultado: ({resultado[0]}, {resultado[1]}, {resultado[2]})")

    elif op == 6:
        if vetor is None:
            print("\nNenhum vetor cadastrado!")
        else:
            escalar = float(input("Digite o valor do escalar: "))
            resultado = dividir_escalar(vetor, escalar)
            if resultado is not None:
                print(f"\nResultado: ({resultado[0]}, {resultado[1]}, {resultado[2]})")

    elif op == 7:
        if vetor is None:
            print("\nNenhum vetor cadastrado!")
        else:
            print("\nDigite o segundo vetor para o produto escalar:")
            vetor2 = add_vetor()
            resultado = produto_escalar(vetor, vetor2)
            print(f"\nResultado do produto escalar: {resultado}")
    
    else:
        print("\nEncerrando o programa...")
        break