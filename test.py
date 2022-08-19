import ctypes

import netmiko
import textfsm
import os
import pandas
from ntc_templates.parse import parse_output
#
#
# file1 = open(r'D:\PyCharmProjects\vlan_mac_compiler\files\StandbySupervisor.txt').read()
#
# os.environ["NTC_TEMPLATES_DIR"] = r'D:\PyCharmProjects\vlan_mac_compiler\NTC_TEMPLATES'
# output = parse_output(command='show mac address vlan 205', data=file1, platform='cisco_ios')
# df = pandas.DataFrame(output)
# print(df)

command = "23434"
ctypes.windll.kernel32.SetConsoleTitleW(command)
