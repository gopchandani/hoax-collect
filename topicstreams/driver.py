'''
Created on Feb 25, 2014

'''
from argparse import ArgumentParser
from SListener import SListener
import tweepy
import sys
import os
import json

api = None
auth = None

def init_api_handle (kfp):
    
    global api, auth
    
    with open(kfp) as infile:
        auth_data = json.load(infile)
        
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(auth_data['consumer_key'], auth_data['consumer_secret'])
    auth.set_access_token(auth_data['access_token'], auth_data['access_token_secret'])

    api = tweepy.API(auth)

    return api


def collect_stream():
    
    track  = ['rip']
    follow = []
    
    print auth
            
    listen = SListener(api, 'test')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started on %s users and %s keywords..." % (len(track), len(follow))

    try: 
        stream.filter(track = track, follow = follow)
        #stream.sample()
    except:
        print "error!"
        stream.disconnect()
        
        
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

        # Process arguments
        args = parser.parse_args()
        api = init_api_handle(args.kfp)
        collect_stream()
        return 0
    
    except Exception, e:
        raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2
    

if __name__ == '__main__':
    sys.exit(main())