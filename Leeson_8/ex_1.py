import re

def mail_plz(mail):
    #Прересмотреть другие способы
    re_email = re.compile("(?:@|^)[^@]*")
    if not re_email.match(mail):
        raise ValueError(f'rong email: {mail}')
    a = re_email.findall(mail)
    result = dict([a])
    print(result)


for i in ['someone@geekbrains.ru', 'someone@geekbrainsru']:
    try:
        mail_plz(i)
    except ValueError as err:
        print(err)
