#!/usr/bin/env python2.7
import sys
import argparse

sys.path.append('/gravel/pkg/gravel-common')
sys.path.append('/gravel/pkg/gravel-master')

import cmd_util
import storage
import gravel_master

def action_add():
    parser = argparse.ArgumentParser()
    parser.add_argument('id')
    parser.add_argument('type')
    args = parser.parse_args()

    box = storage.Box(args.id, autocreate=True)
    box.data.type = args.type
    box.save()

def action_show():
    parser = argparse.ArgumentParser()
    parser.add_argument('id', nargs='?', default=None)
    args = parser.parse_args()

    if args.id:
        box = storage.Box(args.id)
        print box
    else:
        for box in storage.Box.all():
            print box

def action_setactive():
    parser = argparse.ArgumentParser()
    parser.add_argument('id')
    parser.add_argument('node')
    args = parser.parse_args()

    box = storage.Box(args.id)
    node = gravel_master.get_one_node(args.node)

if __name__ == '__main__':
    cmd_util.main_multiple_action(globals())
