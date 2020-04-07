#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install nginx -y
service nginx start
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>\n\t<head>\n\t</head>\n\t<body>\n\tHolberton School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i "s/server_name _;/server_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n/" /etc/nginx/sites-available/default
service ngnix start
exit 0
