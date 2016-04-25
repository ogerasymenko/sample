#!/bin/sh
THISHOST=$(hostname)
PATHTO="/mnt/backup/$THISHOST"
mkdir -p $PATHTO
NOW=$(date +"%F_%H:%M:%S")
tar zcf $PATHTO/etc_$NOW.tgz /etc
cd  $PATHTO"/.."
str="-name *.tgz -mtime +7 -delete"
find $str
