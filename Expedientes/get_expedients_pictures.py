import requests
import os
import hashlib
from bs4 import BeautifulSoup

image_hashes = set()
folder_path = '../raw_html'
for file_name in os.listdir(folder_path):
    if file_name.endswith('.html'):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, encoding='windows-1252') as file:
            try:
                soup = BeautifulSoup(file, 'html.parser')
            except:
                print(f"Error al abrir el archivo: {file_name}")
                continue
            nombre_usuario = soup.find('h4').text
            print("Buscando imagen de:" + nombre_usuario)
            for img in soup.find_all('img'):
                img_url = img.get('src')
                img_name = img.get('alt')
                response = requests.get("https://plataforma.utmetropolitana.edu.mx/panel/" + img_url)
                img_data = response.content
                img_hash = hashlib.md5(img_data).hexdigest()
                img_path = f'./images/{nombre_usuario}.jpg'
                if os.path.exists(img_path):
                    print(f"Imagen ya guardada: {nombre_usuario}.jpg")
                    continue
                if img_hash in image_hashes:
                    print(f"Imagen duplicada: {nombre_usuario}.jpg")
                    continue
                with open(img_path, 'wb') as handler:
                    handler.write(img_data)
                image_hashes.add(img_hash)
                print(f"Imagen guardada: {nombre_usuario}.jpg")