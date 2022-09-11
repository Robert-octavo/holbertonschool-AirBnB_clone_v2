# script that sets up your web servers for the deployment of web_static

exec { 'update'
  command => 'sudo apt-get update',
}

-> exec {'install nginx':
  command => 'sudo apt-get -y install nginx',
}

-> exec {'test-dir':
  command => 'sudo mkdir -p /data/web_static/releases/test/',
}

-> exec {'shared-dir':
  command => 'sudo mkdir -p /data/web_static/shared/',
}

-> exec {'index':
  command => 'sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html',
}

-> exec {'symbolic-link':
  command => 'sudo ln -sf /data/web_static/releases/test /data/web_static/current',
}

-> exec {'server-location':
  command => 'sudo sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}

-> exec {'restart':
  command => 'sudo service nginx restart',
}

-> exec {'grant':
  command => 'sudo chown -R ubuntu:ubuntu /data',
}
