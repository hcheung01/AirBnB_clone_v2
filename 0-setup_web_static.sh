#!/usr/bin/env bash
# setups web servers for deployment of web_static
service nginx status
if [ $? -eq 1 ]; then
    WHERE="/etc/nginx/sites-available/default"
    ADD="\\\tlocation \/redirect_me {\n\t\treturn 301 http://heindrickcheung.site;\n\t}\n"
    E404="\\\n\terror_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t}\n"
    apt-get update && apt-get install -y nginx
    apt-get update && apt-get upgrade -y
    echo "Holberton School" | sudo tee /usr/share/nginx/html/index.html
    sed -i "30i $ADD" $WHERE
    echo -e "Ceci n'est pas une page\n" | sudo tee /usr/share/nginx/html/custom_404.html
    sed -i "48i $E404" $WHERE
fi
cp /etc/nginx/sites-available/default{,.orig}
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "hello" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
ADD2="\\\n\tlocation = /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sed -i "54i $ADD2" $WHERE
service nginx restart
