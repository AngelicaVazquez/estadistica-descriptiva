import numpy as np
import statistics as stast
import matplotlib.pyplot as plt


#pesos de las zanahorias en gramos
zanahorias = [300, 280, 290, 310, 275, 290, 295, 315, 290, 280, 310, 305]

# Estadisticas descriptivas
media = np.mean(zanahorias) #promedio
mediana = np.median(zanahorias) #valor central
moda = stast.mode(zanahorias) #valor mas común
desviacion = np.std(zanahorias) #VARIABILIDAD

#Resultados
print(f"CONCURSO DE ZANAHORIAS")
print(f"Los siguientes datos son relativos al peso de las zanahorias presentadas por los participantes")
print(f"Media: {media} gramos")
print(f"Mediana: {mediana} gramos")
print(f"Moda: {moda} gramos")
print(f"Desviación estándar: {desviacion:.2f} gramos")

plt.figure(figsize=(9, 5))

# Histograma con barras naranjas
conteo, bordes, _ = plt.hist(
    zanahorias,
    bins=8,
    color="#FF7F0E",
    edgecolor="black",
    alpha=0.75,
    label="Pesos registrados"
)

# Líneas guía de medidas de tendencia central
plt.axvline(media, color="blue", linestyle="dashed", linewidth=2, label=f"Media: {media:.1f} g")
plt.axvline(mediana, color="green", linestyle="dotted", linewidth=2, label=f"Mediana: {mediana:.1f} g")
plt.axvline(moda, color="red", linestyle="dashdot", linewidth=2, label=f"Moda: {moda:.1f} g")

plt.title("Distribución de Pesos en el Concurso de Zanahorias", fontsize=14, fontweight="bold")
plt.xlabel("Peso (gramos)", fontsize=11)
plt.ylabel("Número de Zanahorias", fontsize=11)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()

plt.show()

""""
📢 Historia:
Un grupo de agricultores está participando en un concurso para ver quién tiene las zanahorias más grandes. Han medido el peso (en gramos) de 12 zanahorias y necesitan analizar los datos para ver qué tan uniformes son sus cultivos.
📌 Tu misión
📊 Escribe un programa en Python que haga lo siguiente:
1. Calcule la media (promedio) del peso de las zanahorias.
2. Encuentre la mediana del peso.
3. Determine la moda (peso más común).
4. Calcule la desviación estándar para ver qué tanto varían los pesos.
5. Muestre los resultados de forma clara y divertida.
📌 Estos son los pesos (en gramos) de las zanahorias concursantes:
zanahorias = [300, 280, 290, 310, 275, 290, 295, 315, 290, 280, 310, 305]

🚀 Bonus (Opcional)
📊 Extra 1: Agrega una visualización con Matplotlib 📉 para mostrar la distribución de los pesos.
🤖 Extra 2: Modifica el código para que el usuario pueda ingresar los pesos de nuevas zanahorias.
"""