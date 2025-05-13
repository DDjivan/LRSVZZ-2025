from requests import post
from socket import gethostname, gethostbyname
from os import getlogin
from time import sleep



def send_three_data(sIPaddress:str) -> None :
    url = f'http://{sIPaddress}:50000/update_ip'

    hostname   = gethostname()  # get hostname
    username   = getlogin()  # get username
    ip_address = gethostbyname(hostname)  # get current IP address

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
