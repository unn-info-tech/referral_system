import random
import string

def generate_verification_code(length=4):
    characters = string.digits
    verification_code = ''.join(random.choice(characters) for _ in range(length))
    return verification_code
