from netmiko import ConnectHandler


ip=input('Enter IP address: ')
username=input('Enter username: ')
password=input('Enter password: ')
port=input('Enter port number: ')

MT = {
    'device_type': 'mikrotik_routeros',
    'host': ip,
    'port': port,
    'username': username,
    'password': password
}

ssh = ConnectHandler(**MT)
print('Connected to {}.'.format(ip))


print("""
Commands:
1. Change Router's Identity
2. Control (Lan) interface up/downs
3. Control and change the ports of services (Telnet, ssh , web)
4. Disconnect
""")

while(True):
    choice=input('Enter command number:')

    if choice=="1":
        name=input("Enter new name: ")
        output = ssh.send_command(f'system identity set name={name}')
        output = ssh.send_command('system identity print')

    elif choice=="2":
        name=input("Enter LAN interface name: ")
        choicee=input("up(u) or down(d)?: ")
        if ed=='u':
                output = ssh.send_command(f'ip link set dev {name} up')
        if ed=='d':
                output = ssh.send_command(f'ip link set dev {name} down')
        else: print('Invalid input!')

    elif choice=="3":
        choicee=input("control port(1) or change port(2)?: ")
        serv=input(""" choose one:
            1.telnet
            2.ssh
            3.www
            """)
        if choicee=="1":
            ed=input("enable(e) or disable(d)?: ")
            if ed=='e':
                output = ssh.send_command(f'ip service enable {serv}')
            if ed=='d':
                output = ssh.send_command(f'ip service disable {serv}')
            else: print('Invalid input!')
        if choicee=="2":
            serv_port=input(f"Specify port number for service {serv}: ")
            output = ssh.send_command(f'ip service set {serv} port={serv_port}')
        else: print('Invalid input!')

    elif choice=="4":
        break
    
    else: print('Invalid input!')
    print(output)
