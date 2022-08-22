import ctypes

import netmiko
import textfsm
import os
import pandas
from netmiko import ConnectHandler
from ntc_templates.parse import parse_output
#
#
file1 = r'D:\PyCharmProjects\vlan_mac_compiler\files\show vrf.txt'

dev_info = {
    'device_type': 'cisco_ios',
    'host': '192.168.254.28',
    'username': '********',
    'password': '********',
    'secret': '********',
    'timeout': 10,
    'fast_cli': False
}

with ConnectHandler(**dev_info) as dev:
    dev.enable()

    with open('templates/show_vrf.template') as f:
        fsm = textfsm.TextFSM(f)
        output = fsm.ParseText(dev.send_command('show vrf'))
        df = pandas.DataFrame(output)

        vrf_dict = {}
        i = 1
        for vrf in df[0].tolist():
            vrf_dict.update({i: vrf})
            i += 1

        print(vrf_dict)
