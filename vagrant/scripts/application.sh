#!/bin/bash -eux

apt-get -y install nginx
sed -i -e '0,/root \/usr\/share\/nginx\/html/s//root \/home\/vagrant\/html/' /etc/nginx/sites-available/default

apt-get -y install git

apt-get remove --purge node

curl -sL https://deb.nodesource.com/setup | bash -

apt-get -y install nodejs

apt-get -y install libfontconfig1 fontconfig libfontconfig1-dev libfreetype6-dev

apt-get -y install ruby

gem install sass

npm install -g grunt-cli

npm install -g lru-cache sigmund
npm install -g accepts batch
npm install -g qunitjs

service nginx reload

echo 'Environment is ready, you should fork and clone the repo now.'