import pandas as pd
import numpy as np
import os
from unidecode import unidecode

# Caminho para o excel contendo o nome dos alunos junto ao RA
df = pd.read_excel('Caminho para excel', dtype={'RA': str})
diretorio = "Caminho diretorio"

def renameImage():
    ListFile = os.listdir(diretorio)

    files_no_extension = np.char.split(ListFile, '.').str[0]

    unidecode_vectorized = np.vectorize(lambda x: unidecode(str(x)).upper())

    colTreated = pd.Series(unidecode_vectorized(df['NOME']), index=df.index)

    dictRa = df.set_index(colTreated)['RA'].to_dict()

    for file in files_no_extension:
            
            if file in dictRa:
                ra = dictRa[file]
                print(f"Arquivo: {file}, RA correspondente: {ra}")
                os.rename(f"{diretorio}/{file}.JPG", f"{diretorio}/{ra}.jpg")
                print(f"Arquivo renomeado para: {ra}.jpg com sucesso")
                print("-" * 50)

renameImage()
