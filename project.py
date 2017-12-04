"""Project"""
import fnmatch
import os
import subprocess

import yaml

import workspace


def add_parser(subparsers):
    """Add the Parser"""
    parser = subparsers.add_parser('project', help='Create an Xcode project for a target')
    parser.set_defaults(func=project)
    parser.add_argument('target', nargs=1, help='The target to generate the project for')

def project(args):
    """"Project"""
    target = args.target[0]
    specs = get_specs()
    spec = _spec(target, specs)
    if spec != None:
        directory = os.path.dirname(spec['spec'])
        result = _inflate(target, specs)
        xcodegen(result)
        workspace.generate(target, directory, _result(result))
        open_project(directory, target)
    else:
        print 'Target: {} not found!'.format(target)

def _result(input):
    output = {}
    for _, path in input.iteritems():
        spec = __read(path)
        output[spec['name']] = path
    return output

def _spec(target, specs):
    if target in specs:
        return specs[target]
    else:
        return None

def get_specs():
    """Gets all available modules"""
    result = {}
    for root, _, filenames in os.walk('.'):
        for filename in fnmatch.filter(filenames, 'project.yml'):
            path = os.path.join(root, filename).replace('./', '')
            spec = __read(path)
            for target, values in spec['targets'].iteritems():
                if target not in result:
                    result[target] = { 'spec': path , 'deps': [], 'tests': []}
                if 'dependencies' in values:
                    for dep in values['dependencies']:
                        if 'framework' in dep and 'implicit' in dep:
                            result[target]['deps'].append(dep['framework'])
                if 'scheme' in values: 
                    if 'testTargets' in values['scheme']:
                        for test in values['scheme']['testTargets']:
                            result[target]['tests'].append(test)
    return result

def _inflate(target, specs):
    result = {}
    spec = specs[target]
    _get_deps(target, spec, specs, result)
    return result

def _get_deps(target, spec, specs, result):
    result[target] = spec['spec']
    for dep in spec['deps']:
        next_target = dep.replace('.framework', '')
        if next_target in specs:
            next_spec = specs[next_target]
            _get_deps(next_target, next_spec, specs, result)
    for test in spec['tests']:
        if test in specs:
            next_spec = specs[test]
            _get_deps(test, next_spec, specs, result)

def xcodegen(specs):
    """xcodegen"""
    generated = []
    for _, path in specs.iteritems():
        if path not in generated:
            subprocess.call(['XcodeGen', '-s', path, "-p", __head(path), '--quiet'])
            print "Generated => {}".format(path)
            generated.append(path)

def open_project(path, target):
    """"Open the Target project"""
    print 'Quiting Xcode'
    subprocess.call(['osascript', '-e', 'quit app "Xcode"'])
    target_workspace = path + '/' + target + '.xcworkspace'
    print 'Opening: {}'.format(target_workspace)
    subprocess.call(['open', target_workspace])

def __head(path):
    head, _ = os.path.split(path)
    return head

def __read(path):
    return yaml.load(open(path))
