#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Generate a responsive HTML page for stored movie recommendations"""

from media import Movie
import fresh_tomatoes

movies = Movie.imdb_load()

fresh_tomatoes.open_movies_page(movies)

