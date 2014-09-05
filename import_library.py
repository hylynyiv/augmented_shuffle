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

def get_tracks(token, max_tracks):
    sp = spotipy.Spotify(auth=token)
    all_results = []
    step = 50 if max_tracks == -1 else min(max_tracks, 50)
    results = sp.current_user_saved_tracks(step).get('items')
    while(len(results) > 0):
        all_results.extend(results)
        step = 50 if max_tracks == -1 else min(max_tracks - len(all_results), 50)
        results = sp.current_user_saved_tracks(step, len(all_results)).get('items')
    return all_results

def transform_tracks(item):
    track = item['track']
    return track['name'] + '\t' + track['artists'][0]['name']

def query_spotify(username, output_file):
        scope = 'user-library-read'
        token = util.prompt_for_user_token(username=username, scope=scope, client_id=ID, client_secret=SECRET, redirect_uri=RD_URI)

        if token:
            tracks = get_tracks(token, -1)
            lines = map(transform_tracks, tracks)
            UTF8Writer(open(output_file, 'w')).write("\n".join(lines))
        else:
            print "Can't get token for", username


if __name__ == "__main__":
        query_spotify('utstikkar', sys.argv[1])
