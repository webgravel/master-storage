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
    parser.add_argument('option', nargs='*')
    args = parser.parse_args()

    box = storage.Box(args.id, autocreate=True)
    box.data.type = args.type
    for option in args.option:
        if '=' not in option:
            sys.exit('option must contain "="')
        k, v = option.split('=', 1)
        box.data.options[k] = v
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
    box.set_active(node)

if __name__ == '__main__':
    cmd_util.main_multiple_action(globals())
