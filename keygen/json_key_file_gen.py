#!/usr/local/bin/python2.7
# encoding: utf-8
'''
@author:     Rakesh
'''

import sys
import os
import json

from argparse import ArgumentParser

__all__ = []
__version__ = 0.1
__date__ = '2014-02-28'
__updated__ = '2014-02-28'

def generate_json_file(kfp, ck, cs, at, ats):    
    auth_data = {"consumer_key":ck, 
            "consumer_secret":cs, 
            "access_token":at, 
            "access_token_secret":ats}
    
    with open(kfp, 'wb') as outfile:
        json.dump(auth_data, outfile)


class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): 
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])

    try:
        # Setup argument parser
        parser = ArgumentParser(description='')
        parser.add_argument("-kfp", dest="kfp", help="Full path to where the output json file should be saved", metavar="keyfilepath", nargs='?', required=True)
        parser.add_argument("-ck", dest="ck", help="Consumer Key", metavar="consumer_key", nargs='?', required=True)
        parser.add_argument("-cs", dest="cs", help="Consumer Secret", metavar="consumer_secret", nargs='?', required=True)
        parser.add_argument("-at", dest="at", help="Access Token", metavar="access_token", nargs='?', required=True)
        parser.add_argument("-ats", dest="ats", help="Access Token Secret", metavar="access_token_secret", nargs='?', required=True)

        # Process arguments
        args = parser.parse_args()
        generate_json_file(args.kfp, args.ck, args.cs, args.at, args.ats)       
        return 0
    
    except Exception, e:
        raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":

    sys.exit(main())