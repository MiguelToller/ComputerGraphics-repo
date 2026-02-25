
A = [
    [1, 3, 2],
    [4, 7, 6]
]

B = [
    [2, 8],
    [3, 1],
    [5, 9]
]

def multiplicar_matrizes(A, B):
    linhas_A = len(A)
    colunas_A = len(A[0])
    linhas_B = len(B)
    colunas_B = len(B[0])

    if colunas_A != linhas_B:
        return None

    resultado = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]

    for i in range(linhas_A):
        for j in range(colunas_B):
            soma = 0
            for k in range(colunas_A):
                soma += A[i][k] * B[k][j]
            resultado[i][j] = soma

    return resultado

def matriz_eh_diagonal(A):
    linhas = len(A)
    colunas = len(A[0])

    if linhas != colunas:
        return False

    for i in range(linhas):
        for j in range(colunas):
            if i != j and A[i][j] != 0:
                return False
    return True

def matriz_eh_identidade(A):
    linhas = len(A)
    colunas = len(A[0])

    if linhas != colunas:
        return False

    for i in range(linhas):
        for j in range(colunas):
            if (i == j and A[i][j] != 1) or (i != j and A[i][j] != 0):
                return False
    return True

def matriz_transposta(A):
    linhas = len(A)
    colunas = len(A[0])

    # Inicializa a matriz transposta com tamanho colunas x linhas
    transposta = [[0 for _ in range(linhas)] for _ in range(colunas)]

    for i in range(linhas):
        for j in range(colunas):
            transposta[j][i] = A[i][j]

    return transposta

def multiplicar_por_escalar(A, x):
    linhas = len(A)
    colunas = len(A[0])

    resultado = [[0 for _ in range(colunas)] for _ in range(linhas)]

    for i in range(linhas):
        for j in range(colunas):
            resultado[i][j] = A[i][j] * x

    return resultado

resultado = multiplicar_matrizes(A, B)

# Impressão das matrizes
print("Matriz A:")
for linha in A:
    print(linha)

print("\nMatriz B:")
for linha in B:
    print(linha)

# Resultado da multiplicação
if resultado:
    print("\nResultado de A x B:")
    for linha in resultado:
        print(linha)
else:
    print("\nNão é possível multiplicar as matrizes.")

# Verifica se B é diagonal
if matriz_eh_diagonal(B):
    print("\nA matriz B é diagonal!")
else:
    print("\nA matriz B NÃO é diagonal.")

# Verifica se B é identidade
if matriz_eh_identidade(B):
    print("\nA matriz B é identidade!")
else:
    print("\nA matriz B NÃO é identidade.")

# Cria e imprime a matriz transposta de A
transposta_A = matriz_transposta(A)
print("\nMatriz transposta de A:")
for linha in transposta_A:
    print(linha)

# Cria e imprime a matriz transposta de B
transposta_B = matriz_transposta(B)
print("\nMatriz transposta de B:")
for linha in transposta_B:
    print(linha)

# Multiplicação por escalar
x = 3
escalar_A = multiplicar_por_escalar(A, x)
print(f"\nMatriz A multiplicada pelo escalar {x}:")
for linha in escalar_A:
    print(linha)