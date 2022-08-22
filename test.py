import ctypes

import netmiko
import textfsm
import os
import pandas
from ntc_templates.parse import parse_output
#
#
file1 = r'D:\PyCharmProjects\vlan_mac_compiler\files\show vrf.txt'

with open('templates/show_vrf.template') as f:
    fsm = textfsm.TextFSM(f)
    output = fsm.ParseText(open('files/show vrf.txt').read())
    df = pandas.DataFrame(output)

    vrf_dict = {}
    i = 1
    for vrf in df[0].tolist():
        vrf_dict.update({i: vrf})
        i += 1

    print(vrf_dict)
