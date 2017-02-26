#!/bin/sh

#Configure /etc/hosts file
echo "" | sudo tee --append /etc/resolv.conf 2> /dev/null && \
echo "nameserver 8.8.8.8" | sudo tee --append /etc/resolv.conf 2> /dev/null

# Configure /etc/puppetlabs/puppet/puppet.conf for add PuppetMaster
echo "" | sudo tee --append /etc/puppetlabs/puppet/puppet.conf 2> /dev/null && \
echo "[main]" | sudo tee --append /etc/puppetlabs/puppet/puppet.conf 2> /dev/null && \
echo "server = master" | sudo tee --append /etc/puppetlabs/puppet/puppet.conf 2> /dev/null && \
echo "environment = production" | sudo tee --append /etc/puppetlabs/puppet/puppet.conf 2> /dev/null && \
echo "runinterval = 1800s" | sudo tee --append /etc/puppetlabs/puppet/puppet.conf 2> /dev/null

# sudo source /vagrant/py_vars.sh

sudo /opt/puppetlabs/bin/puppet resource service puppet ensure=running enable=true 
sudo /opt/puppetlabs/bin/puppet agent -t
sudo /opt/puppetlabs/puppet/bin/puppet agent --daemonize


if [ $? -eq 2 ]
    then exit 0 
fi
