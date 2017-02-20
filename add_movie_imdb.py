#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Retrieve movie information by IMDb ID and store it for inclusion in the movie recommendations.
Note: Every addition triggers the regenerations of the HTML file."""

import sys
import settings
from media import Movie

youtube_id = ""
imdb_id = ""

if len(settings.wemakesites_api_key) < 20:
    print """Are you sure that the api key placed in the settings is valid? Mine reads like
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"""
    quit()

if len(sys.argv) < 2:
    print "Please specify at least the IMDb ID of the desired movie."
    quit()

if len(sys.argv) > 1:
    if Movie.validate_imdb(sys.argv[1]):
        imdb_id = sys.argv[1]
        print "Adding video " + imdb_id
    else:
        print "IMDB ID invalid: " + sys.argv[1]
        quit()
        
if len(sys.argv) == 3:
    if Movie.validate_youtube(sys.argv[2]):
        youtube_id = sys.argv[2]
        print "Adding with trailer!"
    else:
        print "YouTube Trailer invalid: " + sys.argv[2]
        quit()

Movie.set_api_key(settings.wemakesites_api_key)
Movie.add_from_imdb(imdb_id, youtube_id)

execfile("entertainment_center.py")