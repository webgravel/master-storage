import gravel_master

import graveldb
import re

PATH = '/gravel/system/master'

class Box(graveldb.Table('boxes', PATH)):
    default = dict(type=None, active=None, backups=[])
    autocreate = False

    def validate(self):
        if not re.match('^[a-zA-Z0-9:_.]+$', self.name):
            raise ValueError('invalid name')

    def set_active(self, target):
        if self.data.active == target.name:
            return

        if self.data.active:
            gravel_master.Node(self.data.active).call('storage', 'deactivate', self.name)
            self.data.active = None
            self.save()

        self.data.active = target.name
        self.save()
        target.call('storage', 'activate', self.name)
