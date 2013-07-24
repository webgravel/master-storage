#!/usr/bin/env python2.7
import sys
import argparse

sys.path.append('/gravel/pkg/gravel-common')
sys.path.append('/gravel/pkg/gravel-master')

import cmd_util
import storage
import gravel_master
import gravelrpc

def action_activate():
    parser = argparse.ArgumentParser()
    parser.add_argument('id')
    args = parser.parse_args()

    box = storage.Box(args.id)
    box.activate(gravel_master.get_node())

def action_getinfo():
    parser = argparse.ArgumentParser()
    parser.add_argument('id')
    args = parser.parse_args()

    box = storage.Box(args.id)

    gravelrpc.bson.dump(dict(
        type=box.data.type,
        options=box.data.options,
    ), sys.stdout)

def action_fetchinfo():
    parser = argparse.ArgumentParser()
    parser.add_argument('id')
    args = parser.parse_args()

    box = storage.Box(args.id)

    gravelrpc.bson.dump(box.get_fetchinfo(), sys.stdout)

if __name__ == '__main__':
    cmd_util.main_multiple_action(globals())
