#!/usr/bin/python

from youku import YoukuUpload
import os
CLIENT_ID       = os.environ['YOUKU_CLIENT_ID']
ACCESS_TOKEN    = os.environ['YOUKU_ACCESS_TOKEN']

def upload2youku( filename, title, tags='PCCES', description = 'video of PCCES, pcces.org' ):
    file_info = {
        'title'         : title,
        'tags'          : tags,
        'description'   : description
    }
    youku = YoukuUpload(CLIENT_ID, ACCESS_TOKEN, filename)
    youku.upload( file_info )

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", "-f",
        help    = "the file name you would like to upload")
    parser.add_argument("--title", "-t",
        default = "PCCES")
    args = parser.parse_args()
    upload2youku( args.filename, args.title )

