import os
import gdown
import duckdb
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

url_pasta = 'https://drive.google.com/drive/folders/1Y7Fh8yeI-waTCd48drpEWaHaLmgCdKW2?usp=sharing'
diretorio_local = './pasta_gdown'

# Função para baixar os arquivos do Google Drive.
def baixar_os_arquivos_do_google_drive(url_pasta, diretorio_local):
   os.makedirs(diretorio_local, exist_ok=True)
   gdown.download_folder(url_pasta,out=diretorio_local, quiet=False, use_cookies=False)

# Função para carregar os arquivos do Google Drive.
if __name__ == '__main__':
    url_pasta = 'https://drive.google.com/drive/folders/1Y7Fh8yeI-waTCd48drpEWaHaLmgCdKW2?usp=sharing'
    diretorio_local = './pasta_gdown'
    baixar_os_arquivos_do_google_drive(url_pasta, diretorio_local)