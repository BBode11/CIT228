print("*---------- 8-7 ----------*")
def make_album(artist_name, album_title):
        album = {
            "Artist": artist_name.title(),
            "Album Title": album_title.title(),
            }
        return album

album = make_album('Lincoln Park', 'Hybrid Theory')
print(album)

album = make_album("Led Zeppelin", "Led Zeppelin II")
print(album)

album = make_album("Def Leppard", "Hysteria")
print(album, "\n")

def make_album(artist_name, album_title, songs=0):
        album = {
            "Artist": artist_name.title(),
            "Album Title": album_title.title(),
            }
        if songs:
            album["songs"] = songs
        return album

album = make_album('Lincoln Park', 'Hybrid Theory', songs=12)
print(album)

album = make_album("Led Zeppelin", "Led Zeppelin II")
print(album)

album = make_album("Def Leppard", "Hysteria")
print(album)

print("\n*---------- 8-8 ----------*")

def make_album(artist_name, album_title, songs=0):
        album = {
            "Artist": artist_name.title(),
            "Album Title": album_title.title(),
            }
        if songs:
            album["songs"] = songs
        return album
#Prompt user for values
artist_name_prompt = "What artist do you like?"
album_title_prompt = "What is their best album?"

print("To exit the application enter 'q' at any time.")

while True:
    artist = input(artist_name_prompt)
    if artist == "q":
        break

    title = input(album_title_prompt)
    if title == "q":
        break
    album = make_album(artist, title)
    print(album)
