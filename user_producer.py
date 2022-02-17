import requests
import os
from faker import Faker

def populate_user(auth, mem_ids, user_url):
    fake = Faker()
    
    # user_url = f"http://{user_url}/users/registration"
    user_url = "http://ad5bb2216daae4111b2251bab2e5effc-1860113579.us-east-1.elb.amazonaws.com:8003/users/registration"

    user_entries = len(mem_ids)
    for i in range(user_entries):
        user_info = {
            "role" : fake.random_element(elements=('admin','member')),
            "username" : fake.user_name(),
            "password" : fake.lexify('Aa1!?????'),
            "firstName" : fake.first_name(),
            "lastName" : fake.last_name(),
            "email" : fake.email(),
            "phone" : fake.numerify('(###)-###-####'),
            "membershipId" : mem_ids[i],
            "lastFourOfSSN" : str((i%10)+1)*4
        }

        try:
            reg_user = requests.post(user_url, json=user_info, headers=auth)
            print(reg_user)
            print(f"{user_info} \n")
        except Exception as e:
            pass

print('', end='')