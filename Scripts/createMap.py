import folium
import branca
import pandas as pd
from MapInfo import *

# Carregar os dados do arquivo CSV
df = pd.read_csv('../Data/ERBS/final.csv',encoding='latin-1')
df = df.sample(frac=0.001, random_state=42)

mm = folium.Map(location=[-14.4043717, -47.0065407], tiles="Stamen Terrain")
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

    Hexap = choseBest(torre.NomeEntidade)

    if 'NICA BRASIL' in torre.NomeEntidade:
        IconP = VivoIcon
        Hexap = vivoHexa
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

    content = f"""
    <strong>Operadora:</strong> {torre.NomeEntidade}<br>
    <strong>Tecnologia:</strong> {str(torre.Tecnologia).replace('NR', '5G')}<br>
    <strong>Frequência:</strong> {torre.FreqTxMHz}Mhz<br>
    <strong>Altura:</strong> {torre.AlturaAntena}m<br>
    """
    folium.Marker(
        [torre.Latitude, torre.Longitude],
        popup=content,
        tooltip=torre.NomeEntidade,
        icon=IconP
    ).add_to(mm)

    folium.Circle(
        location=[torre.Latitude, torre.Longitude],
        radius=torre.RaioAlcance*1000,
        popup=content,
        color=Hexap,
        fill=True,
        fill_color=Hexap,
    ).add_to(mm)
mm