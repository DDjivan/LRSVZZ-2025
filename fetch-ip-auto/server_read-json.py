from json import load



if __name__ == '__main__':
    with open('./tunnel/client_tunnelconfig.json') as file:
        config = load(file)

    print(config['PORT'])
    print(config['USERNAME'])
    print(config['ADDRESSEIP'])
