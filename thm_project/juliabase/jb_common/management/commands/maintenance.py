# This file is part of JuliaBase

"""Module which defines the command ``maintenance``.  It should be called
nightly as a cronjob.  For example, one line in the crontab may read::

    0 3 * * * /home/juliabase/juliabase/manage.py maintenance
"""

from django.core.management.base import BaseCommand
from jb_common.signals import maintain


class Command(BaseCommand):
    args = ""
    help = "Does database maintenance work.  It should be called nightly as a cronjob."

    def handle(self, *args, **kwargs):
        maintain.send(sender=Command)
