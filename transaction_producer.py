import requests
import os
from faker import Faker

def populate_transaction(auth, acc_nums, transaction_url):
    fake = Faker()
    # transaction_url = f"http://{transaction_url}/transactions"
    transaction_url = "http://a8b0ff0b530704ed5801cafdddecde33-1284104502.us-east-1.elb.amazonaws.com:8004/transactions"

    transaction_entries = len(acc_nums)
    for i in range(transaction_entries):
        transaction_info = {
            "amount" : fake.numerify('#####'),
            "date" : fake.numerify('201#-0%-1#'),
            "initialBalance" : fake.numerify('####'),
            "method" : fake.random_element(elements=('ACH','ATM','CREDIT_CARD','DEBIT_CARD','APP')), 
            "merchantCode" : '1111',
            "type" : fake.random_element(elements=('WITHDRAWAL','TRANSFER_OUT','TRANSFER_IN','DEPOSIT')),
            "accountNumber" : acc_nums[i]
        }

        if transaction_entries == 0:
            print("Application type was credit card, so no transaction created.")
        else:
            try:
                reg_trans = requests.post(transaction_url, json=transaction_info, headers=auth)
                print(reg_trans)
                print(f"{transaction_info} \n")
            except Exception as e:
                print(e)

print('', end='')