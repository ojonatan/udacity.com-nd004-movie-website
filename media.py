import urllib
import re
import settings
import os
import json
from imdbpie import Imdb

class Movie():
    """Movie object storing detailed information and related media links

    Parameters
    ----------
    title
        Movie title
    storyline
        A short excerpt of the moviews Storyline
    poster_image_url
        Covershot URL
    trailer_youtube_url
        Youtube URL of the trailer
    genre : list
        List of genres
    
    """

    __api_key = ""
    __movies = []
    def __init__(self, title, storyline, image, trailer_url, genre):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_url
        self.genre = genre
    
    @staticmethod
    def set_api_key(api_key):
        """Sets the private property __api_key to allow information retrieval from the selected inofficial IMDb REST API"""
        Movie.__api_key = api_key
    
    @staticmethod
    def validate_imdb(fragment):
        """Validates the passed parameter against the typical IMDb ID pattern"""
        return re.match('tt[0-9]{7}$',fragment)

    @staticmethod
    def validate_youtube(fragment):
        """Validates the passed parameter against by retrieving the HTTP response code assuming 200 means it is valid.
        
        @return bool 
        """
        request=urllib.urlopen('https://www.youtube.com/watch?v=' + fragment)
        return request.getcode() == 200

    @staticmethod
    def imdb_load_file(file_name):
        """Loads a stored JSON file according for the given filename from the subfolder imdb."""
        imdb_saved = open(file_name)
        imdb_save = json.loads(imdb_saved.read())
        Movie.__movies.append(
            Movie(
                imdb_save['title'],
                imdb_save['description'],
                imdb_save['image'],
                "https://www.youtube.com/watch?v=" + imdb_save['youtube_id'],
                imdb_save['genres']
            )
        )

    @staticmethod
    def imdb_load():
        """Loads all JSON files from the subfolder imdb and calls imdb_load_file respectively.
        
        @return list 
        """
        for root, dirs, filenames in os.walk(os.path.dirname(__file__) + "/imdb"):
            for file_name in filenames:
                if file_name.find(".json") > 0:
                    Movie.imdb_load_file(os.path.dirname(__file__) + "/imdb/" + file_name)
        return Movie.__movies          
        
        
    @staticmethod
    def add_from_imdb(imdb_id, youtube_id):        
        """Retrieves movie data from the inofficial IMDb REST API as well as the IMDB lib imdbpie."""
        file_name = os.path.dirname(__file__) + "/imdb/" + imdb_id + ".json"
        if not os.path.isdir(os.path.dirname(file_name)):
            os.mkdir(os.path.dirname(file_name))

        if os.path.isfile(file_name):
            imdb_saved = open(file_name)
            imdb_save = json.loads(imdb_saved.read())
        else:
            response = urllib.urlopen('http://imdb.wemakesites.net/api/' + imdb_id + '?api_key=' + Movie.__api_key)
            json_response = response.read()
            imdb_data = json.loads(json_response)
            imdb_save = imdb_data['data']

        imdb = Imdb()
        imdb = Imdb(anonymize=True) # to proxy requests
        movie = imdb.get_title_by_id(imdb_id)
        if not movie.title:
            movie.title = raw_input("Movie Title not defined. Please set: ") 

        imdb_save['rating'] = movie.rating
        imdb_save['title'] = movie.title
        
        if youtube_id:
            imdb_save['youtube_id'] = youtube_id
            
        imdb_file = open(file_name, 'w')
        imdb_file.write(json.dumps(imdb_save))
        imdb_file.close()
        


        
