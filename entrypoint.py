#!/usr/bin/python3

import os
import time
import sys
import re

os.chdir('/PrintABrick')

FLAG = "/initialized"

print('Waiting for db server')
time.sleep(20)


if os.path.exists(FLAG):
    print('Already initialized.')
else:
    print('Initializing...It may take an hour.')


    # set api keys
    brickset_api = os.getenv('BRICKSET_API')
    rebrickable_api = os.getenv('REBRICKABLE_API')

    if brickset_api == None or brickset_api == "":
        brickset_api = input('Enter your Brickset api key: ')

    if rebrickable_api == None or rebrickable_api == "":
        rebrickable_api = input('Enter your Rebrickable api key: ')

    os.system("sed -i -re 's/brickset_apikey: ~/brickset_apikey: %s/g' /PrintABrick/app/config/parameters.yml.dist" % brickset_api) 
    os.system("sed -i -re 's/rebrickable_apikey: ~/rebrickable_apikey: %s/g' /PrintABrick/app/config/parameters.yml.dist" % rebrickable_api) 


    ret = 0
    ret = os.system('php bin/console doctrine:database:create')
    ret += os.system('php bin/console doctrine:schema:create' )
    ret += os.system('php bin/console doctrine:fixtures:load -n')

    ret += os.system('php bin/console app:init')

    print(f'final return code = {ret}')

    #if ret != 0:
    #    print('Initialization has failed.')
    #    sys.exit(-1)        
    #else:
    #    os.system('touch ' + FLAG)
    with open(FLAG, 'w'):   pass


os.system('php bin/console server:run 0.0.0.0:8000')
