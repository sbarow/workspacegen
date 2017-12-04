"""Workspace"""
import os
import shutil
import string
from xml.etree.ElementTree import Element, ElementTree, SubElement

import yaml


def generate(name, directory, specs):
    """Generate a workspace"""
    root = Element('Workspace')
    root.set('version', '1.0')

    abs_path = os.path.abspath('.')
    keys = sorted(specs)
    for key in keys:
        path = os.path.join('./', specs[key])
        array = string.split(path, '/')
        array.pop(0)

        parent = root
        count = len(array)
        while count > 0:
            item = array[0]
            if item == 'project.yml' or array[1] == 'project.yml':
                _file_ref(parent, _project(path), abs_path)
                break
            else:
                parent = _group(parent, item)
            array.pop(0)
            count -= 1

    path = '{}/{}.xcworkspace'.format(directory, name)
    contents_path = '{}/contents.xcworkspacedata'.format(path)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    ElementTree(root).write(contents_path, encoding='UTF-8', method='xml')
    print "\n"

def _project(path):
    data = yaml.load(open(path))
    name = data['name']
    return path.replace('project.yml', '{}.xcodeproj'.format(name))

def _group(parent, name):
    group = _find_element(parent, name)
    if group is None:
        group = SubElement(parent, 'Group')
    group.set('location', 'container:')
    group.set('name', name)
    return group

def _find_element(element, name):
    for node in element.findall('Group'):
        if node.attrib['name'] == name:
            return node
    return None

def _file_ref(parent, path, abs_path):
    item = SubElement(parent, 'FileRef')
    item.set('location', 'container:{}'.format(os.path.join(abs_path, os.path.relpath(path))))
    return item
