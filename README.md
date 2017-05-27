# videomover
Since the cloud storage of Zoom.us is pretty limited, and manually downloading and uploading to video websites is tedious. This package aims to solve this problem. It moves recording files from Zoom.us to a storage space, such as local server, Youtube, and YouKu.

# Installation
this package was tested using python3.6, all python3 version should be fine.

## setup key and secret
To get the permission of accessing or deleting recording files, you should use key and secret from developer page of Zoom.us.

we use enviroment variable to provide the key and secret.

add the two lines in the end of your `~/.bashrc` (linux) | `~/.bash_profile` (MacOS)
```
export ZOOM_KEY=YOUR_KEY_HERE
export ZOOM_SECRET=YOUR_SECRET_HERE
```
enable the enviroment variable: `source ~/.bashrc`

# Resources and References
## Zoom.us

python package 
https://github.com/actmd/zoomus

Zoom.us REST API
https://support.zoom.us/hc/en-us/articles/206324325-REST-Cloud-Recording-API

## Youtube API

### official REST API
https://developers.google.com/youtube/v3/code_samples/python#upload_a_video

### python code sample
https://github.com/youtube/api-samples/tree/master/python

## Youku 
python SDK
https://github.com/hanguokai/youku
