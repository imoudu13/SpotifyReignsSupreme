import requests
import csv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

clientID = "Cannot_share_mine"
clientSecret = "Cannot_share_mine"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID, client_secret=clientSecret, redirect_uri='https://developer.spotify.com/dashboard/create', scope='user-library-modify'))


def getToken(id, secret):
    tokenUrl = 'https://accounts.spotify.com/api/token'
    data = {'grant_type': 'client_credentials'}
    response = requests.post(tokenUrl, data=data, auth=(id, secret))
    access_token = response.json()['access_token']
    return access_token

token = getToken(clientID, clientSecret)

def readSongCSV(filePath):
    songs = []
    with open(filePath, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            song_name, artist_name = row
            songs.append({'name': song_name, 'artist': artist_name}) #add the song to the list


    return songs


songsList = readSongCSV('output.csv')


for song in songsList:
    query = f"{song['name']} {song['artist']}"
    results = sp.search(q=query, type='track', limit=1)

    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        sp.current_user_saved_tracks_add(tracks=[track_id])
        print(f"Added {song['name']} by {song['artist']} to your Spotify favorites.")
    else:
        print(f"Could not find {song['name']} by {song['artist']} on Spotify.")




