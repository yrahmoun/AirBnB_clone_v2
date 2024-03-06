#!/usr/bin/python3
"""distributes an archive to your web servers"""
from fabric.api import env, put, sudo
from os.path import exists

env.hosts = ['34.224.5.162', '54.165.200.8']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        folder = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        sudo('mkdir -p {}{}/'.format(path, folder))
        sudo('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, folder))
        sudo('rm /tmp/{}'.format(filename))
        sudo('mv {0}{1}/web_static/* {0}{1}/'.format(path, folder))
        sudo('rm -rf {}{}/web_static'.format(path, folder))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}{}/ /data/web_static/current'.format(path, folder))
        return True
    except Exception:
        return False
