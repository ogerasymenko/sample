#!/bin/bash -eux

apt-get -y install nginx
# create jenkins and graphite config for nginx
cat <<EOF > /etc/nginx/sites-available/manage

    location  / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:3031;
    }

EOF


rm /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

ln -s /etc/nginx/sites-available/manage /etc/nginx/sites-enabled/

service nginx restart