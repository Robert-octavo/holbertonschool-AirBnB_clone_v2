#!/usr/bin/python3
from fabric.api import run, env, put
from os import path


env.hosts = ['18.215.143.86', '50.19.37.76']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Fabric script that distributes an archive to your web servers"""
    if not path.exists(archive_path):
        return False

    try:
        file = archive_path.split('/')[1]
        # print(f'filename with extension .tgz : {file}')
        filename = file.split('.')[0]
        # print(f'just the filename  : {filename}')
        put(archive_path, "/tmp/")
        # print("Test put")
        run('mkdir -p /data/web_static/releases/{}'.format(filename))
        # print("Test First")
        run('tar -zxf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file, filename))
        # print("Test Second")
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
        # print(e)
        return False
