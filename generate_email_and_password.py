import random
import string


def generate_random_email():
    domain = "@yandex.ru"
    username_length = random.randint(5, 10)
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))
    return username + domain

def generate_random_password():
    password = random.randint(100000, 999999)
    return password