import sympy as sp

# Definir a variável simbólica
x = sp.symbols('x')

# Definir a expressão da função exponencial
expr = sp.exp(-20000.0*x**2 + 199640.0*x - 498201.62)

# Calcular o valor numérico da integral definida
integral = sp.integrate(expr, (x, 4.991, 5.018)).evalf()

# Exibir o resultado
print("Resultado da integral:", integral)
