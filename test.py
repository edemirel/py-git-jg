# coding: utf-8
import os
# import pymssql
import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open(r'config'))

server = config.get('login', 'server')
user = 'steelseries\{0}'.format(config.get('login', 'username'))
password = config.get('login', 'password')

source_folder = '.\output\John Galt'
for the_file in os.listdir(source_folder):
     if the_file.split('.')[-1] == 'sql':
        print "oya"
