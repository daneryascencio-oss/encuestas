import matplotlib.pyplot as plt
from collections import Counter

# ===============================
# DATOS DE LA MUESTRA (10 personas)
# ===============================

personas = [
    "ALONDRA ANDRADE",
    "DANERY ASCENCIO",
    "SAMUEL BATRES",
    "FRANCISCA BONILLA",
    "GENESIS CRUZ",
    "JUAN ESPINAL",
    "KEVIN CASTRO",
    "MARIA MARTINEZ",
    "ANDREA RODRIGUEZ",
    "OMAR VENTURA"
]

# 1. Gráfico de Líneas: Horas de sueño
horas_dormidas = [7, 6, 8, 5, 9, 6, 7, 8, 5, 7]

plt.figure(figsize=(7,4))
plt.plot(personas, horas_dormidas, marker='o', color='b')
plt.title("¿Cuántas horas dormiste anoche?")
plt.xlabel("Personas")
plt.ylabel("Horas dormidas")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Gráfico de Barras: Tazas de café por día
tazas_cafe = [2, 1, 3, 0, 2, 1, 2, 4, 1, 3]

plt.figure(figsize=(7,4))
plt.bar(personas, tazas_cafe, color='orange')
plt.title("¿Cuántas tazas de café tomas al día?")
plt.xlabel("Personas")
plt.ylabel("Tazas de café")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Gráfico de Pastel: Red social más usada
redes = [
    "Instagram", "Facebook", "TikTok", "X", "Instagram",
    "Instagram", "TikTok", "Facebook", "X", "Instagram"
]

conteo_redes = Counter(redes)

plt.figure(figsize=(6,6))
plt.pie(conteo_redes.values(), labels=conteo_redes.keys(),
        autopct='%1.1f%%', startangle=90)
plt.title("¿Qué red social usas más?")
plt.show()

# 4. Histograma: Minutos en llegar a la universidad
minutos_u = [15, 20, 35, 10, 25, 40, 30, 15, 50, 20]

plt.figure(figsize=(7,4))
plt.hist(minutos_u, bins=5, color='green', edgecolor='black')
plt.title("¿Cuántos minutos te tardas en llegar a la U?")
plt.xlabel("Minutos")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()
