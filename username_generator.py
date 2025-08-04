import random
import string

def generate_username(length=5):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

# Generate 10 usernames
for i in range(10):
    print(generate_username())
