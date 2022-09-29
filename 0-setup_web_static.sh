#!/usr/bin/env bash
# Script for setting up web server
apt-get -y update
if ! dpkg -l | grep -q nginx
then
	apt-get -y install nginx
fi
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" | tee /data/web_static/releases/test/index.html > /dev/null
link="/data/web_static/current"
if [ ! -L "$link" ]
then
	ln -s /data/web_static/releases/test/ "$link"
else
	rm -f "$link"
	ln -s /data/web_static/releases/test/ "$link"
fi
chown -R ubuntu /data/
chgrp -R ubuntu /data/
sblock="server_name\ _;\\n\\n\\tlocation\ \/hbnb_static\/\ {\\n\\t\\talias\ \/data\/web_static\/current\/;\\n\\t}\\n"
sudo sed -i "s/server_name _;/$sblock/" /etc/nginx/sites-available/default
service nginx restart
exit 0
