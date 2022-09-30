#!/usr/bin/env bash
# Script for setting up web server
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" | tee /data/web_static/releases/test/index.html > /dev/null
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sblock="server_name\ _;\\n\\n\\tlocation\ \/hbnb_static\/\ {\\n\\t\\talias\ \/data\/web_static\/current\/;\\n\\t}\\n"
sudo sed -i "s/server_name _;/$sblock/" /etc/nginx/sites-available/default
service nginx restart
