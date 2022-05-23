import string
import random

import faker


def get_user():
    fake = faker.Faker()
    name = fake.name().split()[0]
    surname = fake.name().split()[1]
    middle_name = fake.name().split()[0]
    username = "".join(random.choice(string.ascii_letters) for _ in range(14))
    email = fake.email()
    password = fake.password()
    return name, surname, middle_name, username, password, email
