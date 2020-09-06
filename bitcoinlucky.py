from bitcoin import *
import requests
import json

m = open('privkey.txt', 'a')
def gen_priv_key():
    my_private_key = random_key()
    print(my_private_key)
    my_pub_key = privkey_to_pubkey(my_private_key)
    my_adrr = privkey_to_address(my_private_key)
    print(my_pub_key)
    print(my_adrr)
    r = requests.get(f'https://chain.api.btc.com/v3/address/{my_adrr}?')
    todos = json.loads(r.text)
    bal = todos.get('balance')
    if bal != None:
        print("T'es Riche Mgl")
        m.write(my_private_key)
        m.write(bal)
        m.write(my_adrr)
        m.close()
while True:
    gen_priv_key()
