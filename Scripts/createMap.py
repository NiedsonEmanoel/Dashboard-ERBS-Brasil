import folium
import pandas as pd

IconP=folium.features.CustomIcon('../Images/vivo.png', icon_size=(20,20))
Hexap=''

VivoIcon = folium.features.CustomIcon('../Images/vivo.png', icon_size=(20,20))
TimIcon = folium.features.CustomIcon('../Images/tim.png', icon_size=(20,20))
ClaroIcon = folium.features.CustomIcon('../Images/claro.png', icon_size=(20,20))

AlgarIcon = folium.features.CustomIcon('../Images/algar.png', icon_size=(20,20))
LiggaIcon = folium.features.CustomIcon('../Images/ligga.png', icon_size=(20,20))
LigueIcon = folium.features.CustomIcon('../Images/ligue.jpg', icon_size=(20,20))

SercomtelIcon = folium.features.CustomIcon('../Images/sercomtel.png', icon_size=(20,20))
WinityIcon = folium.features.CustomIcon('../Images/winity.jpg', icon_size=(20,20))
BrisanetIcon = folium.features.CustomIcon('../Images/brisa.jpg', icon_size=(20,20))


timHexa = '#024691'
claroHexa = '#E3272F'
vivoHexa = '#660099'
algarHexa = '#1B7E6C'
brisanetHexa = '#EF7D36'
sercomtelHexa = '#121C54'
ligueHexa = '#50099E'
winityHexa = '#35EBC9'
liggaHexa= '#FF9200'

# Carregar os dados do arquivo CSV
df = pd.read_csv('../Data/ERBS/final.csv',encoding='latin-1')
df_sample = df.sample(frac=0.01, random_state=42)

del df

filedf = df_sample.iloc[2800]


if 'NICA BRASIL' in filedf.NomeEntidade:
    IconP = VivoIcon
    Hexap = vivoHexa
elif 'ALGAR TELECOM' in filedf.NomeEntidade:
    IconP = AlgarIcon
    Hexap = algarHexa
elif 'Brisanet Servicos' in filedf.NomeEntidade:
    IconP = BrisanetIcon
    Hexap = brisanetHexa
elif 'SERCOMTEL' in filedf.NomeEntidade:
    IconP = SercomtelIcon
    Hexap = sercomtelHexa
elif 'LIGUE TELECOM' in filedf.NomeEntidade:
    IconP = LigueIcon
    Hexap = ligueHexa
elif 'Winity Ii Telecom' in filedf.NomeEntidade:
    IconP = WinityIcon
    Hexap = winityHexa
elif 'LIGGA TELECOMUNICACOES' in filedf.NomeEntidade:
    IconP = LiggaIcon
    Hexap = liggaHexa
elif 'CLARO' in filedf.NomeEntidade:
    IconP = ClaroIcon
    Hexap = claroHexa
else:
    IconP = TimIcon
    Hexap = timHexa


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


# informacoes
    #NomeEntidade           TIM S A
    #NumEstacao         684065134.0
    #EnderecoEstacao     RUA ALBITA
    #EndComplemento             NaN
    #SiglaUf                     MG
    #CodMunicipio         3106200.0
    #Tecnologia                 LTE
    #tipoTecnologia             NaN
    #FreqTxMHz               2130.0
    #FreqRxMHz               1940.0
    #GanhoAntena               15.9
    #AlturaAntena              41.0
    #Latitude            -19.941139
    #Longitude             -43.9265
    #RaioAlcance           8.020713
    #Name: 1042898, dtype: object
