import csv
import random
from faker import Faker

fake = Faker()
num_of_users = 100

fieldnames = ['username', 'display name', 'first name', 'last name', 'email', 'alternate emails', 'phone number', 'mobile number', 'street address', 'city', 'state/province', 'zip/postal code', 'country', 'company', 'department', 'title', 'birthdate', 'custom1', 'custom2', 'custom3', 'password', 'otp', 'otp-only', 'groups']

with open('users.csv', mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #writer.writeheader()
    for i in range(num_of_users):
        username = fake.user_name()
        display_name = fake.name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        alternate_emails = [fake.email() for _ in range(random.randint(0, 3))]
        phone_number = "+1-4257772222"
        mobile_number = "+1-4257772222"
        street_address = fake.street_address()
        city = fake.city()
        state_province = fake.state()
        zip_postal_code = fake.zipcode()
        country = fake.country()
        company = fake.company()
        department = fake.job()
        title = fake.job()
        birthdate = fake.date_of_birth().strftime('%Y-%m-%d')
        custom1 = ""
        custom2 = ""
        custom3 = ""
        password = fake.password(length=10)
        otp = ""
        otp_only = ""
        groups = "testgroup"
        writer.writerow({'username': username, 'display name': display_name, 'first name': first_name, 'last name': last_name, 'email': email, 'alternate emails': ';'.join(alternate_emails), 'phone number': phone_number, 'mobile number': mobile_number, 'street address': street_address, 'city': city, 'state/province': state_province, 'zip/postal code': zip_postal_code, 'country': country, 'company': company, 'department': department, 'title': title, 'birthdate': birthdate, 'custom1': custom1, 'custom2': custom2, 'custom3': custom3, 'password': password, 'otp': otp, 'otp-only': otp_only, 'groups': groups})