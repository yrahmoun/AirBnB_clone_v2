#!/usr/bin/python3
"""generates a .tgz archive from the the web_static folder"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive"""
    local("mkdir -p versions")
    time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(time)
    result = local("tar -czvf {} web_static".format(archive_path))
    if result.succeeded:
        return archive_path
    else:
        return None
