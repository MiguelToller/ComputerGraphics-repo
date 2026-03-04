import numpy as np
import matplotlib.pyplot as plt

# Função de rotação
def rotacao(pontos, angulo):
    pontos_rotacionados = []

    angulo_rad = np.radians(angulo)  # Converter graus → radianos

    for x0, y0 in pontos:
        xu = round(x0 * np.cos(angulo_rad) - y0 * np.sin(angulo_rad), 2)
        yu = round(x0 * np.sin(angulo_rad) + y0 * np.cos(angulo_rad), 2)

        pontos_rotacionados.append((xu, yu))

    return pontos_rotacionados

# Pontos originais
p1 = (2, 2)
p2 = (4, 4)
pontos_originais = [p1, p2]

# Ângulo de rotação
angulo = 45

# Aplicando a rotação
pontos_rotacionados = rotacao(pontos_originais, angulo)

# Impressão no terminal
print("Pontos originais:")
for i, p in enumerate(pontos_originais, start=1):
    print(f"P{i}: {p}")

print("\nPontos rotacionados:")
for i, p in enumerate(pontos_rotacionados, start=1):
    print(f"P{i}: {p}")

# Preparando dados para o gráfico
x_orig = [p[0] for p in pontos_originais]
y_orig = [p[1] for p in pontos_originais]

x_rot = [p[0] for p in pontos_rotacionados]
y_rot = [p[1] for p in pontos_rotacionados]

# Plotagem
plt.plot(x_orig, y_orig, 'bo-', label='Pontos originais')
plt.plot(x_rot, y_rot, 'ro-', label='Pontos rotacionados')

# Rótulos dos pontos originais
for i, p in enumerate(pontos_originais, start=1):
    plt.text(p[0], p[1], f' P{i}', fontsize=12,
             verticalalignment='bottom',
             horizontalalignment='right')

# Rótulos dos pontos rotacionados
for i, p in enumerate(pontos_rotacionados, start=1):
    plt.text(p[0], p[1], f' P{i}', fontsize=12,
             verticalalignment='bottom',
             horizontalalignment='right')

# Configurações do gráfico
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Rotação de pontos no plano cartesiano')
plt.grid(True)
plt.legend()

plt.show()