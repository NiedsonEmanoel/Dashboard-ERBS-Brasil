import folium
import branca
import pandas as pd
from MapInfo import *
from geopy.distance import geodesic

# Coordenadas de referência (latitude e longitude)
homeLatitude, homeLongitude = -18.707441377814433, -53.8724935894998
raio_km = 40

# Função para verificar se uma coordenada está dentro do raio
coord_referencia = (homeLatitude, homeLongitude)
def dentro_do_raio(coord1, coord2, raio_km):
    distancia = geodesic(coord1, coord2).kilometers
    return distancia <= raio_km

# Carregar os dados do arquivo CSV
df = pd.read_csv('../Data/ERBS/final.csv',encoding='latin-1')
df=df[df['SiglaUf'] == 'MS']

# Filtrar os objetos que estão dentro do raio de 80 km
df["Distancia"] = df.apply(lambda row: geodesic(coord_referencia, (row["Latitude"], row["Longitude"])).kilometers, axis=1)
df = df[df["Distancia"] <= raio_km]

mm = folium.Map(location=[homeLatitude, homeLongitude], tiles="Stamen Terrain", prefer_canvas=True)
folium.Marker([homeLatitude, homeLongitude], tooltip='Casa', icon=folium.features.CustomIcon('../Images/liksboss.png', icon_size=(30,30))).add_to(mm)

folium.raster_layers.TileLayer(
    tiles='https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
    attr='google',
    name='Google Maps',
    max_zoom=20,
    subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
    overlay=False,
    control=True
).add_to(mm)

folium.raster_layers.TileLayer(
    tiles='https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='google',
    name='Google Satellite',
    max_zoom=20,
    subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
    overlay=False,
    control=True
).add_to(mm)

folium.raster_layers.TileLayer(
    tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
    attr = 'Google',
    max_zoom=20,
    name = 'Google Terrain',
    overlay = False,
    control = True
).add_to(mm)
folium.raster_layers.TileLayer(
    tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
    attr = 'Google',
    max_zoom=20,
    name = 'Google Satellite Hybrid',
    overlay = False,
    control = True
).add_to(mm)
folium.raster_layers.TileLayer(
    tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr = 'Esri',
    max_zoom=20,
    name = 'Esri Satellite',
    overlay = False,
    control = True
).add_to(mm)


folium.LayerControl().add_to(mm)

for torre in df.itertuples():
    IconP = folium.features.CustomIcon('../Images/vivo.png', icon_size=(20,20))
    VivoIcon = folium.features.CustomIcon('../Images/vivo.png', icon_size=(20,20))
    TimIcon = folium.features.CustomIcon('../Images/tim.png', icon_size=(20,20))
    ClaroIcon = folium.features.CustomIcon('../Images/claro.png', icon_size=(20,20))

    AlgarIcon = folium.features.CustomIcon('../Images/algar.png', icon_size=(20,20))
    LiggaIcon = folium.features.CustomIcon('../Images/ligga.png', icon_size=(20,20))
    LigueIcon = folium.features.CustomIcon('../Images/ligue.jpg', icon_size=(20,20))

    SercomtelIcon = folium.features.CustomIcon('../Images/sercomtel.png', icon_size=(20,20))
    WinityIcon = folium.features.CustomIcon('../Images/winity.jpg', icon_size=(20,20))
    BrisanetIcon = folium.features.CustomIcon('../Images/brisa.jpg', icon_size=(20,20))

    if 'NICA BRASIL' in torre.NomeEntidade:
        IconP = VivoIcon
    elif 'ALGAR TELECOM' in torre.NomeEntidade:
        IconP = AlgarIcon
    elif 'Brisanet Servicos' in torre.NomeEntidade:
        IconP = BrisanetIcon
    elif 'SERCOMTEL' in torre.NomeEntidade:
        IconP = SercomtelIcon
    elif 'LIGUE TELECOM' in torre.NomeEntidade:
        IconP = LigueIcon
    elif 'Winity Ii Telecom' in torre.NomeEntidade:
        IconP = WinityIcon
    elif 'LIGGA TELECOMUNICACOES' in torre.NomeEntidade:
        IconP = LiggaIcon
    elif 'CLARO' in torre.NomeEntidade:
        IconP = ClaroIcon
    else:
        IconP = TimIcon
    
    Alcance = ''

    if (((torre.RaioAlcance*1000)-torre.Distancia*1000)>=0):
        Alcance = 'Possivelmente coberto'
    else:
        kms = (round((((torre.RaioAlcance * 1000) - torre.Distancia * 1000) / 1000), 2))*-1
        if(str(kms)=='nan'):
            Alcance = 'Possivelmente fora da área de cobertura, <b>provavelmente torre de serviço da operadora</b>.'
        else:
            Alcance = 'Possivelmente fora da área de cobertura, faltam ' + str(kms) + 'km para entrar na zona de cobertura.'

    content = f"""
    <strong>Distância:</strong> {round(torre.Distancia, 2)}km<br>
    <strong>Cobertura:</strong> {Alcance}<br><br>
    <strong>Operadora:</strong> {torre.NomeEntidade}<br>
    <strong>Torre:</strong> {str(torre.NumEstacao).replace('.0', '')}<br>
    <strong>Tecnologia:</strong> {str(torre.Tecnologia).replace('NR', '5G')}<br>
    <strong>Frequência:</strong> {torre.FreqTxMHz}Mhz<br>
    <strong>Altura:</strong> {torre.AlturaAntena}m<br><br>
    <strong>Endereço:</strong> {str(torre.EnderecoEstacao)}<br>
    """

    folium.Marker(
        [torre.Latitude, torre.Longitude],
        popup=content,
        tooltip=torre.NomeEntidade,
        icon=IconP
    ).add_to(mm)

mm.save('map.html')