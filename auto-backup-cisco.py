#!/usr/bin/env python3

import datetime
from netmiko import ConnectHandler

router = {
    'router_type': 'cisco', 
    'host': '192.x.x.x',
    'username': 'admin',
    'password': 'xxxxxxx', 
}

def backup_configuration(device):
    try:
        net_connect = ConnectHandler(**device)
        
        now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        
        running_config = net_connect.send_command('show running-config')
        
        backup_filename = f"{device['host']}_running_config_{now}.txt"
        
        with open(backup_filename, 'w') as backup_file:
            backup_file.write(running_config)
        
        print(f"Configuration backup successful: {backup_filename}")
        
        net_connect.disconnect()
        
    except Exception as e:
        print(f"Failed to backup configuration: {e}")

backup_configuration(device) 
