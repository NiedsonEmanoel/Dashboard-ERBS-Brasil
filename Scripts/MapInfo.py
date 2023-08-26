import folium

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

def choseBest(name):
    if 'NICA BRASIL' in name:
        IconP = VivoIcon
        Hexap = vivoHexa
    elif 'ALGAR TELECOM' in name:
        IconP = AlgarIcon
        Hexap = algarHexa
    elif 'Brisanet Servicos' in name:
        IconP = BrisanetIcon
        Hexap = brisanetHexa
    elif 'SERCOMTEL' in name:
        IconP = SercomtelIcon
        Hexap = sercomtelHexa
    elif 'LIGUE TELECOM' in name:
        IconP = LigueIcon
        Hexap = ligueHexa
    elif 'Winity Ii Telecom' in name:
        IconP = WinityIcon
        Hexap = winityHexa
    elif 'LIGGA TELECOMUNICACOES' in name:
        IconP = LiggaIcon
        Hexap = liggaHexa
    elif 'CLARO' in name:
        IconP = ClaroIcon
        Hexap = claroHexa
    else:
        IconP = TimIcon
        Hexap = timHexa
    return IconP, Hexap