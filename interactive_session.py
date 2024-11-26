#!/usr/bin/env python3

from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios', 
    'host': '192.168.204.131',
    'username': 'admin',
    'password': 'xxxxxxx', 
}

def interactive_session(device):
    try:
        net_connect = ConnectHandler(**device)
        
        print("Interactive SSH session established. Type 'exit' to end the session.")
        
        while True:
            command = input("Enter command: ")
            
            if command.lower() == 'exit':
                print("Exiting interactive session.")
                break
            
            output = net_connect.send_command(command)
            
            print(output)
        
        net_connect.disconnect()
        
    except Exception as e:
        print(f"Failed to establish interactive session: {e}")

interactive_session(device) 
