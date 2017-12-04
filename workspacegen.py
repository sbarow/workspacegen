#!/usr/bin/env python
"""WorkspaceGen"""
import argparse

import clean
import list_targets
import project

COMMAND_MODULES = [
    list_targets,
    clean,
    project,
]

p = argparse.ArgumentParser(prog='monorepo')
p.add_argument('--version', action='version', version='%(prog)s 1.0')
subparsers = p.add_subparsers(title='commands')

for command in COMMAND_MODULES:
    command.add_parser(subparsers)

args = p.parse_args()
args.func(args)
