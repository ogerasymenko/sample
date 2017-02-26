#!/bin/bash

pwfile="/etc/passwd"
shadowfile="/etc/shadow"
gfile="/etc/group"
hdir="/home"
shell="/bin/bash"

if [ $# == 1 ]
then
  login=$1
  uid="$(awk -F: '{ if (big < $3 && $3 < 5000) big=$3 } END { print big + 1 }' $pwfile)"
  gid=$uid
  homedir=$hdir/$login
  mkdir $homedir
  echo ${login}:x:${uid}:${gid}:${login}:${homedir}:$shell >> $pwfile
  echo ${login}:*:11647:0:99999:7::: >> $shadowfile
  echo "${login}:x:${gid}:$login" >> $gfile
  cp -R /etc/skel/.[a-zA-Z]* $homedir
  chmod 750 $homedir
  chown -R ${login}:${login} $homedir
  exec passwd $login

elif [ $# == 2 ]
then
  groupmems -a $1 -g $2
  groupmems -g $2 -l

else
  echo "Usage: "
  echo "First argument  - 'username'. For add username as system user."
  echo "Second argument - 'username groupname'. For add username to groupname."
fi