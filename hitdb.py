# coding: utf-8
from datetime import datetime as dt

import os
import pymssql
import subprocess
import ConfigParser
import re

config = ConfigParser.ConfigParser()
config.readfp(open(r'config'))

server = config.get('login', 'server')
user = 'steelseries\{0}'.format(config.get('login', 'username'))
password = config.get('login', 'password')

pattern = re.compile('CREATE VIEW\s[a-z]*\.[A-z]*\_[\w\d]*\r\nAS\s*\r\n')

source_folder = '.\output\John Galt'
for the_file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, the_file)
    try:
        if os.path.isfile(file_path) and the_file.split('.')[-1] == 'sql':
            os.unlink(file_path)
        # elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception, e:
        print e

with pymssql.connect(server, user, password, "EDW") as conn:
    with conn.cursor(as_dict=True) as cursor:
        cursor.execute("""
        SELECT  s.name AS SchemaName,
                v.name AS ViewName,
                sm.definition As [ViewDefinition]
        FROM    sys.views v
            INNER JOIN sys.schemas s ON s.schema_id = v.schema_id
            INNER JOIN sys.sql_modules sm ON sm.object_id = v.object_id
        WHERE   s.name = 'sandbox' AND
                v.name LIKE 'JG%'
        """)

        views = cursor.fetchall()
        # print views[0]['ViewDefinition']

for view in views:
    # try:
    #     print pattern.split(view['ViewDefinition'])[1]
    # except IndexError:
    #     print pattern.split(view['ViewDefinition'])
    #     input("Press Enter to continue...")
    with open('output/John Galt/{0}.sql'.format(view['ViewName']), 'wb') as the_file:
        the_file.write(pattern.split(view['ViewDefinition'])[1])

os.chdir("output/John Galt")
subprocess.call("git add *.sql", shell=True)
subprocess.call('git commit -m "{0}"'.format(dt.utcnow().strftime('Commited on %Y%m%d %H:%M UTC+0')), shell=True)
subprocess.call('git push -u origin sql01:sql01', shell=True)
