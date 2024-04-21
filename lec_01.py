from os import getcwd
currentWorkingDirectory = getcwd()
print(currentWorkingDirectory)

import configparser as cfgParser
config = cfgParser.ConfigParser()
config.read('"lec_01.ini')

print("Scetions inside of the config file:")
print(config.sections())
print("Defaults of the config")
print (config.defaults())

for key in config['DEFAULT']:
    print(key, ":=", config['DEFAULT'][key])

from universe import *
print (Feierabend)

