#!/usr/bin/python3
# A fabfile that distributes an archive to your web servers

from fabric.api import run, env, put
import os.path


env.hosts = ['44.210.147.177', '3.83.35.191']
# Set the username
env.user = "ubuntu"
# Set the keyfile
env.key_filename = '~/.ssh/id_rsa'


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
