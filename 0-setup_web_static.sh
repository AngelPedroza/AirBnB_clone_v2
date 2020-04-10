#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install nginx -y
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i "38i location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n/" /etc/nginx/sites-available/default
sudo service nginx start
