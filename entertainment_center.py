#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Generate a static responsive HTML page displaying stored movie recommendations"""

import shared
import settings
from media import Movie
import fresh_tomatoes

movies = Movie.imdb_load()

fresh_tomatoes.open_movies_page(movies,settings.page_title.encode("utf-8").strip())

