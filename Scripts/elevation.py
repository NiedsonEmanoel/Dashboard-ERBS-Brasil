import requests
import numpy as np
import matplotlib.pyplot as plt

# Coordenadas dos pontos A e B
point_a = (-9.228876651530582, -40.372077122802764)
point_b = (-9.193258496938439, -40.411352142067884)

# Função para obter as altitudes de vários pontos usando a API de elevação do Open-Elevation
def get_elevations(locations):
    locations_str = "|".join([f"{lat},{lon}" for lat, lon in locations])
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={locations_str}"
    response = requests.get(url)
    data = response.json()
    elevations = [result['elevation'] for result in data['results']]
    return elevations

# Calculando os incrementos ao longo da linha reta entre os pontos
num_points = 100
lats = np.linspace(point_a[0], point_b[0], num_points)
lons = np.linspace(point_a[1], point_b[1], num_points)

# Preparando as coordenadas para as solicitações de elevação
locations = list(zip(lats, lons))

# Obtendo as altitudes para todas as coordenadas de uma vez
altitudes = get_elevations(locations)

altitudes[0] = altitudes[0] + 0
altitudes[-1] = altitudes[-1] + 0

# Estilizando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(altitudes, color='blue', linewidth=2, label='Variação da Altitude')
plt.xlabel('Distância ao longo da linha reta')
plt.ylabel('Altitude (metros)')
plt.title('Perfil de Elevação entre Dois Pontos')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Traçando uma linha reta entre a primeira e última altitude
plt.plot([0, num_points - 1], [altitudes[0], altitudes[-1]], 'r--')
plt.scatter([0, num_points - 1], [altitudes[0], altitudes[-1]], color='red', zorder=5)

# Destacando os pontos iniciais e finais
plt.scatter([0, num_points - 1], [altitudes[0], altitudes[-1]], color='red', edgecolors='black', linewidths=1, s=80, zorder=5)

# Adicionando texto aos pontos
plt.text(0, altitudes[0], f'({point_a[0]:.4f}, {point_a[1]:.4f})', ha='right', va='bottom', fontsize=9, color='blue')
plt.text(num_points - 1, altitudes[-1], f'({point_b[0]:.4f}, {point_b[1]:.4f})', ha='left', va='bottom', fontsize=9, color='blue')

# Ajustando layout
plt.tight_layout()

# Mostrando o gráfico
plt.show()

