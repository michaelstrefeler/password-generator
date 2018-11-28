from random import SystemRandom
from string import ascii_uppercase, ascii_lowercase, digits


def header():
    print('''
        ____                                          __
       / __ \____ ____________      ______  _________/ /
      / /_/ / __ `/ ___/ ___| | /| / / __ \/ ___/ __  /
     / ____/ /_/ (__  (__  )| |/ |/ / /_/ / /  / /_/ /
    /_/    \__,_/____/____/ |__/|__/\____/_/   \__,_/
       ______                           __
      / _______  ____  ___  _________ _/ /_____  _____
     / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
    / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /
    \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/
    ''')
    return 'It worked'


def generate_password():
    while True:
        try:
            length = int(input('Password length: '))
            if length < 8:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Choose any number greater than 7")

    more = 'continue'
    while more.upper() != 'Q':
        # Generate random password
        password = ''.join(SystemRandom().choices(
            ascii_uppercase + ascii_lowercase + digits, k=length))
        print(f'Here\'s your new password: {password}')
        more = input('Press Q to quit or anything to continue: ')


if __name__ == '__main__':
    header()
    generate_password()
