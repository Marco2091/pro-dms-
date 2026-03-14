import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == '__main__':
    password_length = 12  # Default password length
    new_password = generate_password(password_length)
    print(f'Generated password: {new_password}')