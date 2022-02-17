import requests
import os
from faker import Faker

def populate_applicant(auth, applicant_url):
    fake = Faker()
    mem_id_array = []
    acc_num_array = []
    # applications_url = f"http://{applicant_url}/applications"
    applications_url = "http://a1910778a353e42239ddda8b500b9f6a-88828737.us-east-1.elb.amazonaws.com:8001/applications"
    
    application_type = fake.random_element(elements=('CHECKING', 'SAVINGS'))
    applicant_info = {
        "applicationType" : application_type,
        "noApplicants" : False,
        "applicants" : [{
            "address" : fake.street_address(),
            "city" : fake.city(),
            "dateOfBirth" : fake.numerify('19##-0%-1#'),
            "driversLicense" : fake.numerify('#########'),
            "email" : fake.email(),
            "firstName" : fake.first_name(),
            "gender" : fake.random_element(elements=('MALE','FEMALE', 'OTHER', 'UNSPECIFIED')),
            "income" : fake.numerify('#%#######'),
            "lastName" : fake.last_name(),
            "mailingAddress" : fake.street_address(),
            "mailingCity" : fake.city(),
            "mailingState" : fake.state(),
            "mailingZipcode" : fake.zipcode(),
            "middleName" : fake.first_name(),
            "phone" : fake.numerify('(###)-###-####'),
            "socialSecurity" : fake.ssn(),
            "state" : fake.state(),
            "zipcode" : fake.zipcode()
        }]
    }

    try:
        reg_app = requests.post(applications_url, json=applicant_info, headers=auth)
        print(reg_app)
        print(reg_app.json())
        print(f"{applicant_info} \n")
        mem_id_array.append(reg_app.json()['createdMembers'][0]['membershipId'])
        if application_type != 'CREDIT_CARD':
            acc_num_array.append(reg_app.json()['createdAccounts'][0]['accountNumber'])
    except Exception as e:
        pass

    return [mem_id_array, acc_num_array]

print('', end='')