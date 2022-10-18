import os
import re

from cisco_functions import CiscoDataHandler

dev_info = {
    'device_type': 'cisco_ios',
    'host': '192.168.254.28',
    'username': '********',
    'password': '********',
    'secret': '********',
    'timeout': 10,
    'fast_cli': False
}


def execute():
    c = CiscoDataHandler()

    print(f'Текущий ip-адрес: {dev_info.get("host")}. Изменить?\n Y - да, N - нет')
    ch = input()
    if ch == 'Y' or ch == 'y' or ch == 'ye' or ch == 'yes':
        print('Введи новый ip-адрес устройства:')

        address = input()

        while not re.match('(\d+\.){3}\d+', address):
            print('Введеный хост не подходит паттерну: 0-255.0-255.0-255.0-255')
            address = input()
        else:
            print(f'Назначен новый адрес хоста: {address}')
            dev_info['host'] = address

    c.get_info(dev_info)


# os.environ["NTC_TEMPLATES_DIR"] = os.getcwd() + '\\NTC_TEMPLATES'


if (
        dev_info['username'] == '********' or
        dev_info['password'] == '********' or
        dev_info['secret'] == '********'
):
    print("Введи логин")
    dev_info['username'] = input()
    print("...и пароль:")
    password = input()
    dev_info['password'] = password
    dev_info['secret'] = password
    execute()
else:
    execute()
