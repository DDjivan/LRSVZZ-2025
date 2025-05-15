from requests import post
from socket import gethostname, gethostbyname
from socket import socket, AF_INET, SOCK_DGRAM
from os import getlogin
from time import sleep



def get_local_ip() -> str :
    try:
        # Create a UDP socket
        s = socket(AF_INET, SOCK_DGRAM)
        # s.bind(('', 0))  # Bind to all interfaces, port 0 (arbitrary) DOESN'T WORK
        s.connect(("1.1.1.1", 80))
        local_ip = s.getsockname()[0]  # Get the local IP address
        s.close()
        return local_ip

    except Exception as e :
        print(f"Error getting local IP: {e}")
        return "0.0.0.0"  # default value in case of error

def send_three_data(sIPaddress:str) -> None :
    url = f'http://{sIPaddress}:50000/update_ip'

    hostname   = gethostname()  # get hostname
    username   = getlogin()  # get username
    # get current IP address :
    # ip_address = gethostbyname(hostname)  # unfortunately, RPi4 assigns it to 127.0.1.1
    ip_address = get_local_ip()

    dict_to_send = {'ip': ip_address, 'hostname': hostname, 'username': username}

    try :
        response = post(url, data=dict_to_send)  # send the data to the server RPi 2

        print(f'Sent following data: IP address: {ip_address}, Hostname: {hostname}, Username: {username}')

        print(f'Response: {response.text}')

    except Exception as e :
        print(f'Error sending data: {e}')

    finally :
        print(" ")



if __name__ == '__main__' :
    rpi2_ip_local = '10.0.0.222'
    rpi2_ip_public = '90.22.255.6'

    while True:
        send_three_data(rpi2_ip_public)
        sleep(60)
