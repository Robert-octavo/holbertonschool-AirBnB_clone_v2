# script that sets up your web servers for the deployment of web_static

exec { 'update'
  provider => shell,
  command  => 'sudo apt-get update',
}

-> exec {'install nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
}

-> exec {'test-dir':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
}

-> exec {'shared-dir':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/shared/',
}

-> exec {'index':
  provider => shell,
  command  => 'sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html',
}

-> exec {'symbolic-link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test /data/web_static/current',
}

-> exec {'server-location':
  provider => shell,
  command  => 'sudo sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}

-> exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}

-> exec {'grant':
  provider => shell,
  command  => 'sudo chown -R ubuntu:ubuntu /data',
}
