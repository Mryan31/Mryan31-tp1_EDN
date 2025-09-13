import numpy as np
import matplotlib.pyplot as plt
from metodos import euler, heun, rk4 # Importe também o rk4

# --- Definições do Problema (Seção 2) ---
def f_pvi1(t, y):
    return -y + 2 * np.cos(t)

def y_analitico_pvi1(t):
    return np.cos(t) + np.sin(t)

t0 = 0.0
tf = 10.0
y0 = 1.0

# --- Análise de Ordem ---
h_valores = np.array([0.2, 0.1, 0.05, 0.025, 0.0125])
erros_euler = []
erros_heun = []
erros_rk4 = []

for h in h_valores:
    t_valores = np.arange(t0, tf + h, h)
    
    # Calcular solução com Euler
    y_euler = euler(f_pvi1, y0, t_valores)
    erros_euler.append(np.abs(y_euler[-1] - y_analitico_pvi1(tf)))
    
    # Calcular solução com Heun
    y_heun = heun(f_pvi1, y0, t_valores)
    erros_heun.append(np.abs(y_heun[-1] - y_analitico_pvi1(tf)))
    
    # Calcular solução com RK4
    y_rk4 = rk4(f_pvi1, y0, t_valores)
    erros_rk4.append(np.abs(y_rk4[-1] - y_analitico_pvi1(tf)))

# --- Visualização da Análise de Ordem ---
plt.figure(figsize=(10, 6))
plt.loglog(h_valores, erros_euler, 's-', label='Erro Euler (Ordem 1)')
plt.loglog(h_valores, erros_heun, 'o-', label='Erro Heun (Ordem 2)')
plt.loglog(h_valores, erros_rk4, '^-', label='Erro RK4 (Ordem 4)')

# Linhas de referência para as inclinações teóricas
plt.loglog(h_valores, h_valores**1, 'k--', alpha=0.5, label='Referência Ordem 1 (h¹)')
plt.loglog(h_valores, h_valores**2, 'k:', alpha=0.5, label='Referência Ordem 2 (h²)')
plt.loglog(h_valores, h_valores**4, 'k-.', alpha=0.5, label='Referência Ordem 4 (h⁴)')

plt.title('Análise da Ordem Numérica dos Métodos')
plt.xlabel('Tamanho do Passo (h)')
plt.ylabel('Erro de Truncamento Global em t=10')
plt.gca().invert_xaxis()
plt.legend()
plt.grid(True)
plt.savefig('plots/analise_ordem_final.png')
plt.show()