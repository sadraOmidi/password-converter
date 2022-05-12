from hashlib import sha256
import json


class PasswordHasher:
    def __init__(self):
        pass

    # create dictionary (key=password , value=password hash) in json file
    with open('hashed_password.json', 'w') as h:
        for i in range(10000):
            number = str(i)
            if len(number) <= 4:
                number = ''.join(((4 - len(number)) * '0', number))
            PASSWORD_HASH = {number: sha256(number.encode('utf-8')).hexdigest()}
            h.write(json.dumps(PASSWORD_HASH) + '\n')

    def hash_converter(self, user_hash_input):
        with open('hashed_password.json', 'r') as reader:
            for line in reader.readlines():
                line = json.loads(line)
                if user_hash_input == list(line.values())[0]:
                    return f'your password is : {list(line.keys())[0]}'

    def password_converter(self, user_password_input):
        for i in range(10000):
            if len(user_password_input) > 4:
                return 'Your input is more than 4 characters.'
            number = str(i)
            if len(user_password_input) <= 4:
                number = ''.join(((4 - len(user_password_input)) * '0', user_password_input))
            PASSWORD_HASH = sha256(number.encode('utf-8')).hexdigest()

        return f'your password hash is : {PASSWORD_HASH}'
