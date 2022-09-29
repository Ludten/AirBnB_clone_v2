#!/usr/bin/python3
# A fabfile that generates a .tgz archive from the contents of the web_static
# folder of your AirBnB Clone repo

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    A function to package the contents of AirBnB Clone repo
    """
    now = datetime.now()
    archive_name = 'web_static_{}{}{}{}{}{}'.format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    if local('tar -cvzf {}.tgz web_static'.format(archive_name)).succeeded:
        return('./{}.tgz'.format(archive_name))
