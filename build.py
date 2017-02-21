#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Generating/updating project related files"""

import hashlib
import re
import os
import binascii
import datetime
import time
from media import Movie

files = [
    'add_movie_imdb.py',
    'entertainment_center.py',
    'fresh_tomatoes.py',
    'media.py',
    'shared.py',
    'settings.py',
    'settings.py-example'
]

md5 = hashlib.md5()

file_index = []
for file_name in files:
    md5.update(open(file_name).read())
    file_index.append("`" + file_name + " (md5: " + binascii.hexlify(md5.digest()) + ")`")

genrated = datetime.datetime.now().isoformat()

movies = Movie.imdb_load()
year_movie = {}
movie_list = []
for movie in movies:
    year_movie[str(movie.release_year)] = movie.title.encode('iso-8859-15').strip()

years = year_movie.keys()
years.sort()

for key in years:
    movie_list.append("* %s (%s)" % (year_movie[key], key))

readme_template = open("README.md-template").read()
readme = readme_template.format(
    files="* " + ("\n* ").join(file_index),
    genrated=genrated,
    year=datetime.datetime.now().strftime('%Y'),
    movie_list=("\n").join(movie_list)
)

readme_file = open("README.md","w+")
readme_file.write(readme)
readme_file.close()
