from pprint import pprint

import bs4 as bs
import pandas as pd
import os

from bs4 import NavigableString

# Path to the folder containing the raw HTML files
raw_html_folder = './raw_html'

main_csv = pd.DataFrame()
errores = 0
#List the folder
file_paths = os.listdir(raw_html_folder)
for filepath in file_paths: #Cada uno de los archivos HTML
    try:
        with open(f'{raw_html_folder}/{filepath}', 'r') as f:   
            soup = bs.BeautifulSoup(f, 'html.parser')
            dc = {}
            # Extraer el nombre
            dc["Nombre"] = soup.find('h4').text
            # Extraer datos personales
            for i_tag in soup.find_all('i'):
                key = i_tag.nextSibling
                if isinstance(key, NavigableString):
                    key = key.strip()
                value_tag = i_tag.find_next_sibling('input')
                if value_tag:
                    value = value_tag['value']
                    dc[key] = value
            pprint(dc)
            input()
    except Exception as e:
        errores += 1
        print(e)
        input("Error encontrado, errores encontrados: " + str(errores))
        continue

print("Errores" + str(errores))
