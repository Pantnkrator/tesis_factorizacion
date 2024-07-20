import numpy as np
import scipy.stats as stats

# Datos de ejemplo: tiempos de ejecución para cada caso de prueba y algoritmo
# algoritmo_a = np.array([2.1, 2.2, 2.0, 2.3, 2.5, 2.1, 2.4, 2.2, 2.3, 2.4, 2.5, 2.2, 2.3])
# algoritmo_b = np.array([2.3, 2.4, 2.2, 2.5, 2.6, 2.3, 2.5, 2.3, 2.4, 2.5, 2.6, 2.3, 2.5])
# algoritmo_c = np.array([2.5, 2.6, 2.4, 2.7, 2.8, 2.5, 2.6, 2.5, 2.6, 2.7, 2.8, 2.5, 2.6])
# algoritmo_d = np.array([2.0, 2.1, 1.9, 2.2, 2.3, 2.0, 2.2, 2.1, 2.2, 2.3, 2.4, 2.1, 2.2])

algoritmo_a = np.array([0.437, 1.394, 6.293, 21.026, 39.504, 64.788, 109.328, 339.266, 3414.5, 15096.03, 81195.058, 43553.943])
algoritmo_b = np.array([0.009, 0.03, 0.036, 0.003, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002])
algoritmo_c = np.array([0.213, 0.235, 0.28, 2.49, 1.729, 1.384, 1.494, 0.481, 15.424, 14.593, 62.654, 11.13])
algoritmo_d = np.array([69.424, 70.688, 70.603, 74.497, 57.068, 90.008, 82.297, 69.058, 68.385, 103.500, 84.799, 88.860])

# Función para realizar pruebas t pareadas y mostrar resultados
def realizar_pruebas_t(algoritmo1, algoritmo2, nombre1, nombre2):
    t_stat, p_value = stats.ttest_rel(algoritmo1, algoritmo2)
    print(f'Comparación entre {nombre1} y {nombre2}')
    print(f'Estadístico t: {t_stat:.4f}')
    print(f'Valor p: {p_value:.4f}')
    if p_value < 0.05:
        print("Rechazamos la hipótesis nula: hay una diferencia significativa entre los algoritmos.\n")
    else:
        print("No se rechaza la hipótesis nula: no hay una diferencia significativa entre los algoritmos.\n")

# Comparaciones entre algoritmos
realizar_pruebas_t(algoritmo_a, algoritmo_b, 'Divisiones Sucesivas', 'Algoritmo de Fermat')
realizar_pruebas_t(algoritmo_a, algoritmo_c, 'Divisiones Sucesivas', 'Algoritmo Pollard-Rho')
realizar_pruebas_t(algoritmo_a, algoritmo_d, 'Divisiones Sucesivas', 'Criba Cuadratica')
realizar_pruebas_t(algoritmo_b, algoritmo_c, 'Algoritmo de Fermat', 'Algoritmo Pollard-Rho')
realizar_pruebas_t(algoritmo_b, algoritmo_d, 'Algoritmo de Fermat', 'Criba Cuadratica')
realizar_pruebas_t(algoritmo_c, algoritmo_d, 'Algoritmo Pollard-Rho', 'Criba Cuadratica')
