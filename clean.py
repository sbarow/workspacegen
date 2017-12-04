"""Clean"""
import glob
import shutil


def add_parser(subparsers):
    """Add the Parser"""
    parser = subparsers.add_parser('clean', help='Cleans all generated files & directories')
    parser.set_defaults(func=clean)

def clean(args=None):
    """Clean all generated files"""
    for path in glob.glob("**/*/*.xcworkspace"):
        shutil.rmtree(path)
    for path in glob.glob("**/*/*.xcodeproj"):
        shutil.rmtree(path)
    print "Removed all generated files."
