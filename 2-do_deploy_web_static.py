#!/usr/bin/python3

from datetime import datetime
from fabric.api import env, local, run, put
import os

env.hosts = ['107.22.143.53', '18.210.14.41']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        archive_name = os.path.basename(archive_path)
        put(archive_path, "/tmp/{}".format(archive_name))
        run("mkdir -p /data/web_static/releases/{}/".format(
            archive_name[:-4]))
        run("tar -xzf /tmp/{} --strip-components=1 -C /data/web_static/releases/{}/".format(
            archive_name, archive_name[:-4]))
        run("rm /tmp/{}".format(archive_name))
        new_dir = "/data/web_static/releases/{}/".format(archive_name[:-4])
        run("rm -rf /data/web_static/current")
        ln_dir = "/data/web_static/current"
        run("ln -s /data/web_static/releases/{}/ {}".format(
             archive_name[:-4], ln_dir))
        return True
    except Exception:
        return False
