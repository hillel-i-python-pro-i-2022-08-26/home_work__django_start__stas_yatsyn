from faker import Faker

fake = Faker()


def get_random_user():
    return fake.first_name()
