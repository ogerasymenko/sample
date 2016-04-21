#!/bin/bash -eux

apt-get update

apt-get -y upgrade

apt-get -y install linux-headers-$(uname -r)

apt-get -y -f install

cat <<EOF > /etc/init/refresh-apt.conf
description "update package index"
start on networking
task
exec /usr/bin/apt-get update
EOF

apt-get -y install curl
apt-get -y install mc

apt-get -y install rsync

apt-get -y install screen

apt-get -y install git

echo "UseDNS no" >> /etc/ssh/sshd_config
echo "GSSAPIAuthentication no" >> /etc/ssh/sshd_config
