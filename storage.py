import gravel_master

import graveldb
import re

PATH = '/gravel/system/master'

class Box(graveldb.Table('boxes', PATH)):
    default = dict(type=None, active=None, backups=[], new=True, ready=False,
                   options={})
    autocreate = False

    def validate(self):
        if not re.match('^[a-zA-Z0-9:_.]+$', self.name):
            raise ValueError('invalid name')

    def set_active(self, target):
        if self.data.ready and self.data.active == target.name:
            return

        if self.data.active and self.data.active != target.name:
            gravel_master.Node(self.data.active).call('storage', 'deactivate', self.name)
            self.data.active = None
            self.save()

        self.data.active = target.name
        self.data.ready = False
        self.save()
        target.call('storage', 'activate', self.name)
        self.data.new = False
        self.data.ready = True
        self.save()

    def get_fetchinfo(self):
        if self.data.new:
            return dict(new=True)
        elif self.data.active:
            target_node = self.data.active
        elif self.data.backups:
            date, target_node = sorted(self.data.backups)[0]
        else:
            raise Exception('zero replicas')

        return gravel_master.Node(target_node).arrange_p2p('storage', 'transfer', self.name)
