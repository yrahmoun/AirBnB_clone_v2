#!/usr/bin/python3
"""creates and distributes an archive to web servers"""
from fabric.api import env, local, run
from datetime import datetime
from os.path import exists

env.hosts = ['34.224.5.162', '54.165.200.8']


def do_pack():
    """Creates the archive"""
    try:
        current_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        archive_path = 'versions/web_static_{}.tgz'.format(current_time)
        local('mkdir -p versions')
        local('tar -czvf {} web_static'.format(archive_path))
        return archive_path
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.
    """
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


def deploy():
    """
    deploy the web_static content to the web servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
