"""
Ejercicio: "Concurso de Aguacates Gigantes"
Un grupo de agricultores está ahora compitiendo para ver quién tiene los aguacates más pesados.
Esta vez, además de analizar los datos básicos (media, mediana, moda, desviación estándar), necesitarán también:
Tu misión:

1. Calcular:
• Media (promedio) del peso.
• Mediana.
• Moda.
• Desviación estándar.
• Coeficiente de variación (desviación estándar / media * 100) → Para ver qué tan homogéneo es el cultivo.

2. Identificar:
• El aguacate más pesado y el más ligero.
• Cuántos aguacates están dentro de un rango "ideal" de peso (por ejemplo, entre 400g y 600g).
3. Visualizar:
• Un histograma de distribución de pesos.
• Una gráfica de caja ("boxplot") para visualizar los valores atípicos (outliers).

4. Interactividad:
• Permitir al usuario definir el rango ideal (no fijo como 400-600g).
• Permitir ingresar datos manualmente o usar un conjunto de datos precargados.
"""
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt

# 1. Datos precargados (pesos en gramos de aguacates gigantes)
aguacates_default = [
    420, 510, 390, 680, 450, 530, 480, 510, 
    720, 380, 490, 510, 600, 440, 850, 460
]

print("=== CONCURSO DE AGUACATES GIGANTES ===")

# 2. Selección de origen de datos (Punto 4)
opcion = input("¿Deseas ingresar datos manualmente? (s/n, por defecto 'n'): ").strip().lower()

if opcion == "s":
    entrada_datos = input("Ingresa los pesos en gramos separados por comas: ").strip()
    try:
        aguacates = [float(x.strip()) for x in entrada_datos.split(",") if x.strip()]
        if len(aguacates) < 2:
            print("-> Se requieren al menos 2 datos. Usando conjunto precargado.")
            aguacates = aguacates_default
    except ValueError:
        print("-> Entrada no válida. Usando conjunto precargado.")
        aguacates = aguacates_default
else:
    aguacates = aguacates_default

aguacates = np.array(aguacates)

# 3. Definición interactiva del rango ideal (Punto 4)
print("\n--- Definición del rango ideal ---")
try:
    min_ideal_input = input("Límite inferior del rango ideal en gramos (por defecto 400): ").strip()
    min_ideal = float(min_ideal_input) if min_ideal_input else 400.0

    max_ideal_input = input("Límite superior del rango ideal en gramos (por defecto 600): ").strip()
    max_ideal = float(max_ideal_input) if max_ideal_input else 600.0

    if min_ideal > max_ideal:
        print("-> Límite inferior mayor al superior; invirtiendo valores.")
        min_ideal, max_ideal = max_ideal, min_ideal
except ValueError:
    print("-> Valor inválido ingresado. Usando rango por defecto: [400g, 600g].")
    min_ideal, max_ideal = 400.0, 600.0

# 4. Cálculos estadísticos (Punto 1 y Punto 2)
media = np.mean(aguacates)
mediana = np.median(aguacates)
desviacion = np.std(aguacates, ddof=1)
cv = (desviacion / media) * 100 if media != 0 else 0.0

modas = stats.multimode(aguacates)
if len(modas) == len(aguacates):
    moda_str = "No hay moda (todos únicos)"
else:
    moda_str = ", ".join(f"{m:.1f} g" for m in modas)

peso_max = np.max(aguacates)
peso_min = np.min(aguacates)

dentro_rango = np.sum((aguacates >= min_ideal) & (aguacates <= max_ideal))
porcentaje_rango = (dentro_rango / len(aguacates)) * 100

# 5. Reporte de resultados
print("\n" + "=" * 50)
print("REPORTE ESTADÍSTICO DE LA COSECHA")
print("=" * 50)
print(f"Total analizados       : {len(aguacates)} aguacates")
print(f"Peso promedio (Media)  : {media:.2f} g")
print(f"Mediana                : {mediana:.2f} g")
print(f"Moda                   : {moda_str}")
print(f"Desviación estándar (s): {desviacion:.2f} g")
print(f"Coeficiente variación  : {cv:.2f}%")
print("-" * 50)
print(f"Aguacate más pesado    : {peso_max:.2f} g")
print(f"Aguacate más ligero    : {peso_min:.2f} g")
print(f"En rango ideal [{min_ideal:.0f}-{max_ideal:.0f}g]: {dentro_rango} ({porcentaje_rango:.1f}%)")
print("=" * 50 + "\n")

# 6. Visualizaciones (Punto 3: Histograma y Boxplot)
fig, (ax_hist, ax_box) = plt.subplots(1, 2, figsize=(14, 5))

# Histograma
ax_hist.hist(
    aguacates,
    bins=7,
    color="#4CAF50",
    edgecolor="black",
    alpha=0.75,
    label="Pesos registrados"
)
ax_hist.axvline(media, color="blue", linestyle="dashed", linewidth=2, label=f"Media: {media:.1f} g")
ax_hist.axvline(mediana, color="orange", linestyle="dotted", linewidth=2, label=f"Mediana: {mediana:.1f} g")
ax_hist.axvspan(min_ideal, max_ideal, color="gray", alpha=0.18, label=f"Rango ideal ({min_ideal:.0f}-{max_ideal:.0f}g)")

ax_hist.set_title("Distribución de Pesos de Aguacates", fontsize=12, fontweight="bold")
ax_hist.set_xlabel("Peso (gramos)", fontsize=10)
ax_hist.set_ylabel("Frecuencia", fontsize=10)
ax_hist.legend()
ax_hist.grid(axis="y", linestyle="--", alpha=0.5)

# Boxplot (para identificar outliers)
box = ax_box.boxplot(
    aguacates,
    vert=True,
    patch_artist=True,
    tick_labels=["Aguacates"],
    boxprops=dict(facecolor="#81C784", color="black"),
    medianprops=dict(color="orange", linewidth=2),
    flierprops=dict(marker="o", markerfacecolor="red", markersize=7, linestyle="none")
)
ax_box.axhspan(min_ideal, max_ideal, color="gray", alpha=0.18, label="Rango ideal")
ax_box.set_title("Diagrama de Caja (Detección de Outliers)", fontsize=12, fontweight="bold")
ax_box.set_ylabel("Peso (gramos)", fontsize=10)
ax_box.grid(axis="y", linestyle="--", alpha=0.5)
ax_box.legend()

plt.tight_layout()
plt.show()