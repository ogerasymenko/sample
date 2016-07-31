'''
program to display information about 
system memory and disk usage
before use it install psutil module:
pip install psutil
'''

import psutil
import sys
import os
import time
import socket
from datetime import datetime


def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))


def disk_usage():
    templ = "%-10s %7s %7s %7s %6s%% %7s  %s"
    print('-----------')
    print('DISK INFO\n-----------')
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                   "Mount"))
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue
        usage = psutil.disk_usage(part.mountpoint)
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))


def users():
    print('-----------')
    print('LOGINED USERS\n-----------')
    users = psutil.users()
    for user in users:
        print("%-12s %-7s %s  (%s)" % (
            user.name,
            user.terminal or '-',
            datetime.fromtimestamp(user.started).strftime("%Y-%m-%d %H:%M"),
            user.host))
    print('-----------')


def main():
    print('-----------')
    print('HOSTNAME\n-----------\n', socket.getfqdn(), sep='')
    print('-----------')
    print('MEMORY INFO\n-----------')
    pprint_ntuple(psutil.virtual_memory())
    print('-----------')
    print('SWAP INFO\n-----------')
    pprint_ntuple(psutil.swap_memory())


if __name__ == '__main__':
    main()
    disk_usage()
    users()
