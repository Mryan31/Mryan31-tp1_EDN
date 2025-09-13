# src/main_implicitos_naolinear.py

import numpy as np
import matplotlib.pyplot as plt
from metodos import euler_regressivo_naolinear_bhaskara

# --- 1. Definição do Problema (Seção 3.2) ---
# PVI: y' = -y^2, com y(1)=1 [cite: 55]
def f_pvi3(t, y):
    return -y**2

# Solução analítica para o PVI acima
def y_analitico_pvi3(t):
    return 1.0 / t

# --- 2. Parâmetros da Simulação ---
t0 = 1.0
tf = 10.0
h = 0.1
y0 = 1.0

# --- 3. Execução do Método ---
t_valores = np.arange(t0, tf + h, h)
y_numerico = euler_regressivo_naolinear_bhaskara(y0, t_valores)
y_analitico = y_analitico_pvi3(t_valores)

# --- 4. Visualização ---
plt.figure(figsize=(12, 8))
plt.plot(t_valores, y_numerico, 'o-', label='Euler Regressivo Não-Linear')
plt.plot(t_valores, y_analitico, 'k--', label='Solução Analítica (y=1/t)')

plt.title('Método Implícito para PVI Não-Linear')
plt.xlabel('Tempo (t)')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.savefig('plots/implicitos_naolinear.png')
plt.show()