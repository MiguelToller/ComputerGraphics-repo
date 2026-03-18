import numpy as np

# Matriz de translação
Mt = np.array([
    [1, 0, 0, 5],
    [0, 1, 0, 2],
    [0, 0, 1, 3],
    [0, 0, 0, 1]
])

# Ponto original
P = np.array([
    [-2],
    [4],
    [1],
    [1]
])

# Multiplicação matriz x vetor
P_linha = np.dot(Mt, P)

# Impressão dos resultados
print("Matriz de Translação (Mt):")
print(Mt)

print("\nPonto Original (P):")
print(P)

print("\nPonto Transladado (P'):")
print(P_linha)