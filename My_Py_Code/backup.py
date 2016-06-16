# To run this programm you need to create wp_backup.ini
# with following content:
# [your_site.name]
# www_data = '/var/www/html/wordpress'
# mysql_db = 'wordpress'
# mysql_host = 'localhost'
# mysql_user = 'wordpress'
# mysql_pass = 'wordpress'


from __future__ import print_function

import os
import datetime
import subprocess
import shutil
import configparser


TOOL_ROOT = '/home/sashko/Dev/MyCode'
BACKUPS_ROOT = os.path.join(TOOL_ROOT, 'backup')
WWW_BACKUPS_ROOT = os.path.join(BACKUPS_ROOT, 'www')
DB_BACKUPS_ROOT = os.path.join(BACKUPS_ROOT, 'db')
WEB_ROOT = '/var/www/html/wordpress/'

if os.access(BACKUPS_ROOT, os.F_OK) == False:
    os.mkdir('backup')

if os.access(WWW_BACKUPS_ROOT, os.F_OK) == False:
    os.mkdir(os.path.join(BACKUPS_ROOT, 'www'))

if os.access(DB_BACKUPS_ROOT, os.F_OK) == False:
    os.mkdir(os.path.join(BACKUPS_ROOT, 'db'))

config = os.path.join(TOOL_ROOT, 'wp_backup.ini')
parser = configparser.ConfigParser()

if len(parser.read(config)) == 0:
    raise Exception('ERROR: No config file {} found!'.format(config))


def www_backup(source_dir, output_file):

    shutil.make_archive(backup_name, 'zip', root_dir=WWW_BACKUPS_ROOT, base_dir=source_dir)

for section in parser.sections():

    print('Executing WWW data backup on: {}'.format(section))

    today = datetime.datetime.now().strftime('%d-%m-%Y-%H-%M')
    source_dir = parser.get(section, 'www_data').strip("\'")
    backup_name = os.path.join(WWW_BACKUPS_ROOT, section + '-' + today)

    www_backup(source_dir, backup_name)

    print('Executing MySQL data backup on: {}'.format(section))

    mysql_host = parser.get(section, 'mysql_host')
    mysql_db = parser.get(section, 'mysql_db')
    mysql_user = parser.get(section, 'mysql_user')
    mysql_pass = parser.get(section, 'mysql_pass')
    mysql_backup_file = os.path.join(DB_BACKUPS_ROOT, parser.get(section, 'mysql_db') + '-' + today + '.sql')

    print('Using: \nHOST: {}\nDB: {}\nUSER: {}\n'.format(mysql_host, mysql_db, mysql_user, mysql_pass))

    dump_cmd = ['mysqldump ' +
                '--user={mysql_user} '.format(mysql_user=mysql_user) +
                '--password={db_pw} '.format(db_pw=mysql_pass) +
                '--host={db_host} '.format(db_host=mysql_host) +
                '{db_name} '.format(db_name=mysql_db) +
                '> ' +
                '{filepath}'.format(filepath=mysql_backup_file)]

    dump = subprocess.Popen(dump_cmd, shell=True)
    dump.wait()
