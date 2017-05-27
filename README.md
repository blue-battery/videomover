# videomover
Since the cloud storage of Zoom.us is pretty limited, and manually downloading and uploading to video websites is tedious. This package aims to solve this problem. It moves recording files from Zoom.us to a storage space, such as local server, Youtube, and YouKu.

# Installation
this package was tested using python3.6, all python3 version should be fine. 

## setup key and secret
To get the permission of accessing or deleting recording files, you should use key and secret from developer page of the official web sites.

### Zoom.us
we use enviroment variable to provide the key and secret.

add the two lines in the end of your `~/.bashrc` (linux) | `~/.bash_profile` (MacOS)
```
export ZOOM_KEY=YOUR_KEY_HERE
export ZOOM_SECRET=YOUR_SECRET_HERE
```
enable the enviroment variable: `source ~/.bashrc`

### Youtube
The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
the OAuth 2.0 information for this application, including its client_id and
client_secret. You can acquire an OAuth 2.0 client ID and client secret from
the {{ Google Cloud Console }} at {{ https://cloud.google.com/console }}.
Please ensure that you have enabled the YouTube Data API for your project.
For more information about using OAuth2 to access the YouTube Data API, see:
    https://developers.google.com/youtube/v3/guides/authentication
For more information about the client_secrets.json file format, see:
    https://developers.google.com/api-client-library/python/guide/aaa_client_secrets

make a credential file with `service account` permission, and move it to `~/.google.secret.json`. Our package will automatically load the json file and handle the authorization.

### Youku
The video was uploaded using Youku cloud, so register a Youku cloud account first. Follow the [documentation of Youku cloud API](https://cloud.youku.com/docs?id=0), you'll get you `client ID` and `client secret` string.

Similar with Zoom.us, Youku uses the environment variable to grant permissions. add these two lines in the end of your rc file.
```
export YOUKU_CLIENT_ID=YOUR_ID_HERE
export YOUKU_CLIENT_SECRET=YOUR_SECRET_HERE
```
use `source ~/.bashrc` (linux) or `source ~/.bash_profile` to enable your environment.

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
