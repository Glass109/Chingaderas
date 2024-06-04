import psycopg2
from faker import Faker
import os
from dotenv import load_dotenv

# Initialize Faker
fake = Faker()
load_dotenv()
db_url = os.getenv("GURUAPP_DB_URL")
# Establish a connection to your database
connection = psycopg2.connect(db_url)
cursor = connection.cursor()

# Number of entries to create
num_entries = 100

for _ in range(num_entries):
    # Generate fake data
    data = {
        "RazonSocial": fake.company(),
        "RFC": fake.random_number(digits=12, fix_len=True),
        "Email": fake.company_email(),
        "FechaIngreso": fake.date_between(start_date='-1y', end_date='today'),
        "DiasCredito": 0,
        "Contacto1": fake.name(),
        "TelContacto1": fake.phone_number(),
        "EmailContacto1": fake.email(),
        "Estado": fake.random_element(elements=('ACTIVO', 'INACTIVO')),
        "Tipo": fake.random_element(elements=('COMPLETA', 'DEMO')),
        "Vendedor": fake.name(),
        "ValidarPago": "true",
        "DB": fake.random_number(digits=5, fix_len=True)
    }

    # SQL INSERT INTO statement
    insert_query = """INSERT INTO public.cuentas ("RazonSocial", "RFC", "Email", "FechaIngreso", "DiasCredito", "Contacto1", "TelContacto1", "EmailContacto1", "Estado", "Tipo", "Vendedor", "ValidarPago", "DB") 
                      VALUES (%(RazonSocial)s, %(RFC)s, %(Email)s, %(FechaIngreso)s, %(DiasCredito)s, %(Contacto1)s, %(TelContacto1)s, %(EmailContacto1)s, %(Estado)s, %(Tipo)s, %(Vendedor)s, %(ValidarPago)s, %(DB)s)
                      ON CONFLICT DO NOTHING;
                      """

    # Execute the SQL statement
    cursor.execute(insert_query, data)

# Commit the changes
connection.commit()

# Close the connection
cursor.close()
connection.close()
