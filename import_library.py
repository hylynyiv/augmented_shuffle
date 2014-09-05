#!/usr/bin/python
import spotipy, os
import spotipy.util as util
import codecs
import sys

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

ID = os.environ.get("CLIENT_ID",'')
SECRET = os.environ.get("CLIENT_SECRET",'')
RD_URI = os.environ.get("REDIRECT_URI",'')

def get_tracks(token):
    sp = spotipy.Spotify(auth=token)
    all_results = []
    results = sp.current_user_saved_tracks(50).get('items')
    while(len(results) > 0):
        all_results.extend(results)
        results = sp.current_user_saved_tracks(50, len(all_results)).get('items')
    return all_results

def transform_tracks(item):
    track = item['track']
    return track['name'] + '\t' + track['artists'][0]['name']

def query_spotify(username, output_file):
        scope = 'user-library-read'
        token = util.prompt_for_user_token(username=username, scope=scope, client_id=ID, client_secret=SECRET, redirect_uri=RD_URI)

        if token:
            tracks = get_tracks(token)
            print len(tracks)
            lines = map(transform_tracks, tracks)
            UTF8Writer(open(output_file, 'w')).write("\n".join(lines))
        else:
            print "Can't get token for", username


if __name__ == "__main__":
        query_spotify('utstikkar', sys.argv[1])
