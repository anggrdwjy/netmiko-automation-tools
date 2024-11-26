#!/usr/bin/env python3

from netmiko import ConnectHandler

router = {
    'router_type': 'cisco', 
    'host': '192.x.x.x',
    'username': 'admin',
    'password': 'xxxxxxx', 
}

def troubleshoot_device(device):
    try:
        net_connect = ConnectHandler(**device)
        
        commands = [
            'show ip interface brief',  # Check interface statuses
            'show ip route',  # Check routing table
            'show interfaces status',  # Check detailed interface status
            'ping 8.8.8.8',  # Ping to an external address
            'traceroute 8.8.8.8',  # Traceroute to an external address
            'show logging | include ERR',  # Check for errors in logs
        ]
        
        troubleshoot_results = {}

        for command in commands:
            output = net_connect.send_command(command)
            troubleshoot_results[command] = output
        
        net_connect.disconnect()
        
        for command, output in troubleshoot_results.items():
            print(f"Command: {command}\n")
            print(f"Output:\n{output}\n")
            print("="*50)
        
        for command, output in troubleshoot_results.items():
            if 'ping' in command and '0 packets received' in output:
                print("Warning: Ping to external address failed!")
            if 'show ip interface brief' in command and 'down' in output:
                print("Warning: Some interfaces are down!")
        
        print("Troubleshooting completed successfully.")
        
    except Exception as e:
        print(f"Failed to troubleshoot device: {e}")

troubleshoot_device(device)
