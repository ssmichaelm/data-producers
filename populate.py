import requests, json

from applicant_producer import populate_applicant
from bank_producer import populate_bank
from branch_producer import populate_branch
from transaction_producer import populate_transaction
from user_producer import populate_user

with open("config.json", "r") as f:
    endpoint = json.load(f)
url = endpoint["url"]
user_port = endpoint["user_port"]
bank_port = endpoint["bank_port"]
transaction_port = endpoint["transaction_port"]
underwriter_port = endpoint["underwriter_port"]

iterations = int(input("Enter the number of iterations: "))

login_info = {
    'username' : 'michael',
    'password' : 'Aaa123!!'
}

login_url = f"http://ad5bb2216daae4111b2251bab2e5effc-1860113579.us-east-1.elb.amazonaws.com:8003/login"

login_response = requests.post(login_url, json=login_info)
bearer_token = login_response.headers['Authorization']
auth = {'Authorization' : bearer_token}

# Populate the database
for i in range (iterations):
    print(f"Bank generating...")
    populate_bank(auth, 1, f'{url}:{bank_port}')
    print(f"Branch generating...")
    populate_branch(auth, 1, f'{url}:{bank_port}')
    print(f"Application generating...")
    app_out = populate_applicant(auth, f'{url}:{underwriter_port}')
    print(app_out)
    print("User generating...")
    populate_user(auth, app_out[0], f'{url}:{user_port}')
    print("Transaction generating...")
    populate_transaction(auth, app_out[1], f'{url}:{transaction_port}')

