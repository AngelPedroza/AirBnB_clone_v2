#!/usr/bin/env python3
"""Create a folder if not exists and create a tgz
file with the local command execution with fabric"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ['35.237.103.2', '18.209.63.81']

def do_pack():
    """Create the folder and the tgz"""
    try:
        with hide('running'):
            local("mkdir versions")

        date = datetime.now()
        all_date = date.strftime("%Y%m%d%H%M%S")

        command = "tar -cvzf versions/web_static_{}.tgz web_static".format(all_date)
        path = "versions/web_static_{}.tgz".format(all_date)
        message = "Packing web_static to {}".format(path)

        print(message)
        local(command)

        with hide('running'):
            size = local('wc -c < {}'.format(path), capture=True)

        f_msg = "web_static packed: {} -> {}Bytes".format(path, size)

        with hide('running'):
            local("chmod 664 {}".format(path))

        print(f_msg)

        return path
    except:
        return None

def do_deploy(archive_path):
    """Run commands to remotly, pass a file and uncompress it"""
    if not os.path.isfile(archive_path):
        return False

    name = archive_path
    name = name.replace("/", " ")
    name = name.split()
    file_ext = name[-1]
    fname, exten = os.path.splitext(file_ext)

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}/".format(fname))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_ext,
                                                                       fname))
        run("sudo rm /tmp/{}".format(file_ext))
        run("sudo mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(fname, fname))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(fname))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(fname))

        print("New version deployed!")
        return True

    except:

        return False
