#!/usr/bin/python

import os
ZOOM_KEY = os.environ['ZOOM_KEY']
ZOOM_SECRET = os.environ['ZOOM_SECRET']


from zoomus import ZoomClient
import urllib.request

client = ZoomClient( ZOOM_KEY, ZOOM_SECRET)

for user in client.user.list().json()['users']:
    user_id = user['id']
    meeting_list = client.meeting.list( host_id = user_id )
    recording_list = client.recording.list( host_id = user_id )
    meeting_records = recording_list.json()['meetings']
#     print(meeting_records)
    for meeting_record in meeting_records:
#         print(meeting_record)
        for recording_file in meeting_record['recording_files']:
            file_name = '/Users/jpwu/Desktop/{}.mp4'.format(recording_file['id'])
            url = recording_file['download_url']
            urllib.request.urlretrieve(url, file_name)
            print(url)






