import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'



gp_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
gp_len = int(input('Какой длины должен быть пароль? '))
gp_digits = input('Включать ли в пароль цифры от 0 до 9? (да/нет) ')
gp_uppercase = input('Включать ли в пароль прописные буквы? (да/нет)  ')
gp_lowercase = input('Включать ли в пароль строчные буквы? (да/нет) ')
gp_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? (да/нет) ')
gp_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? (да/нет) ')

def is_valid(check):
    if check.lower().strip() == 'да' or check.lower().strip() == 'нет':
        return True
    else: return False


def gen_posword():

    chars = ''
    password_list = []


    if gp_digits.lower().strip() == 'да':
        chars += digits
        password_list.append(random.choice(digits))
    if gp_uppercase.lower().strip() == 'да':
        chars += uppercase_letters
        password_list.append(random.choice(uppercase_letters))
    if gp_lowercase.lower().strip() == 'да':
        chars += lowercase_letters
        password_list.append(random.choice(lowercase_letters))
    if gp_punctuation.lower().strip() == 'да':
        chars += punctuation
        password_list.append(random.choice(punctuation))

    while len(password_list) < gp_len:
        if gp_exceptions.lower().strip() == 'да':
            for i in password_list:
                if i in 'il1Lo0O':
                    password_list.remove(i)
        password_list.append(random.choice(chars))
    random.shuffle(password_list)

    new_password = ''.join(password_list)

    return new_password

for _ in range(gp_quantity):
    print(gen_posword())