from random import SystemRandom
from string import ascii_uppercase, ascii_lowercase, digits

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

while True:
    try:
        length = int(input('Password length: '))
        if length < 8:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Choose any number greater than 7")

more = 'Y'
while more.upper() != 'N':
    # Generate random password
    password = ''.join(SystemRandom().choices(
        ascii_uppercase + ascii_lowercase + digits, k=length))
    print(f'''
Here\'s your new password: {password}
    ''')
    more = input('Press N to quit and anything else for another password: ')
