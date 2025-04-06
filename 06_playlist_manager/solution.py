# do not change the method name
def main():
    print("Welcome to Playlist Manager!\n")
    
    playlist = []
    print(f"Current playlist: {playlist}\n")

    title = "Bohemian Rhapsody"
    artist = "Queen"
    print(f'Adding: "{title}" by {artist}')
    playlist.append(f"{title} - {artist}")
    print(f"Current playlist: {playlist}\n")


    title = "Hotel California"
    artist = "Eagles"
    print(f'Adding: "{title}" by {artist}')
    playlist.append(f"{title} - {artist}")
    print(f"Current playlist: {playlist}\n")


    title = "Sweet Child O'Mine"
    artist = "Guns N'Roses"
    print(f'Adding: "{title}" by {artist}')
    playlist.append(f"{title} - {artist}")
    print(f"Current playlist: {playlist}\n")


    title = "Billie Jean"
    artist = "Michael Jackson"
    print(f'Adding: "{title}" by {artist}')
    playlist.append(f"{title} - {artist}")
    print(f"Current playlist: {playlist}\n")
    
    title = "Stairway to Heaven"
    artist = "Led Zeppelin"
    print(f'Adding: "{title}" by {artist}')
    playlist.append(f"{title} - {artist}")
    print(f"Current playlist: {playlist}\n")

    print(f"Recently added songs (last 3): {playlist[-3:]}\n")

    print(f"First song: {playlist[0]}")
    print(f"Last song: {playlist[-1]}\n")
    
    song_to_remove = "Hotel California - Eagles"
    if song_to_remove in playlist:
        print(f'Removing: "Hotel California" by Eagles')
        playlist.remove(song_to_remove)
    print(f"Current playlist: {playlist}\n")

    top_songs = playlist[:2]
    print(f"Top songs list: {top_songs}")
    
# do not change the following lines:
main()
