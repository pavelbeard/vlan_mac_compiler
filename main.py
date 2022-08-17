import sys
import preproc
import os
from cisco_functions import CiscoDataHandler

os.environ["NTC_TEMPLATES_DIR"] = os.getcwd() + '\\NTC_TEMPLATES'

dev_info = {
    'device_type': 'cisco_ios',
    'host': '192.168.254.28',
    'username': 'borodinpa',
    'password': '1qaz@WSX',
    'secret': '1qaz@WSX',
    'timeout': 10,
    'fast_cli': False
}

c = CiscoDataHandler()
c.get_info(dev_info)
