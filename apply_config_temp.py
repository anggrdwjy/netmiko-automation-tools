#!/usr/bin/env python3

from netmiko import ConnectHandler

devices =[
{
    'device_type': 'cisco_ios', 
    'host': '192.168.204.131',
    'username': 'admin',
    'password': 'xxxxxxx', 
}
# Add more devices as needed
]

# Configuration commands to apply
config_commands = [
    'interface GigabitEthernet0/1',
    'description Configured by Netmiko',
    'no shutdown',
    'exit',
    'ip domain-name labmachine.com',
]

def apply_configuration(device, commands):
    try:
        net_connect = ConnectHandler(**device)
        
        output = net_connect.send_config_set(commands)
        
        print(f"Configuration applied to {device['host']}:\n{output}")
        
        save_output = net_connect.save_config()
        print(f"Configuration saved on {device['host']}:\n{save_output}")
        
        net_connect.disconnect()
        
    except Exception as e:
        print(f"Failed to apply configuration to {device['host']}: {e}")

for device in devices:
    apply_configuration(device, config_commands) 
