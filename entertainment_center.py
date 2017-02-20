#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Generate a static responsive HTML page displaying stored movie recommendations"""

from media import Movie
import fresh_tomatoes

movies = Movie.imdb_load()

fresh_tomatoes.open_movies_page(movies)

