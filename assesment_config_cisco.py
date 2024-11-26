#!/usr/bin/env python3
from netmiko import ConnectHandler

router = {
    'router_type': 'cisco', 
    'host': '192.x.x.x',
    'username': 'admin',
    'password': 'xxxxxxx', 
}

def security_audit(device):
    try:
        net_connect = ConnectHandler(**device)
        
        commands = [
            'show version',  # Check for software version
            'show running-config | include password',  # Check for password configurations
            'show running-config | include snmp',  # Check SNMP configurations
            'show running-config | include access-list',  # Check access control lists (ACLs)
            'show running-config | include ntp',  # Check NTP settings
            'show running-config | include logging',  # Check logging configurations
            'show running-config | include ssh',  # Check SSH configurations
            'show ip interface brief'  # Check interface statuses
        ]
        
        audit_results = {}

        for command in commands:
            output = net_connect.send_command(command)
            audit_results[command] = output
        
        net_connect.disconnect()
        
        for command, output in audit_results.items():
            print(f"Command: {command}\n")
            print(f"Output:\n{output}\n")
            print("="*50)
        
        for command, output in audit_results.items():
            if 'password' in command and 'password' not in output:
                print("Warning: No password configured!")
            if 'snmp' in command and 'public' in output:
                print("Warning: Default SNMP community string 'public' found!")
        
        print("Security audit completed successfully.")
        
    except Exception as e:
        print(f"Failed to perform security audit: {e}")

security_audit(device) 
