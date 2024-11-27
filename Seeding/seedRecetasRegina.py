from random import choice
from dotenv import load_dotenv
import requests
from faker import Faker
import json

load_dotenv()
# Initialize Faker
faker = Faker()

# Base URL
url = 'https://jimenezmiapi.somee.com/api/Receta'

# Headers
headers = {
    'accept': '*/*',
    'Content-Type': 'application/json-patch+json',
}
imageURLs = [
    "https://images.unsplash.com/photo-1546069901-ba9599a7e63c",
    "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe",
    "https://images.unsplash.com/photo-1484723091739-30a097e8f929",
    "https://images.unsplash.com/photo-1512621776951-a57141f2eefd",
    "https://images.unsplash.com/photo-1529042410759-befb1204b468"
]


# Number of users to create
index = 0
for _ in range(100):
    datos = {
        "titulo": faker.city(),
        "descripcion": faker.text(),
        "img_Receta": choice(imageURLs),
        "num_Raciones": str(faker.random_int(min=1, max=10)),
        "tiempo": f"{faker.random_int(min=1, max=120)} minutos",
        "dificultad": "Fácil",
        "fechaCreacion": faker.date(),
        "idCategoria": faker.random_int(min = 1, max =3),
        "idIngPrincipal": faker.random_int(min=1, max=4),
        "horadecomida": "Desayuno",
        "idUser": 1,
        "status": True,
        "pasos": [
            {
                "description": faker.word(),
                "stepImage": "https://source.unsplash.com/random",
                "order": 1,
                "note": faker.text()
            }
        ],
        "ingredientes": [
            {
                "nombre": "Polvo de hadas",
            }
        ],
        "etiquetas": [
            {
                "etiquetaId": "1"
            }
        ]
    }
    print(datos)
    # Send POST request
    response = requests.post(url, headers=headers, data=json.dumps(datos))

    # Print response
    print(f"Index: {index}")
    index += 1
    print(response.__dict__)