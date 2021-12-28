import requests
import webbrowser

class Media:

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", json=None):
        self.json = json
        if json is not None:
            #self.title = self.json['trackName'] #changed to collectionName, was collectioncensoredname. Now changed to trackName
            if self.json.get("trackName") is not None:
                self.title = self.json['trackName']
            else:
                self.title = self.json['collectionName']

            self.author = self.json['artistName']
            self.release_year = self.json['releaseDate'].split("-")[0] #need to  split

            if self.json.get("trackViewUrl") is not None:
                self.url = self.json['trackViewUrl']
            else:
                self.url = self.json['collectionViewUrl']
            #self.url = self.json['collectionViewUrl']
            #self.url = self.json['trackViewUrl'] #chnaged to trackviewurl, was collectionViewUrl

        else:
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url

    def info(self):
        return f"{self.title} by {self.author} ({self.release_year})"

    def length(self):
        return 0


# Other classes, functions, etc. should go here

class Song(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", album="No Album", genre="No Genre", track_length=0, json=None):
        super().__init__(title, author, release_year, url, json)
        if json is not None:
            self.title = self.json['trackName'] 
            self.author = self.json['artistName']
            self.release_year = self.json['releaseDate'].split("-")[0] #need to  split
            self.url = self.json['trackViewUrl'] #wascollectionviewurl
            self.album = self.json['collectionName'] 
            self.genre = self.json['primaryGenreName']
            self.track_length = int(self.json['trackTimeMillis'])
        else:
            self.album = album
            self.genre = genre
            self.track_length = track_length

    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.genre}]"

    def length(self):
        round_l = round(self.track_length * 0.001)
        return round_l

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", rating="No Rating", movie_length=0,json=None):
        super().__init__(title, author, release_year, url, json)
        if json is not None:
            self.title = self.json['trackName'] 
            self.author = self.json['artistName']
            self.release_year = self.json['releaseDate'].split("-")[0] #need to  split
            self.url = self.json['trackViewUrl']
            self.rating = self.json['contentAdvisoryRating']
            self.movie_length = self.json['trackTimeMillis']
        else:
            self.rating = rating
            self.movie_length = movie_length

    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.rating}]"

    def length(self):
        round_l = round(self.movie_length * 1.66667e-5)
        return round_l #rounding to the nearest minute

####################
###### Part 3 ######
####################

#Fetching data from iTunes

def song_format(song_list): 
    count = 1
    for song in song_list:
        print(count, song.info())
        count += 1
    return count

def movie_format(movie_list,c): 
    count = c
    for movie in movie_list:
        print(count, movie.info())
        count += 1
    return count

def other_format(other_list,c):
    count = c
    for other in other_list:
        print(count, other.info())
        count += 1
    return count

def final_format(song_list, movie_list, other_list): 
    #call song_format, movie_format, other_format
    print("SONGS")
    c = song_format(song_list)
    print("MOVIES")
    c = movie_format(movie_list,c)
    print("OTHER MEDIA")
    c = other_format(other_list,c)
    return c


if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here

    base_url = 'https://itunes.apple.com/search?term="'

    song_kind = ['album', 'song']
    movie_kind = ['feature-movie']
    other_kind = []

    while True:
        song_list = []
        movie_list = []
        other_list = []

        search1 = input("Enter a search term, or 'exit' to quit:")
        if search1 == "exit":
            print("Bye")
            break
        elif search1.isnumeric():
            link = webbrowser.open(base_url+search1)
            f" Launching {link} in web browser ..."
        else:
            new_search = requests.get(base_url + search1)
            new_output = new_search.json()
            itunes_list = new_output['results']
            if not itunes_list:
                print("Please try again")
                continue

            #identify what kind it is 
            for item in itunes_list:
                #print(item)
                if item.get("kind") is not None:
                    #print("Exists")
                    kind = item['kind']
                    #extract data
                    # append it to list,
                    if kind in song_kind:
                        #print(' ')
                        #It is a song
                        S = Song(json=item)
                        song_list.append(S)
                    elif kind in movie_kind:
                        #print(item, '\n','\n')
                        #It is a Movie
                        M = Movie(json=item)
                        movie_list.append(M)
                    else:
                        # Its other media
                        O = Media(json=item)
                        other_list.append(O)
                else:
                    #print("Does not exist")
                    # #instantiat Media with info here
                    O = Media(json=item)
                    other_list.append(O)


        final_format(song_list,movie_list,other_list)
    print(final_format)



