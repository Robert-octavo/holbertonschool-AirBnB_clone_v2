#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """Fabric script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo"""
    file_date = strftime("%Y%m%d%H%M%S")
    file_name = 'web_static_' + file_date + '.tgz'
    try:
        local('mkdir -p versions')
        local('tar -czvf versions/{} web_static/'.format(file_name))

        return 'versions/{}'.format(file_name)
    except Exception as e:
        return None
