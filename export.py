import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
load_dotenv()


client_id = os.getenv("YOUR_APP_CLIENT_ID")
client_secret = os.getenv("YOUR_APP_CLIENT_SECRET")
redirect_uri = os.getenv("YOUR_APP_REDIRECT_URI")

scope="user-follow-read user-library-read playlist-read-private playlist-read-collaborative user-read-playback-position"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
                                               client_secret,
                                               redirect_uri,
                                               scope=scope))

def get_artists_id():
    message = "artists"
    filename = "export_artists.txt"    
    id_list = []

    get1 = sp.current_user_followed_artists(limit=50)
    for i in get1["artists"]["items"]:
        id_list.append(i["id"])

    after_id = get1["artists"]["cursors"]["after"]
    
    count = int(get1["artists"]["total"])

    while len(id_list) < count:
        get2 = sp.current_user_followed_artists(limit=50, after=after_id)
        for i in get2["artists"]["items"]:
            id_list.append(i["id"])            
            after_id = get2["artists"]["cursors"]["after"]

    full_count = len(id_list)

    with open(filename, 'w') as outfile:
        outfile.write('\n'.join(str(i) for i in id_list))


    print("Export of {} {} has been successfully completed".format(full_count, message))

def get_tracks_id():
    message = "tracks"
    filename = "export_tracks.txt"
    id_list = []
   
    get1 = sp.current_user_saved_tracks(limit=50)
    count = int(get1["total"])

    for i in get1["items"]:
        id_list.append(i["track"]["id"])
    offset = int(50)

    while len(id_list) < count:
        get2 = sp.current_user_saved_tracks(limit=50, offset=offset)
        for i in get2["items"]:
            id_list.append(i["track"]["id"])            
        offset += 50

    full_count = len(id_list)
    
    with open(filename, 'w') as outfile:
        outfile.write('\n'.join(str(i) for i in id_list))


    print("Export of {} {} has been successfully completed".format(full_count, message))

def get_albums_id():
    message = "albums"
    filename = "export_albums.txt"

    id_list = []
   
    get1 = sp.current_user_saved_albums(limit=50)
    
    count = int(get1["total"])
    for i in get1["items"]:
        id_list.append(i["album"]["id"])
    offset = int(50)
    while len(id_list) < count:
        get2 = sp.current_user_saved_albums(limit=50, offset=offset)
        for i in get2["items"]:
            id_list.append(i["album"]["id"])            
        offset += 50

    full_count = len(id_list)
    

    with open(filename, 'w') as outfile:
        outfile.write('\n'.join(str(i) for i in id_list))


    print("Export of {} {} has been successfully completed".format(full_count, message))

def get_playlists_id():
    message = "playlists"
    filename = "export_playlists.txt"
    id_list = []
   
    get1 = sp.current_user_playlists(limit=50)
    
    count = int(get1["total"])
    for i in get1["items"]:
        id_list.append(i["id"])
    offset = int(50)
    while len(id_list) < count:
        get2 = sp.current_user_playlists(limit=50, offset=offset)
        for i in get2["items"]:
            id_list.append(i["id"])            
        offset += 50


    full_count = len(id_list)
    

    with open(filename, 'w') as outfile:
        outfile.write('\n'.join(str(i) for i in id_list))


    print("Export of {} {} has been successfully completed".format(full_count, message))

def get_episodes_id():
    message = "episodes"
    filename = "export_episodes.txt"
    id_list = []
  
    get1 = sp.current_user_saved_episodes(limit=50)
    count = int(get1["total"])
    for i in get1["items"]:
        id_list.append(i["episode"]["id"])
    offset = int(50)
    while len(id_list) < count:
        get2 = sp.current_user_saved_episodes(limit=50, offset=offset)
        for i in get2["items"]:
            id_list.append(i["episode"]["id"])          
        offset += 50

    full_count = len(id_list)
    

    with open(filename, 'w') as outfile:
        outfile.write('\n'.join(str(i) for i in id_list))


    print("Export of {} {} has been successfully completed".format(full_count, message))

def get_shows_id():
    message = "shows"
    filename = "export_shows.txt"
    id_list = []
   
    get1 = sp.current_user_saved_shows(limit=50)
    count = int(get1["total"])

    for i in get1["items"]:
        id_list.append(i["show"]["id"])
    offset = int(50)
    while len(id_list) < count:
        get2 = sp.current_user_saved_shows(limit=50, offset=offset)
        for i in get2["items"]:
            id_list.append(i["show"]["id"])          
        offset += 50

    full_count = len(id_list)
    

    with open(filename, 'w') as outfile:
        outfile.write('\n'.join(str(i) for i in id_list))


    print("Export of {} {} has been successfully completed".format(full_count, message))

get_artists_id()
get_tracks_id()
get_albums_id()
get_playlists_id()
get_episodes_id()
get_shows_id()