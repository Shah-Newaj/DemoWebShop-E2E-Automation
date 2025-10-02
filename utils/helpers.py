import random
import string

def random_email():
    domain = "example.com"
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{user}@{domain}"
