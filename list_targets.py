"""List all projects"""
import fnmatch
import os

import yaml


def add_parser(subparsers):
    """Add the Parser"""
    parser = subparsers.add_parser('list', help='Lists all available projects')
    parser.set_defaults(func=list_targets)

def list_targets(args=None):
    """Lists all available projects"""
    print "\nProjects: "
    result = []
    for root, _, filenames in os.walk('.'):
        for filename in fnmatch.filter(filenames, 'project.yml'):
            path = os.path.join(root, filename)
            spec = yaml.load(open(path))
            result.append(spec['name'])
    for item in sorted(result):
        print " - " + item
    print ""
