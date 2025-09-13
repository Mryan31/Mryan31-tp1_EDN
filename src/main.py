import numpy as np
import matplotlib.pyplot as plt
from metodos import euler, heun, ponto_medio

#Definindo a estrutura do problema
def f(t, y):
    return -y + 2 * np.cos(t)

#Escolhendo os parâmetros para a simulação
t0 = 0.0 #Tempo inicial
tf = 10.0 #Tempo Final
h = 0.1 #Tamanho do parâmetro inicial para derivação/integração
y0 = 1.0 #Condição inicial y(t0) = y0

#Agora vamos criar o "eixo x" do nosso gráfico com a seguinte chamada
t_valores = np.arange(t0, tf + h, h)

#Loop de Euler
y_valores_euler = euler(f, y0, t_valores)
y_valores_heun = heun(f, y0, t_valores)
y_valores_ponto_medio = ponto_medio(f, y0, t_valores)

#Solução Analítica (para comparação) ---
y_analitico = np.cos(t_valores) + np.sin(t_valores)

#Por fim vamos ver os resultados
plt.figure(figsize=(12, 8))
plt.plot(t_valores, y_valores_euler, 'o-', label='Euler (Ordem 1)')
plt.plot(t_valores, y_valores_heun, 's-', label='Heun (Ordem 2)')
plt.plot(t_valores, y_valores_ponto_medio, '^-', label='Ponto Médio (Ordem 2)')
plt.plot(t_valores, y_analitico, 'k--', label='Solução Analítica')
plt.title('Comparação de Métodos Numéricos')
plt.xlabel('Tempo (t)')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.savefig('plots/comparacao_metodos.png')
plt.show()

print("Simulação concluída! Gráfico salvo em 'plots/euler_vs_analitica.png'")