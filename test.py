import ctypes

import netmiko
import textfsm
import os
import pandas
from ntc_templates.parse import parse_output
#
#
file1 = open(r'D:\PyCharmProjects\vlan_mac_compiler\files\show vrf.txt').read()

# os.environ["NTC_TEMPLATES_DIR"] = r'D:\PyCharmProjects\vlan_mac_compiler\NTC_TEMPLATES'
output = parse_output(command='show vrf', data=file1, platform='cisco_ios')
df = pandas.DataFrame(output)
vrf_dict = dict()
i = 1
for vrf in df['name']:
    vrf_dict.update({i: vrf})
    print(vrf_dict.get(i))
    i += 1

# command = "23434"
# ctypes.windll.kernel32.SetConsoleTitleW(command)
