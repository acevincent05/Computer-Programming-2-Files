    #gets the information of each song
class Song: 
    def __init__(self, songName, artist, duration, album):
        self._songName = songName
        self._artist = artist
        self._duration = duration
        self._album = album

    @property
    def songName(self):
        return self._songName

    @songName.setter
    def songName(self, new_name):
        self._songName = new_name

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, new_artist):
        self._artist = new_artist

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        self._duration = new_duration

    @property
    def album(self):
        return self._album

    @album.setter
    def album(self, new_album):
        self._album = new_album    

    def SongDetails(self):
        return f"Title: {self.songName}\nArtist: {self.artist}\nAlbum: {self.album}\nDuration: {self.duration} minutes"
    
    def __str__(self):
        return self.SongDetails()

#gets the information of the playlist and its list of songs
class Playlist:
    def __init__(self, playlistName, dateCreated):
        self._playlistName = playlistName
        self._dateCreated = dateCreated
        self._songlist = []

    @property
    def playlistName(self):
        return self._playlistName

    @playlistName.setter
    def playlistName(self, new_name):
        self._playlistName = new_name

    @property
    def dateCreated(self):
        return self._dateCreated

    @dateCreated.setter
    def dateCreated(self, new_date):
        self._dateCreated = new_date

    @property
    def songlist(self):
        return self._songlist

    #adds the inputted song to the created playlist
    def addToPlaylist(self, song: Song):
        self.songlist.append(song)

    #organizes the songs included in the playlist   
    def viewSongs(self):
        for index, song in enumerate(self.songlist, start=1):
            print(f'{index}. "{song.songName}" by {song.artist}')

    #allows the user to view the details of a song
    def songDetails(self):
        input_song = int(input('Enter song number to see details: '))
        song = self.songlist[input_song - 1]
        print()
        print(song.SongDetails())

#gets user input about the playlist
playlistName = input('Enter playlist name: ')
dateCreated = input('Enter date created: ')

play1 = Playlist(playlistName, dateCreated)

#add songs in the playlist with its details
while True:
    user_input = input('Add a song? (y/n): ').strip().lower()
    if user_input != 'y':
        break
    print()
    name = input('Enter song title: ')
    artist = input('Enter artist name: ')
    duration = input('Enter duration: ')
    album = input('Enter album name: ')

    song1 = Song(name, artist, duration, album)
    play1.addToPlaylist(song1)

print()
print(f'Songs in "{playlistName}" - {dateCreated}:')
play1.viewSongs()
play1.songDetails()