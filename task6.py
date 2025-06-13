import string
import random
size = int(input('Введите число: '))

def password():
    cahrs = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    return ''.join(random.choice(cahrs) for x in range(size))
print(password())