#!/usr/bin/python3
# A fabfile deletes out-of-date archives

from fabric.api import env, run, local

env.hosts = ['44.210.147.177', '3.83.35.191']
# Set the username
env.user = "ubuntu"
# Set the keyfile
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """
    deletes out-of-date archives
    """
    number = int(number)
    if number == 0 or number == 1:
        num = 2
    elif number >= 2:
        num = number + 1

    local(
        'cd versions && ls -t web_static_* | tail -n +{} | \
xargs rm -f -- && cd -'.format(num))
    run(
        'cd /data/web_static/releases && ls -t web_static_* | tail -n +{} | \
xargs rm -f -- && cd -'.format(num))
