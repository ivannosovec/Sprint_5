import random


class PersonData:
    user_name = 'Ivan_yandex'
    login = 'ivanyandex@test.ru'
    password = 'Qpromes15'


class ValidData:
    user_name = 'Spartak1'
    login = f"Tfootball{random.randint(10, 999)}@yandex.ru"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"