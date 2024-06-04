import requests
from faker import Faker
import json
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()
# Initialize Faker
fake = Faker()

# Base URL
url = 'https://jimenezmiapi.somee.com/api/User'

# Headers
headers = {
    'accept': '*/*',
    'Content-Type': 'application/json-patch+json',
}

# Number of users to create
num_users = 400
startdate = datetime(2024, 1, 1)
for _ in range(num_users):
    # Generate fake data
    data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name(),
        "profileImage": fake.image_url(),
        "phoneNumber": fake.phone_number(),
        "description": fake.text(),
        "preferencias": fake.text(),
        "fechaCreacion": fake.date_between(start_date=startdate, end_date='today').strftime('%Y-%m-%d'),
        "rolId": 1,
        "status": True
    }

    # Send POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Print response
    print(response.status_code)