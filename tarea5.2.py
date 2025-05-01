import numpy as np
import matplotlib.pyplot as plt

# Datos del ejercicio
distancia = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
temperatura = np.array([250, 220, 180, 150, 130, 125])

# Ajustes polinómicos
coef_lineal = np.polyfit(distancia, temperatura, 1)      # Lineal (grado 1)
coef_cuadratica = np.polyfit(distancia, temperatura, 2)  # Cuadrática (grado 2)
coef_cubica = np.polyfit(distancia, temperatura, 3)      # Cúbica (grado 3)

# Valores para graficar
x_vals = np.linspace(0, 5, 200)
y_lineal = np.polyval(coef_lineal, x_vals)
y_cuadratica = np.polyval(coef_cuadratica, x_vals)
y_cubica = np.polyval(coef_cubica, x_vals)

# Graficar los resultados
plt.figure(figsize=(8, 6))
plt.scatter(distancia, temperatura, color='red', label='Datos experimentales')
plt.plot(x_vals, y_lineal, '--', label='Ajuste Lineal', color='blue')
plt.plot(x_vals, y_cuadratica, '-.', label='Ajuste Cuadrático', color='green')
plt.plot(x_vals, y_cubica, label='Ajuste Cúbico', color='purple')
plt.xlabel('Distancia (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Ajustes Polinómicos: Lineal, Cuadrático y Cúbico - Temperatura en un Motor')
plt.legend()
plt.grid()
plt.savefig('ajuste_polinomico_motor.png', dpi=300)
plt.show()

# Mostrar las ecuaciones ajustadas en consola (opcional)
print("Ecuación lineal:", np.poly1d(coef_lineal))
print("\nEcuación cuadrática:", np.poly1d(coef_cuadratica))
print("\nEcuación cúbica:", np.poly1d(coef_cubica))
