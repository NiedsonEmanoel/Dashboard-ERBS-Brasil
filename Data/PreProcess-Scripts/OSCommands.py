import os
import pandas as pd
import zipfile
import requests

Folder_ERBS = '../ERBS/'

ListFiles = [
    '14.zip', '23.zip', '24.zip', '27.zip',
    'csvfile-doesnotmov (1).csv', 'csvfile-doesnotmov (2).csv',
    'csvfile-doesnotmov (3).csv', 'csvfile-doesnotmov (4).csv',
    'csvfile-doesnotmov (5).csv', 'csvfile-doesnotmov (6).csv',
    'csvfile-doesnotmov (7).csv', 'csvfile-doesnotmov (8).csv',
    'csvfile-doesnotmov (9).csv', 'csvfile-doesnotmov (10).csv',
    'csvfile-doesnotmov (11).csv', 'csvfile-doesnotmov (12).csv',
    'csvfile-doesnotmov (13).csv', 'csvfile-doesnotmov (14).csv',
    'csvfile-doesnotmov (15).csv', 'csvfile-doesnotmov (16).csv',
    'csvfile-doesnotmov (17).csv', 'csvfile-doesnotmov (18).csv',
    'csvfile-doesnotmov (19).csv', 'csvfile-doesnotmov (20).csv',
    'csvfile-doesnotmov (21).csv', 'csvfile-doesnotmov (22).csv',
    'csvfile-doesnotmov (23).csv'
]


def hasLockrem(pasta):
    for file in os.listdir(pasta):
        if file.endswith(".lockrem"):
            return True
    return False

def hasLockpd(pasta):
    for file in os.listdir(pasta):
        if file.endswith(".lockpd"):
            return True
    return False

def hasLockdel(pasta):
    for file in os.listdir(pasta):
        if file.endswith(".lockdel"):
            return True
    return False

def pushFiles(pasta, files):
    base_url = "https://github.com/NiedsonEmanoel/Dashboard-ERBS-Brasil/raw/68ac4504d06f5b414e493a61c3cafa7f197e152b/Data/ERBS/"
    
    if hasLockdel(pasta=pasta):
        print('Operação bloqueada, dados pré-processados.')
        return

    if hasLockpd(pasta=pasta):
        print('Operação bloqueada, dados pré-processados.')
        return

    if hasLockrem(pasta=pasta):
        print('Operação bloqueada, dados pré-processados.')
        return

    # Verificar se o caminho da pasta é válido
    if not os.path.exists(pasta):
        print("Caminho inválido.")
        return

    for file in files:
        url = base_url + file.replace(' ', '%20')
        file_path = os.path.join(pasta, file)

        if not os.path.exists(file_path):
            response = requests.get(url)
            
            if response.status_code == 200:
                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"Arquivo '{file}' baixado com sucesso.")
            else:
                print(f"Não foi possível baixar o arquivo '{file}'.")
        else:
            print(f"O arquivo '{file}' já existe na pasta.")

def extractZP(zip_pathe, extract_path):
    """
    Extrai o conteúdo de um arquivo ZIP para o diretório de extração e depois exclui o arquivo ZIP.

    Args:
        zip_pathe (str): Nome do arquivo ZIP.
        extract_path (str): Caminho para o diretório de extração.
    """
    zip_path = extract_path+zip_pathe
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    os.remove(zip_path)  # Remove o arquivo ZIP após a extração    

def renomear_arquivos_csv(pasta):
    """
    Renomeia arquivos CSV na pasta especificada, atribuindo números sequenciais.

    Args:
        pasta (str): O caminho para a pasta contendo os arquivos CSV.
    """
    if hasLockrem(pasta=pasta):
        print('Operação bloqueada, dados pré-processados.')
    else:
        # Lista todos os arquivos na pasta que terminam com '.csv'
        arquivos_csv = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith('.csv')]
        arquivos_csv.sort()  # Ordena a lista de arquivos CSV alfabeticamente

        # Itera pelos arquivos CSV e os renomeia com números sequenciais
        for i, arquivo_csv in enumerate(arquivos_csv, start=1):
            caminho_antigo = os.path.join(pasta, arquivo_csv)  # Obtém o caminho completo do arquivo antigo
            novo_nome = f'{i}.csv'
            caminho_novo = os.path.join(pasta, novo_nome)  # Obtém o caminho completo do novo nome de arquivo

            # Renomeia o arquivo movendo-o para o novo nome e caminho
            os.rename(caminho_antigo, caminho_novo)
            print(f'Renomeando {caminho_antigo} para {caminho_novo}')
        
        lock_contents = "This file is a lock file. Do not remove."
        file_path = str(pasta)+'csv.lockrem'
        with open(file_path, 'w') as lock_file:
            lock_file.write(lock_contents)

def juntar_csvs_em_dataframe(pasta, encoding='latin1'):
    """
    Lê arquivos CSV da pasta especificada, converte cada um em um DataFrame e os junta em um só.

    Args:
        pasta (str): O caminho para a pasta contendo os arquivos CSV.
        encoding (str, opcional): Codificação dos arquivos CSV. Padrão é 'latin1'.
    
    Returns:
        pandas.DataFrame: Um único DataFrame que contém os dados de todos os arquivos CSV.
    """
    if hasLockpd(pasta=pasta):
        print('Operação bloqueada, dados pré-processados.')
        return ''
    else:
        arquivos_csv = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith('.csv')]
        
        dataframes = []
        
        for arquivo_csv in arquivos_csv:
            caminho_arquivo = os.path.join(pasta, arquivo_csv)
            df = pd.read_csv(caminho_arquivo, encoding=encoding)
            dataframes.append(df)
        
        dataframe_final = pd.concat(dataframes, ignore_index=True)

        lock_contents = "This file is a lock file. Do not remove."
        file_path = str(pasta)+'csv.lockpd'
        with open(file_path, 'w') as lock_file:
            lock_file.write(lock_contents)
        
        return dataframe_final

def apagarCSV_Separado(pasta, df):
    countFiles = len(os.listdir(pasta))
    ableToWrite = 1
    if (countFiles >= 5):
        if hasLockdel(pasta=pasta):
            print('Operação bloqueada, dados pré-processados.')
            return
        else:
            # Lista todos os arquivos na pasta que terminam com '.csv'
            arquivos_csv = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith('.csv')]
            arquivos_csv.sort()  # Ordena a lista de arquivos CSV alfabeticamente

            for i, arquivo_csv in enumerate(arquivos_csv, start=1):
                caminho = os.path.join(pasta, arquivo_csv)  # Obtém o caminho completo do arquivo antigo
                if(arquivo_csv != 'final.csv'):
                    os.remove(caminho)
                    print(f'Deletado {caminho}')
                else:
                    print('Interrompido pela segurança dos dados.')
                    ableToWrite = 0
                    
            if(ableToWrite == 1):
                file_pathFinal = str(pasta)+'final.csv'
                df.to_csv(file_pathFinal, index=False, encoding='latin-1')

            lock_contents = "This file is a lock file. Do not remove."
            file_path = str(pasta)+'csv.lockdel'
            with open(file_path, 'w') as lock_file:
                lock_file.write(lock_contents)

            return
    else:
        print('Interrompido pela segurança dos dados.')
        return 
