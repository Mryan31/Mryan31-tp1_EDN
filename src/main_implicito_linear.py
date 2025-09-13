# src/main_implicitos_linear.py

import numpy as np
import matplotlib.pyplot as plt
from metodos import euler_regressivo_linear, trapezio_linear

# --- 1. Definição do Problema (Seção 3.1) ---
# PVI: y' = te^{-t} - y, com y(0)=1 
def f_pvi2(t, y):
    return t * np.exp(-t) - y

# Solução analítica para o PVI acima
def y_analitico_pvi2(t):
    return t * np.exp(-t) + np.exp(-t)

# --- 2. Parâmetros da Simulação ---
t0 = 0.0
tf = 10.0
y0 = 1.0
h_valores = [0.2, 0.1, 0.05] # Valores de h solicitados [cite: 51]

print("--- Análise de Erro para Métodos Implícitos (Problema Linear) ---")
print(f"{'h':<10}{'Erro Euler Regressivo':<25}{'Erro Trapézio':<25}")
print("-" * 60)

# --- 3. Execução e Cálculo de Erros ---
# Dicionário para guardar os resultados para o plot
resultados_plot = {}

for h in h_valores:
    t_valores = np.arange(t0, tf + h, h)
    
    # Solução com Euler Regressivo
    y_euler_reg = euler_regressivo_linear(y0, t_valores)
    erro_euler_reg = np.abs(y_euler_reg[-1] - y_analitico_pvi2(tf))
    
    # Solução com Método do Trapézio
    y_trapezio = trapezio_linear(y0, t_valores)
    erro_trapezio = np.abs(y_trapezio[-1] - y_analitico_pvi2(tf))
    
    print(f"{h:<10.3f}{erro_euler_reg:<25.10f}{erro_trapezio:<25.10f}")
    
    # Guarda os resultados do menor h para plotar
    if h == min(h_valores):
        resultados_plot['t'] = t_valores
        resultados_plot['euler_reg'] = y_euler_reg
        resultados_plot['trapezio'] = y_trapezio

# --- 4. Visualização (para o menor h) ---
plt.figure(figsize=(12, 8))
t_plot = resultados_plot['t']
y_analitico_plot = y_analitico_pvi2(t_plot)

plt.plot(t_plot, resultados_plot['euler_reg'], 'o-', label='Euler Regressivo (h=0.05)')
plt.plot(t_plot, resultados_plot['trapezio'], 's-', label='Trapézio (h=0.05)')
plt.plot(t_plot, y_analitico_plot, 'k--', label='Solução Analítica')

plt.title('Métodos Implícitos vs. Solução Analítica (Problema Linear)')
plt.xlabel('Tempo (t)')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.savefig('plots/implicitos_linear.png')
plt.show()