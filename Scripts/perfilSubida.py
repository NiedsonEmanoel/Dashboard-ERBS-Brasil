import requests
import numpy as np
import matplotlib.pyplot as plt

# Função para obter as altitudes de vários pontos usando a API de elevação do Open-Elevation
def get_elevations(locations):
    locations_str = "|".join([f"{lat},{lon}" for lat, lon in locations])
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={locations_str}"
    response = requests.get(url)
    data = response.json()
    elevations = [result['elevation'] for result in data['results']]
    return elevations



def elevationPerfil(latitudeA, longitudeA, latitudeB, longitudeB, torreAltura, baseAltura, codBase):
    # Calculando os incrementos ao longo da linha reta entre os pontos
    num_points = 100
    lats = np.linspace(latitudeA, latitudeB, num_points)
    lons = np.linspace(longitudeA, longitudeB, num_points)

    # Preparando as coordenadas para as solicitações de elevação
    locations = list(zip(lats, lons))

    # Obtendo as altitudes para todas as coordenadas de uma vez
    altitudes = get_elevations(locations)

    altitudes[0] = altitudes[0] + torreAltura
    altitudes[-1] = altitudes[-1] + baseAltura

    # Verificando colisões ponto a ponto e mostrando os pontos onde ocorrem
    collision_indices = []
    for i in range(num_points):
        equidistant_altitude = (altitudes[i] + altitudes[-i-1])/2
        if equidistant_altitude >= (altitudes[0] + altitudes[-1])/2:
            if(i>=4):
                if(i<=96):
                    collision_indices.append(i)


    # Mostrando os índices das colisões no gráfico
    if collision_indices:
        collision_text = ', '.join([str(idx) for idx in collision_indices])

    # Estilizando o gráfico
    plt.figure(figsize=(10, 6))
    plt.fill_between(range(num_points), altitudes, color='blue', alpha=0.3, label='Variação da Altitude')
    plt.plot(altitudes, color='blue', linewidth=2)
    #plt.xlabel('Distância ao longo da linha reta')
    plt.ylabel('Altitude (metros)')
    plt.title('Perfil de Elevação')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Traçando uma linha reta entre a primeira e última altitude
    plt.plot([0, num_points - 1], [altitudes[0], altitudes[-1]], 'r--')
    plt.scatter([0, num_points - 1], [altitudes[0], altitudes[-1]], color='red', zorder=5)

    # Destacando os pontos iniciais e finais
    plt.scatter([0, num_points - 1], [altitudes[0], altitudes[-1]], color='red', edgecolors='black', linewidths=1, s=80, zorder=5)

    # Adicionando texto aos pontos
    plt.text(3, altitudes[0]+3, f'Ponto A', ha='right', va='bottom', fontsize=9, color='blue')
    plt.text(num_points - 6, altitudes[-1]+4, f'Ponto Receptor', ha='left', va='bottom', fontsize=9, color='blue')

    plt.scatter(collision_indices, [altitudes[i] for i in collision_indices], color='red', marker='x', s=40)

    # Ajustando o eixo y para começar a partir do valor mínimo da altitude
    min_altitude = min(altitudes)
    plt.ylim(min_altitude-2, max(altitudes)+10)

    # Ajustando layout
    plt.tight_layout()

    # Mostrando o gráfico
    plt.savefig('img/'+str(codBase)+'.png', format='png')
