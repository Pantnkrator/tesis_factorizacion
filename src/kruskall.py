import scipy.stats as stats

# Tiempos de ejecución para cada algoritmo
times_A = [12.4, 11.8, 13.0, 12.7, 12.1]
times_B = [10.5, 11.0, 10.8, 10.9, 11.1]
times_C = [9.8, 9.9, 9.7, 10.0, 9.9]

# Realizar la prueba de Kruskal-Wallis
statistic, p_value = stats.kruskal(times_A, times_B, times_C)

print(f'Estadístico de Kruskal-Wallis: {statistic}')
print(f'Valor p: {p_value}')
