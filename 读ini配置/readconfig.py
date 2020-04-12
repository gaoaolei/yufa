import os
import configparser
path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'a.ini')

con = configparser.ConfigParser()
con.read(path, encoding='utf-8')

weight = con.get('gal','weight')
print(weight)

