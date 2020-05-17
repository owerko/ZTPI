def create_url(host='localhost', port=443):
    adress = 'https://'+host+str(port)
    return adress

print(create_url())


