import folium
import pandas as pd
from MapInfo import *

IconP=folium.features.CustomIcon('../Images/vivo.png', icon_size=(20,20))
Hexap=''

# Carregar os dados do arquivo CSV
df = pd.read_csv('../Data/ERBS/final.csv',encoding='latin-1')
df_sample = df.sample(frac=0.01, random_state=42)

del df

filedf = df_sample.iloc[16000]

IconP, Hexap = choseBest(filedf.NomeEntidade)
m = folium.Map(location=[filedf.Latitude, filedf.Longitude], tiles="Stamen Terrain")

content = f"""
<strong>Operadora:</strong> {filedf.NomeEntidade}<br>
<strong>Tecnologia:</strong> {str(filedf.Tecnologia).replace('NR', '5G')}<br>
<strong>Frequência:</strong> {filedf.FreqTxMHz}Mhz<br>
<strong>Altura:</strong> {filedf.AlturaAntena}m<br>
"""

folium.Marker(
    [filedf.Latitude, filedf.Longitude],
    popup=content,
    tooltip=filedf.NomeEntidade,
    icon=IconP
).add_to(m)

folium.Circle(
    location=[filedf.Latitude, filedf.Longitude],
    radius=filedf.RaioAlcance*1000,
    popup=content,
    color=Hexap,
    fill=True,
    fill_color=Hexap,
).add_to(m)

m
