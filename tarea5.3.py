import numpy as np
import matplotlib.pyplot as plt

# Datos del ejercicio
velocidad = np.array([40, 60, 80, 100, 120, 140])
consumo = np.array([6.5, 5.8, 5.5, 5.7, 6.2, 7.0])

# Ajustes polinómicos
coef_lineal = np.polyfit(velocidad, consumo, 1)      # Lineal (grado 1)
coef_cuadratica = np.polyfit(velocidad, consumo, 2)  # Cuadrática (grado 2)
coef_cubica = np.polyfit(velocidad, consumo, 3)      # Cúbica (grado 3)

# Valores para graficar
x_vals = np.linspace(40, 140, 200)
y_lineal = np.polyval(coef_lineal, x_vals)
y_cuadratica = np.polyval(coef_cuadratica, x_vals)
y_cubica = np.polyval(coef_cubica, x_vals)

# Graficar los resultados
plt.figure(figsize=(8, 6))
plt.scatter(velocidad, consumo, color='red', label='Datos experimentales')
plt.plot(x_vals, y_lineal, '--', label='Ajuste Lineal', color='blue')
plt.plot(x_vals, y_cuadratica, '-.', label='Ajuste Cuadrático', color='green')
plt.plot(x_vals, y_cubica, label='Ajuste Cúbico', color='purple')
plt.xlabel('Velocidad (km/h)')
plt.ylabel('Consumo (L/100 km)')
plt.title('Ajustes Polinómicos: Lineal, Cuadrático y Cúbico - Consumo de Combustible')
plt.legend()
plt.grid()
plt.savefig('ajuste_polinomico_combustible.png', dpi=300)
plt.show()

# Mostrar las ecuaciones ajustadas en consola (opcional)
print("Ecuación lineal:", np.poly1d(coef_lineal))
print("\nEcuación cuadrática:", np.poly1d(coef_cuadratica))
print("\nEcuación cúbica:", np.poly1d(coef_cubica))
