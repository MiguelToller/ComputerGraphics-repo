import matplotlib.pyplot as plt

# Função de translação
def translacao(pontos, Tx, Ty):
    pontos_transladados = []

    for x, y in pontos:
        x_novo = x + Tx
        y_novo = y + Ty
        pontos_transladados.append((x_novo, y_novo))

    return pontos_transladados

# Pontos originais
p1 = (6, 8)
p2 = (4, 5)
p3 = (8, 5)
pontos_originais = [p1, p2, p3]

# Vetor de translação
Tx, Ty = 3, -4

# Aplicando a translação
pontos_transladados = translacao(pontos_originais, Tx, Ty)

# Pontos originais
x_orig = [p[0] for p in pontos_originais]
y_orig = [p[1] for p in pontos_originais]

# Pontos transladados
x_trans = [p[0] for p in pontos_transladados]
y_trans = [p[1] for p in pontos_transladados]

# Fechar o triângulo
x_orig.append(x_orig[0])
y_orig.append(y_orig[0])

x_trans.append(x_trans[0])
y_trans.append(y_trans[0])

# Plotagem
plt.plot(x_orig, y_orig, 'bo-', label="Pontos originais")
plt.plot(x_trans, y_trans, 'ro-', label="Pontos transladados")

plt.xlim(0, 12)
plt.ylim(0, 10)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Translação de pontos no plano cartesiano')
plt.grid(True)
plt.legend()

plt.show()