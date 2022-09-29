#!/usr/bin/python3
# A fabfile that creates and distributes an archive to your web servers

from fabric.api import env
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['44.210.147.177', '3.83.35.191']
# Set the username
env.user = "ubuntu"
# Set the keyfile
env.key_filename = '~/.ssh/id_rsa'


def deploy():
    """
    creates and deploys an archive to your web servers
    """
    path = do_pack()
    if path is None:
        return False

    return(do_deploy(path))
