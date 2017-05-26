#!/usr/bin/python

import os
ZOOM_KEY = os.environ['ZOOM_KEY']
ZOOM_SECRET = os.environ['ZOOM_SECRET']

from zoomus import ZoomClient
import urllib.request

def download_zoom_video( output_dir='/tmp' ):
    client = ZoomClient( ZOOM_KEY, ZOOM_SECRET)
    for user in client.user.list().json()['users']:
        user_id = user['id']
        # meeting_list = client.meeting.list( host_id = user_id )
        recording_list = client.recording.list( host_id = user_id )
        meeting_records = recording_list.json()['meetings']
        for meeting_record in meeting_records:
            print(meeting_record)
            for recording_file in meeting_record['recording_files']:
                file_name = '{}/{}_{}.mp4'.format(output_dir,
                        recording_file['recording_start'],
                        recording_file['meeting_id'])
                url = recording_file['download_url']
                print(url)
                urllib.request.urlretrieve(url, file_name)
                os.system("python ./upload_video.py --file {} --title {}".format(
                    file_name, os.path.basename(file_name)))
                # delete uploaded video in Zoom cloud
                client.recording.delete(
                        meeting_id  = recording_file['meeting_id'],
                        file_id     = recording_file['id'])

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputdir","-d",
                default = "/tmp",
                help = "output directory")
    args = parser.parse_args()

    download_zoom_video( args.outputdir )
