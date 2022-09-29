#!/usr/bin/python3
# A fabfile that creates and distributes an archive to your web servers

from fabric.api import env, run, put, local
import os
from datetime import datetime

env.hosts = ['44.210.147.177', '3.83.35.191']


def do_pack():
    """
    A function to package the contents of AirBnB Clone repo
    """
    now = datetime.now()
    archive_name = 'web_static_{}{}{}{}{}{}'.format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    local('mkdir -p versions')
    if local('cd web_static && tar -cvzf ../versions/{}.tgz . && cd -'.format(
            archive_name)).succeeded:
        return('versions/{}.tgz'.format(archive_name))


def do_deploy(archive_path):
    """
    Deploys archived files to web servers
    """

    if os.path.exists(archive_path) is False:
        return False
    com_file = archive_path.split("/")[-1]
    file = com_file.split(".")[0]
    if put(archive_path, '/tmp/').failed:
        return False
    if run('mkdir -p /data/web_static/releases/{}/'.format(file)).failed:
        return False
    if run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            com_file, file)).failed:
        return False
    if run('rm -rf /tmp/{}'.format(com_file)).failed:
        return False
    if run('rm -rf /data/web_static/current').failed:
        return False

    if run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
           format(file)).failed:
        return False
    return True


def deploy():
    """
    creates and deploys an archive to your web servers
    """
    path = do_pack()
    if path is None:
        return False

    return(do_deploy(path))
