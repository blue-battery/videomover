#!/usr/bin/python
import time
import os

from zoomus import ZoomClient
import urllib.request
#import upload2youku

def download_zoom_video(
        output_dir  = '/tmp',
        zoomkey     = os.environ['ZOOM_KEY'],
        zoomsecret  = os.environ['ZOOM_SECRET'] ):
    client = ZoomClient( zoomkey, zoomsecret)
    for user in client.user.list().json()['users']:
        user_id = user['id']
        # meeting_list = client.meeting.list( host_id = user_id )
        recording_list = client.recording.list( host_id = user_id )
        meeting_records = recording_list.json()['meetings']
        for meeting_record in meeting_records:
            print(meeting_record)
            topic = meeting_record['topic']
            print("meeting topic: {}".format(topic))
            for recording_file in meeting_record['recording_files']:
                file_name = '{}/{}_{}.mp4'.format(output_dir,
                        recording_file['recording_start'], topic)
                url = recording_file['download_url']
                print("download {} to {}".format(url, file_name))
                title = os.path.basename(file_name)
                if recording_file['file_type'] == 'MP4':
                    urllib.request.urlretrieve(url, file_name)
		    print("donwload complete, start uploading to {}".format(title))
                    os.system("python ./upload2youtube.py --file \"{}\" --title \"{}\" --noauth_local_webserver".format(
                        file_name, title ))
                    #upload2youku.upload( file_name, title )
                # delete uploaded video in Zoom cloud
                client.recording.delete(
                        meeting_id  = recording_file['meeting_id'],
                        file_id     = recording_file['id'])

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputdir","-d",
            default = "/tmp",
            help    = "output directory")
    parser.add_argument("--sleeptime", "-s",
            default = 60,
            type    = int,
            help    = "time interval of trying to download and upload (minutes)")
    parser.add_argument("--zoomkey", "-k",
            default = os.environ['ZOOM_KEY'],
            help    = "key of zoom.us credential for download permission")
    parser.add_argument("--zoomvalue", "-v",
            default = os.environ['ZOOM_SECRET'],
            help    = "value of zoom.us credential for download permission")
    args = parser.parse_args()
    while True:
        print("trying to download and upload...")
        download_zoom_video( args.outputdir, args.zoomkey, args.zoomvalue )
        print("sleep for {} minutes ...".format( args.sleeptime ))
        time.sleep( args.sleeptime * 60 )
