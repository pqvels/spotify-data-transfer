import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
load_dotenv()


client_id = os.getenv("YOUR_APP_CLIENT_ID")
client_secret = os.getenv("YOUR_APP_CLIENT_SECRET")
redirect_uri = os.getenv("YOUR_APP_REDIRECT_URI")

scope="user-follow-modify user-library-modify playlist-modify-public playlist-modify-private" 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
                                               client_secret,
                                               redirect_uri,
                                               scope=scope))


def add_artist():
    message = "artists"
    filename = "export_artists.txt"
    
    id_list = []
    crimefile = open(filename, 'r')
    id_list = [line.removesuffix("\n") for line in crimefile]
    full_count = len(id_list)
    count = len(id_list)

    while count > 0:
        sp.user_follow_artists(id_list[:50])        
        del id_list[0:50]
        count = len(id_list)
        if count == 0:
            break

    print("Import of {} {} has been successfully completed".format(full_count, message))

def add_tracks():
    message = "tracks"
    filename = "export_tracks.txt"    
    id_list = []
    crimefile = open(filename, 'r')
    id_list = [line.removesuffix("\n") for line in crimefile]
    full_count = len(id_list)
    count = len(id_list)
    
    while count > 0:
        sp.current_user_saved_tracks_add(id_list[:50])
        del id_list[0:50]
        count = len(id_list)
        if count == 0:
            break  

    print("Import of {} {} has been successfully completed".format(full_count, message))

def add_albums():
    message = "albums"
    filename = "export_albums.txt"  
    id_list = []
    crimefile = open(filename, 'r')
    id_list = [line.removesuffix("\n") for line in crimefile]
    count = len(id_list)
    full_count = len(id_list)

    while count > 0:
        sp.current_user_saved_albums_add(id_list[:50])
        del id_list[0:50]
        count = len(id_list)
        if count == 0:
            break  
        
    print("Import of {} {} has been successfully completed".format(full_count, message))

def add_playlists():
    message = "playlists"
    filename = "export_playlists.txt"    
    id_list = []
    crimefile = open(filename, 'r')
    id_list = [line.removesuffix("\n") for line in crimefile]
    count = len(id_list)
    full_count = len(id_list)

    for i in id_list:
        a = str([i])
        b = a[2:24]
        sp.current_user_follow_playlist(b)
  
        
    print("Import of {} {} has been successfully completed".format(full_count, message))

def add_episodes():
    message = "episodes"
    filename = "export_episodes.txt"  
    id_list = []
    crimefile = open(filename, 'r')
    id_list = [line.removesuffix("\n") for line in crimefile]
    count = len(id_list)
    full_count = len(id_list)

    while count > 0:
        sp.current_user_saved_episodes_add(id_list[:50])
        del id_list[0:50]
        count = len(id_list)
        if count == 0:
            break  
        
    print("Import of {} {} has been successfully completed".format(full_count, message))

def add_shows():
    message = "shows"
    filename = "export_shows.txt"  
    id_list = []
    crimefile = open(filename, 'r')
    id_list = [line.removesuffix("\n") for line in crimefile]
    count = len(id_list)
    full_count = len(id_list)

    while count > 0:
        sp.current_user_saved_shows_add(id_list[:50])
        del id_list[0:50]
        count = len(id_list)
        if count == 0:
            break  
        
    print("Import of {} {} has been successfully completed".format(full_count, message))


add_artist()
add_tracks()
add_albums()
add_playlists()
add_episodes()
add_shows()