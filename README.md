# spotify-data-transfer
Transfer your Spotify data (artists, tracks, playlists, podcasts) from one account to another.
# Installation:
Clone this repo:
```
$ git clone https://github.com/pqvels/spotify-data-transfer.git
```
Go to the "spotify-data-transfer" directory:
```
$ cd spotify-data-transfer
```
Install the required libraries using pip:
```
$ pip3 install -r requirements.txt
```
# Setting up:
1. Go to [Spotify Dashboard page](https://developer.spotify.com/dashboard/).
2. Log in and create a new application.
3. Click Edit Settings and add http://localhost:8888/callback to Redirect URIs.
4. Click Users and Access then Add New User and write it your another accounts email adress.
5. Copy and paste Client ID from Dashboard to YOUR_APP_CLIENT_ID in `.env` file.
6. Copy and paste Client ID (you should click Show Clients Secret) from Dashboard to YOUR_APP_CLIENT_SECRET in `.env` file.
# Run:
1. Login to your spotify accout from which you want to export information into your default browser.
2. Run the script for export:
```
$ python3 export.py
```
3. Login to your spotify accout from which you want to import information into your default browser.
4. Run the script for export:
```
$ python3 import.py
```
