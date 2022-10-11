from msilib.schema import Feature
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fourth_project.settings")

import django
django.setup()

from faker import Faker
from app_one.models import Users

faak = Faker()

def populate(N = 5):

    for _ in range(N):
        fake_first_name = faak.first_name()
        fake_last_name = faak.last_name()
        fake_email = faak.email()

        user = Users.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email = fake_email)[0]

if __name__ == "__main__":
    print("Populating!!")
    populate(20)
    print("Populated!!")