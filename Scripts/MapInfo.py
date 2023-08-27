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