import requests
import os
from faker import Faker

def populate_branch(auth, branch_entries, branch_url):
    fake = Faker()
    # branch_url = f"http://{branch_url}/branches"
    branch_url = "http://ab4ef20023c80410ea31ac89ac53a044-299883019.us-east-1.elb.amazonaws.com:8002/branches"

    for i in range(branch_entries):
        branch_info = {
            "name" : fake.name(),
            "address" : fake.street_address(),
            "city" : fake.city(),
            "state" : fake.state(),
            "zipcode" : fake.numerify('#####'),
            "phone" : fake.numerify('(###)-###-####'),
            "bankID" : str(i+1)
        }

        try:
            reg_branch = requests.post(branch_url, json=branch_info, headers=auth)
            print(f"{branch_info} \n")
        except Exception as e:
            pass

print('', end='')