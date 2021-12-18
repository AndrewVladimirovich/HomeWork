import re

def email_parseing(e_address):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(e_address):
        raise ValueError(f'wrong email: {e_address}')
    print(re_email.match(e_address).groupdict())

for k in ['username@mail.ru', 'usern&ame@mail.ru', 'username@mailru']:
    try:
        email_parseing(k)
    except ValueError as error:
        print(error)

