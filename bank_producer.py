import requests
import os
from faker import Faker

def populate_bank(auth, bank_entries, bank_url):
    fake = Faker()

    # bank_url = f'http://{bank_url}/banks'
    bank_url = "http://ab4ef20023c80410ea31ac89ac53a044-299883019.us-east-1.elb.amazonaws.com:8002/banks"

    for i in range(bank_entries):
        bank_info = {
            "routingNumber" : fake.numerify('#########'),
            "address" : fake.street_address(),
            "city" : fake.city(),
            "state" : fake.state(),
            "zipcode" : fake.numerify('#####')
        }

        try:
            reg_bank = requests.post(bank_url, json=bank_info, headers=auth)
            print(f"{bank_info} \n")
        except Exception as e:
            pass

print('', end='')