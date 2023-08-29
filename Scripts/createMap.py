import folium
import branca
import pandas as pd
import os
from perfilSubida import elevationPerfil
from geopy.distance import geodesic

# Obtém o diretório do script atual
script_dir = os.path.dirname(__file__)

# Caminhos para os ícones
vivo_icon_path = os.path.join(script_dir, '../Images/vivo.png')
tim_icon_path = os.path.join(script_dir, '../Images/tim.png')
claro_icon_path = os.path.join(script_dir, '../Images/claro.png')
algar_icon_path = os.path.join(script_dir, '../Images/algar.png')
ligga_icon_path = os.path.join(script_dir, '../Images/ligga.png')
ligue_icon_path = os.path.join(script_dir, '../Images/ligue.jpg')
sercomtel_icon_path = os.path.join(script_dir, '../Images/sercomtel.png')
winity_icon_path = os.path.join(script_dir, '../Images/winity.jpg')
brisanet_icon_path = os.path.join(script_dir, '../Images/brisa.jpg')
userhomebooss = os.path.join(script_dir, '../Images/liksboss.png')

# Cria os ícones personalizados
VivoIcon = folium.features.CustomIcon(vivo_icon_path, icon_size=(20, 20))
TimIcon = folium.features.CustomIcon(tim_icon_path, icon_size=(20, 20))
ClaroIcon = folium.features.CustomIcon(claro_icon_path, icon_size=(20, 20))
AlgarIcon = folium.features.CustomIcon(algar_icon_path, icon_size=(20, 20))
LiggaIcon = folium.features.CustomIcon(ligga_icon_path, icon_size=(20, 20))
LigueIcon = folium.features.CustomIcon(ligue_icon_path, icon_size=(20, 20))
SercomtelIcon = folium.features.CustomIcon(sercomtel_icon_path, icon_size=(20, 20))
WinityIcon = folium.features.CustomIcon(winity_icon_path, icon_size=(20, 20))
BrisanetIcon = folium.features.CustomIcon(brisanet_icon_path, icon_size=(20, 20))

timHexa = '#094A95'
claroHexa = '#E3272F'
vivoHexa = '#660099'
algarHexa = '#1B7E6C'
brisanetHexa = '#EF7D36'
sercomtelHexa = '#121C54'
ligueHexa = '#50099E'
winityHexa = '#35EBC9'
liggaHexa= '#FF9200'

def choseBest(name):
    if 'NICA BRASIL' in name:
        Hexap = vivoHexa
    elif 'ALGAR TELECOM' in name:
        Hexap = algarHexa
    elif 'Brisanet Servicos' in name:
        Hexap = brisanetHexa
    elif 'SERCOMTEL' in name:
        Hexap = sercomtelHexa
    elif 'LIGUE TELECOM' in name:
        Hexap = ligueHexa
    elif 'Winity Ii Telecom' in name:
        Hexap = winityHexa
    elif 'LIGGA TELECOMUNICACOES' in name:
        Hexap = liggaHexa
    elif 'CLARO' in name:
        Hexap = claroHexa
    else:
        Hexap = timHexa
    return Hexap

def makeMap(homeLatitude, homeLongitude, ufsInteresse, raio_km=40):

    # Função para verificar se uma coordenada está dentro do raio
    coord_referencia = (homeLatitude, homeLongitude)

    # Caminho absoluto para o arquivo final.csv
    csv_file_path = os.path.join(script_dir, '../Data/ERBS/final.csv')

    # Carrega o arquivo CSV
    df = pd.read_csv(csv_file_path, encoding='latin-1')
    df=df[df['SiglaUf'].isin(ufsInteresse)]

    # Filtrar os objetos que estão dentro do raio de 80 km
    df["Distancia"] = df.apply(lambda row: geodesic(coord_referencia, (row["Latitude"], row["Longitude"])).kilometers, axis=1)
    df = df[df["Distancia"] <= raio_km]

    mm = folium.Map(location=[homeLatitude, homeLongitude], tiles="Stamen Terrain", prefer_canvas=True)
    folium.Marker([homeLatitude, homeLongitude], tooltip='Casa', icon=folium.features.CustomIcon(userhomebooss, icon_size=(30,30))).add_to(mm)

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
        bolutil = 0
        torreNum = str(torre.NumEstacao).replace('.0', '')

        if (((torre.RaioAlcance*1000)-torre.Distancia*1000)>=0):
            Alcance = 'Possivelmente coberto'
            bolutil = 1
        else:
            kms = (round((((torre.RaioAlcance * 1000) - torre.Distancia * 1000) / 1000), 2))*-1
            if(str(kms)=='nan'):
                Alcance = 'Possivelmente fora da área de cobertura, <b>provavelmente torre de serviço da operadora</b>, ou torre desabilitada.'
                bolutil = 0
            else:
                Alcance = 'Possivelmente fora da área de cobertura, faltam ' + str(kms) + 'km para entrar na zona de cobertura.'
                bolutil = 0

        content = f"""
        <strong>Distância:</strong> {round(torre.Distancia, 2)}km<br>
        <strong>Cobertura:</strong> {Alcance}<br><br>
        <strong>Operadora:</strong> {torre.NomeEntidade}<br>
        <strong>Torre:</strong> {torreNum}<br>
        <strong>Tecnologia:</strong> {str(torre.Tecnologia).replace('NR', '5G')}<br>
        <strong>Frequência:</strong> {torre.FreqTxMHz}Mhz<br>
        <strong>Altura:</strong> {torre.AlturaAntena}m<br><br>
        <strong>Endereço:</strong> {str(torre.EnderecoEstacao)}<br><br>
        """
        if(bolutil == 1):
            elevationPerfil(torre.Latitude, torre.Longitude, homeLatitude, homeLongitude, torre.AlturaAntena, 5, torreNum)
            addtionContent = f""" <img src="img/{torreNum}.png"  style="max-width: 100%; height: auto;">"""
            content = str(content) + str(addtionContent)

        folium.Marker(
            [torre.Latitude, torre.Longitude],
            popup=content,
            tooltip=torre.NomeEntidade,
            icon=IconP
        ).add_to(mm)

    mm.save('map.html')
    return 'map.html'
    
makeMap(-9.192850234349876, -40.41193949600815, ['PE'], 40)
#https://ispdesign.ui.com/#