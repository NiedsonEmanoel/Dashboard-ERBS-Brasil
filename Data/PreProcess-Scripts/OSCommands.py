import os
import pandas as pd

Folder_ERBS = '../ERBS/'


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

            inputA = input('VERIFICOU SE NÃO HÁ O ARQUIVO .CSV ÚNICO-FINAL? (SIM)/(NAO)')
            if(inputA != 'SIM'):
                print('Interrompido pela segurança dos dados.')
                return

            inputB = input('PROSSEGUIR COM A EXCLUSÃO? (sim)/(nao)')
            if(inputB != 'sim'):
                print('Interrompido pela segurança dos dados.')
                return

            inputC = input('QUAL A DATA DE LANÇAMENTO DO JOGO RDR 2? (DD/MM/AAAA)')
            if(inputC != '26/10/2018'):
                print('Interrompido pela segurança dos dados.')
                return

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
