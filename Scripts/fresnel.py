import folium
import pandas as pd

# Carregar os dados do arquivo CSV
df = pd.read_csv('../Data/ERBS/final.csv',encoding='latin-1')
df_sample = df.sample(frac=0.01, random_state=42)

m = folium.Map(location=[-9.3979745, -40.519919])

m


import math

def calculate_range(freq_tx_mhz, freq_rx_mhz, ganho_antena, altura_antena):
    altura_antena_m = altura_antena  # Altura da antena em metros
    
    # Calculando o raio de alcance usando a fórmula
    range_km = math.sqrt((2 * altura_antena_m / 1.23) * (math.sqrt(ganho_antena) / (freq_tx_mhz * freq_rx_mhz)))
    
    return range_km

# Dados de exemplo
freq_tx = 5800  # Frequência de transmissão em MHz
freq_rx = 5800   # Frequência de recepção em MHz
ganho_antena = 35  # Ganho da antena (relação)
altura_antena = 2  # Altura da antena em metros

# Calcula o raio de alcance
raio_alcance = calculate_range(freq_tx, freq_rx, ganho_antena, altura_antena)*1000

print(f"O raio de alcance estimado é de {raio_alcance:.2f} m")
