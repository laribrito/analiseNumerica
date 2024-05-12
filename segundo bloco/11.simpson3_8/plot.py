import math
import numpy as np
import matplotlib.pyplot as plt

def calcular_f_x(x):
    return (1 / (0.005 * (2 * math.pi) ** (1 / 2))) * math.e ** (-0.5 * ((x - 4.991) / 0.005) ** 2)

# Valores de x
x_valores = np.linspace(4.5, 5.5, 100)  # Intervalo de valores de x

# Calcular f(x) para cada valor de x
fx_valores = [calcular_f_x(x) for x in x_valores]

# Plotar a função
plt.plot(x_valores, fx_valores, label='$f(x) = \\frac{1}{0.005 \\cdot (2\\pi)^{\\frac{1}{2}}} \\cdot e^{-\\frac{1}{2}\\left(\\frac{x - 4.991}{0.005}\\right)^2}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da função f(x)')
plt.legend()
plt.grid(True)

# Salvar a figura em um arquivo
plt.savefig('grafico_funcao_f_x.png')

# Exibir uma mensagem indicando que a figura foi salva
print("Gráfico salvo como 'grafico_funcao_f_x.png'")
