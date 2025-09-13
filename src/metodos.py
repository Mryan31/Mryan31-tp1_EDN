import numpy as np

def euler (f, y0, t_valores):
    """
    O Método de Euler recebe como argumentos:
        f (função) : A função de uma EDO f(t, y)
        y0 (float) : Condição inicial f(y0)
        t_valores (np.array) : O array de pontos no tempo onde a solução será calculada.

    Retorna:
        np.array: O array com os valores da solução y(t).
    """
    y_valores = np.zeros_like(t_valores)
    y_valores[0] = y0
    
    h = t_valores[1] - t_valores[0]
    
    for i in range(len(t_valores) - 1):
        y_valores[i+1] = y_valores[i] + h * f(t_valores[i], y_valores[i])
    
    return y_valores

def heun(f, y0, t_valores):
    """
    Calcula a solução de uma EDO usando o método de Heun (RK2).
    Recebe como argumentos:
        f (função) : A função de uma EDO f(t, y)
        y0 (float) : Condição inicial f(y0)
        t_valores (np.array) : O array de pontos no tempo onde a solução será calculada.

    Retorna:
        np.array: O array com os valores da solução y(t).
    """
    y_valores = np.zeros_like(t_valores)
    y_valores[0] = y0
    h = t_valores[1] - t_valores[0]
    
    for i in range(len(t_valores) - 1):
        k1 = f(t_valores[i], y_valores[i])
        k2 = f(t_valores[i] + h, y_valores[i] + h * k1)
        y_valores[i + 1] = y_valores[i] + (h / 2.0) * (k1 + k2)
        
    return y_valores
    
def ponto_medio (f, y0, t_valores):
    """
    Calcula a solução de uma EDO usando o método do Ponto Médio (RK2).
    Recebe como argumentos:
        f (função) : A função de uma EDO f(t, y)
        y0 (float) : Condição inicial f(y0)
        t_valores (np.array) : O array de pontos no tempo onde a solução será calculada.

    Retorna:
        np.array: O array com os valores da solução y(t).
    """
    y_valores = np.zeros_like(t_valores)
    y_valores[0] = y0
    h = t_valores[1] - t_valores[0]

    for i in range(len(t_valores) - 1):
        k1 = f(t_valores[i], y_valores[i])
        k2 = f(t_valores[i] + h / 2.0, y_valores[i] + (h / 2.0) * k1)
        y_valores[i+1] = y_valores[i] + h * k2
        
    return y_valores

def rk4(f, y0, t_valores):
    """
    Calcula a solução de uma EDO usando o Método de Runge-Kutta de $a ordem
    """
    
    y_valores = np.zeros_like(t_valores)
    y_valores[0] = y0
    h = t_valores[1] - t_valores[0]
    
    for i in range(len(t_valores)- 1):
        k1 = f(t_valores[i], y_valores[i])
        k2 = f(t_valores[i] + h / 2.0, y_valores[i] + (h / 2.0) * k1)
        k3 = f(t_valores[i] + h / 2.0, y_valores[i] + (h / 2.0) * k2)
        k4 = f(t_valores[i] + h, y_valores[i] + h * k3)
        
        y_valores[i + 1] = y_valores[i] + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    
    return y_valores

def euler_regressivo_linear (y0, t_valores):
    """
    Soluciona o PVI linear y' = te^{-t} - y usando o método de Euler Regressivo.
    A solução para y_{i+1} já foi isolada algebricamente.
    """
    
    y_valores = np.zeros_like(t_valores)
    y_valores[0] = y0
    h = t_valores[1] - t_valores[0]

    for i in range(len(t_valores)- 1):
        #Vou usar a fórmula com o y_i já isolado
        numerador = y_valores[i] + h * t_valores[i + 1] * np.exp(- t_valores[i + 1])
        denominador = h + 1
        y_valores[i + 1] = numerador / denominador
    
    return y_valores

def trapezio_linear(y0, t_valores):
    """
    Soluciona o PVI linear y' = te^{-t} - y usando o método do Trapézio.
    A solução para y_{i+1} já foi isolada algebricamente.
    """
    
    y_valores = np.zeros_like(t_valores)
    y_valores[0] = y0
    h = t_valores[1] - t_valores[0]
    
    for i in range(len(t_valores)- 1):
        #Fórmula com o y_i já isolado
        termo_y = y_valores[i] * (1 - h / 2.0)
        termo_t = (h / 2.0) * (t_valores[i] * np.exp(-t_valores[i]) + t_valores[i + 1] * np.exp(-t_valores[i + 1]))
        numerador = termo_y + termo_t
        denominador = 1 + h / 2.0
        y_valores[i + 1] = numerador / denominador
        
    return y_valores

# Adicionar ao final de src/methods.py

def euler_regressivo_naolinear_bhaskara(y0, t_valores):
    """
    Soluciona o PVI não-linear y' = -y^2 usando o método de Euler Regressivo.
    A equação quadrática resultante é resolvida a cada passo usando Bhaskara.
    """
    y_valores = np.zeros_like(t_valores)
    y_valores[0] = y0
    h = t_valores[1] - t_valores[0]
    
    for i in range(len(t_valores) - 1):
        # Resolve a equação h*y^2 + y - y_i = 0 para y_{i+1}
        a = h
        b = 1
        c = -y_valores[i]
        
        # Discriminante
        delta = b**2 - 4*a*c
        
        # Bhaskara, pegando a raiz positiva para manter a continuidade da solução
        y_valores[i+1] = (-b + np.sqrt(delta)) / (2*a)
        
    return y_valores