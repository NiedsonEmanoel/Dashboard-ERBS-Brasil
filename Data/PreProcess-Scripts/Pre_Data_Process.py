import pandas as pd
from OSCommands import *

def preData():
    extractZP('14.zip', Folder_ERBS)
    extractZP('23.zip', Folder_ERBS)
    extractZP('24.zip', Folder_ERBS)
    extractZP('27.zip', Folder_ERBS)

    renomear_arquivos_csv(Folder_ERBS)
    rPD = juntar_csvs_em_dataframe(Folder_ERBS)
    apagarCSV_Separado(Folder_ERBS, rPD)

preData()