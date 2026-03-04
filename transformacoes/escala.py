import matplotlib.pyplot as plt

# Função de escala
def escala(pontos, Sx, Sy):
    pontos_escalados = []

    for x, y in pontos:
        x_novo = x * Sx
        y_novo = y * Sy
        pontos_escalados.append((x_novo, y_novo))

    return pontos_escalados

# Pontos originais
p1 = (2, 2)
p2 = (4, 4)

pontos_originais = [p1, p2]

# Fatores de escala
Sx = 2
Sy = 2

# Aplicando a escala
pontos_escalados = escala(pontos_originais, Sx, Sy)

# Pontos originais
x_orig = [p[0] for p in pontos_originais]
y_orig = [p[1] for p in pontos_originais]

# Pontos escalados
x_esc = [p[0] for p in pontos_escalados]
y_esc = [p[1] for p in pontos_escalados]

# Plotagem
plt.plot(x_orig, y_orig, 'bo-', label='Pontos originais')
plt.plot(x_esc, y_esc, 'ro-', label='Pontos escalados')

plt.xlim(-7, 10)
plt.ylim(-7, 10)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Escala de pontos no plano cartesiano')
plt.grid(True)
plt.legend()

plt.show()

# Impressão no terminal
print("Pontos escalados:")
for ponto in pontos_escalados:
    print(ponto)