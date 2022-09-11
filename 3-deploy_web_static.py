#!/usr/bin/python3
from fabric.api import run, env, put, local
from os import path
from time import strftime


env.hosts = ['18.215.143.86', '50.19.37.76']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    """Fabric script that distributes an archive to your web servers"""
    if not path.exists(archive_path):
        return False

    try:
        file = archive_path.split('/')[1]
        # print(f'filename with extension .tgz : {file}')
        filename = file.split('.')[0]
        # print(f'just the filename  : {filename}')
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(filename))
        run('tar -zxvf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file, filename))
        run('rm /tmp/{}'.format(file))
        run('mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/'.format(filename, filename))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(filename))
        print('New version deployed!')
        return True
    except Exception as e:
        return False


def deploy():
    """Fabric script that creates and distributes an archive to your
    web servers, using the function deploy"""

    file_path = do_pack()
    if not file_path:
        return False

    return do_deploy(file_path)
