import pandas as pd
from OSCommands import *

def preData():
    renomear_arquivos_csv(Folder_ERBS)
    rPD = juntar_csvs_em_dataframe(Folder_ERBS)
    apagarCSV_Separado(Folder_ERBS, rPD)

preData()