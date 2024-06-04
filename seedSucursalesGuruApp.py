import os
import random

import psycopg2
from dotenv import load_dotenv
from faker import Faker

load_dotenv()
db_url = os.getenv("GURUAPP_DB_URL")
# Initialize Faker
fake = Faker()

# Establish a connection to your database
connection = psycopg2.connect(db_url)
cursor = connection.cursor()

# Number of entries to create
num_entries = 100
PuntosDeVenta = ['ADMSOFT', 'ALOHA', 'CHEF', 'FRONTR', 'MPRO', 'PIXEL', 'SOFT', 'SQUIRREL']

for _ in range(num_entries):
    # Generate fake data
    data = {"Nombre": fake.company(), "Latitud": fake.latitude(),
            "Longitud": fake.longitude(),
            "Direccion": fake.address(), "LinkFacebook": fake.url(),
            "Estado": fake.random_element(elements=('ACTIVO', 'INACTIVO')),
            "Imagen": fake.image_url(),
            "CuentaId": random.randint(1, 100),  # Assuming you have 100 accounts
            "ImporteMinimoNot": random.randint(1, 10) * 100,
            "Punto": fake.random_element(elements=PuntosDeVenta),
            "Version": fake.random_number(digits=2, fix_len=True),
            "Tipo": fake.random_element(elements=('COMPLETA', 'DEMO')),
            "NotificaAperturaYCierre": fake.random_element(elements=(True, False)),
            "VersionGuru": fake.random_number(digits=2, fix_len=True),
            "FechaInicio": fake.date_between(start_date='-1y', end_date='today'),
            "FechaFinal": fake.date_between(start_date='today', end_date='+1y'),
            "Actualizar": fake.random_element(elements=(True, False)),
            "Reprocesar": fake.random_element(elements=(True, False)),
            "HoraEnvioCorte": fake.date_time_this_year(),
            "ultimaActualizacion": fake.date_time_this_year(),
            "InicioTurno": fake.time(), "FinTurno": fake.time(),
            "InicioSemana": 1,
            "DiasSemana": 7,
            "FechaIReprocesar": fake.date_time_this_year(),
            "FechaFReprocesar": fake.date_time_this_year(),
            "Mesas": random.randint(1, 20),
            "Huespedes": random.randint(1, 100),
            "MostrarImporteSinIVA": fake.random_element(elements=(True, False)),
            "cultureinforegional": fake.language_code(),
            "MonitoreoActividad": fake.random_element(elements=(True, False)),
            "TiempoInactivo": random.randint(1, 120),
            "colorActividad": fake.color_name(),
            "bloqueaUpload": random.randint(1, 10),
            "mostrarceros": fake.random_element(elements=(True, False)),
            "Acceso": fake.random_number(digits=5, fix_len=True),
            "MonitorVenta": fake.random_element(elements=(True, False)),
            "FechaAlta": fake.date_between(start_date='-1y', end_date='today'),
            "PagoAutomatico": fake.random_number(digits=2, fix_len=True),
            "DiaPagoAutomatico": fake.day_of_month(),
            "AlmacenID": fake.random_number(digits=5, fix_len=True),
            "ExcluirProductos": fake.random_number(digits=5, fix_len=True),
            "KitchenEnTiempo": random.randint(1, 120),
            "KitchenRetrasoG": random.randint(1, 120),
            "MostrarEnKitchen": fake.random_element(elements=(True, False)),
            "CurrencyName": fake.currency_code(),
            "CategoriasPromo": fake.random_number(digits=5, fix_len=True)}
    # SQL INSERT INTO statement
    insert_query = """INSERT INTO public.sucursales 
    (
    "Nombre",
    "Latitud",
    "Longitud",
    "Direccion",
    "LinkFacebook",
    "Estado",
    "Imagen",
    "CuentaId",
    "ImporteMinimoNot",
    "Punto",
    "Version",
    "Tipo",
    "NotificaAperturaYCierre",
    "VersionGuru",
    "FechaInicio",
    "FechaFinal",
    "Actualizar",
    "Reprocesar",
    "HoraEnvioCorte",
    "ultimaActualizacion",
    "InicioTurno",
    "FinTurno",
    "InicioSemana",
    "DiasSemana",
    "FechaIReprocesar",
    "FechaFReprocesar",
    "Mesas",
    "Huespedes",
    "MostrarImporteSinIVA",
    "cultureinforegional",
    "MonitoreoActividad",
    "TiempoInactivo",
    "colorActividad",
    "bloqueaUpload",
    "mostrarceros",
    "Acceso",
    "MonitorVenta",
    "FechaAlta",
    "PagoAutomatico",
    "DiaPagoAutomatico",
    "AlmacenID",
    "ExcluirProductos",
    "KitchenEnTiempo",
    "KitchenRetrasoG",
    "MostrarEnKitchen",
    "CurrencyName",
    "CategoriasPromo"
    )
    VALUES (
    %(Nombre)s,
	%(Latitud)s,
	%(Longitud)s,
	%(Direccion)s,
	%(LinkFacebook)s,
	%(Estado)s,
	%(Imagen)s,
	%(CuentaId)s,
	%(ImporteMinimoNot)s,
	%(Punto)s,
	%(Version)s,
	%(Tipo)s,
	%(NotificaAperturaYCierre)s,
	%(VersionGuru)s,
	%(FechaInicio)s,
	%(FechaFinal)s,
	%(Actualizar)s,
	%(Reprocesar)s,
	%(HoraEnvioCorte)s,
	%(ultimaActualizacion)s,
	%(InicioTurno)s,
	%(FinTurno)s,
	%(InicioSemana)s,
	%(DiasSemana)s,
	%(FechaIReprocesar)s,
	%(FechaFReprocesar)s,
	%(Mesas)s,
	%(Huespedes)s,
	%(MostrarImporteSinIVA)s,
	%(cultureinforegional)s,
	%(MonitoreoActividad)s,
	%(TiempoInactivo)s,
	%(colorActividad)s,
	%(bloqueaUpload)s,
	%(mostrarceros)s,
	%(Acceso)s,
	%(MonitorVenta)s,
	%(FechaAlta)s,
	%(PagoAutomatico)s,
	%(DiaPagoAutomatico)s,
	%(AlmacenID)s,
	%(ExcluirProductos)s,
	%(KitchenEnTiempo)s,
	%(KitchenRetrasoG)s,
	%(MostrarEnKitchen)s,
	%(CurrencyName)s,
	%(CategoriasPromo)s
	)
	ON CONFLICT DO NOTHING;"""

    # Execute the SQL statement
    cursor.execute(insert_query, data)

# Commit the changes
connection.commit()

# Close the connection
cursor.close()
connection.close()
