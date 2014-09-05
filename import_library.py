#!/usr/bin/python
import spotipy, os
import spotipy.util as util

ID = os.environ.get("CLIENT_ID",'')
SECRET = os.environ.get("CLIENT_SECRET",'')
RD_URI = os.environ.get("REDIRECT_URI",'')

def query_spotify(username):

        scope = 'user-library-read'
        token = util.prompt_for_user_token(username=username, scope=scope, client_id=ID, client_secret=SECRET, redirect_uri=RD_URI)

        if token:
            sp = spotipy.Spotify(auth=token)
            results = sp.current_user_saved_tracks(50)
            for item in results['items']:
                track = item['track']
                print track['name'] + ' - ' + track['artists'][0]['name']
        else:
            print "Can't get token for", username


if __name__ == "__main__":
        query_spotify('utstikkar')
