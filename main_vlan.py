import os

from cisco_functions import CiscoDataHandler


def execute():
    c = CiscoDataHandler()
    c.get_info(dev_info)


os.environ["NTC_TEMPLATES_DIR"] = os.getcwd() + '\\NTC_TEMPLATES'

dev_info = {
    'device_type': 'cisco_ios',
    'host': '192.168.254.28',
    'username': '********',
    'password': '********',
    'secret': '********',
    'timeout': 10,
    'fast_cli': False
}

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
