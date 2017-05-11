from gmusicapi import Mobileclient
import json

with open('./songs.json', 'r') as f:
    songs = json.load(f)

with open('./config.json', 'r') as f:
    config = json.load(f)

email = config['email']
password = config['password']
api = Mobileclient()
logged_in = api.login(email, password, Mobileclient.FROM_MAC_ADDRESS)
play_list = api.create_playlist('Passport Approved 5 7 17')
for artist, song in songs.items():
    try: 
        search_string = artist + ' - ' + song
        search = api.search(search_string)
        found_artist = search['song_hits'][0]['track']['artist'].lower()
        found_title = search['song_hits'][0]['track']['title'].lower()
        if(found_artist != artist.lower() or found_title != song.lower()):
            print("Missed " + search_string + ". Found " + found_artist + ' - ' + found_title)
        store_id = search['song_hits'][0]['track']['storeId']
        api.add_songs_to_playlist(play_list, store_id)
    except IndexError:
        print("unable to find " + artist + ' - ' + song)
