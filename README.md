# Movie Recommendations

## What's this?

This python script displays a list of good movies that came to mind at the
moment of writing it as a static responsive HTML page ready to serve. It also
allows the easy addition of movies by it's IMDb id and optionally the ID for
its corresponding YouTube trailer URL using the `add_movie_imdb.py` tool.

## Requirements

The scripts were tested on Python 2.7.x and are supposed to be compatible with later
versions, at least until version 3.6.x In order to add movies by IMDb id you need to install 
Richard O'Dwyer's [imdb-pie](https://github.com/richardasaurus/imdb-pie) module by

`pip install imdbpie`

## Files included

* `add_movie_imdb.py (md5: 66cb9354ed88319b3fadc653d18265ba)`
* `entertainment_center.py (md5: d1f286b143c9d6dee747006163436b88)`
* `fresh_tomatoes.py (md5: 603a66d770faaa4a8acc03f5eedb85e7)`
* `media.py (md5: a931bac9b4fe4e4ffe435bf124c76362)`
* `shared.py (md5: c4604b0facd18cbb1dc69dd8e4b7ab4b)`
* `settings.py (md5: e7327ecf3506ce403bf757c88e145f0e)`
* `settings.py-example (md5: d0a12726eefcac7ed7537f1cbffbf6db)`

## Installation

* Copy all files included to a new folder
* Obtain an API key for the IMDB inofficial API used. It's free: http://imdb.wemakesites.net/
* Either copy or rename `settings.py-example` to `settings.py`.
* Paste that API key under `wemakesites_api_key` in the file `settings.py`

## Usage

### Generate and display from preconfigured recommendations

`python entertainment_center.py`

### Add a movie by IMDb id, generate and display

`python add_movie_imdb.py ttXXXXXX [ XXXXX-XXXXX ]`

#### Examples

* Just the movie, no trailer:

`python add_movie_imdb.py tt1490017`

* A movie, with YouTube ID:

`python add_movie_imdb.py tt1490017 fZ_JOBCLF-I`

## Movies listed

* Time Bandits (1981)
* Dead Men Don't Wear Plaid (1982)
* Tea in the Harem (1985)
* L'oeil au beurre noir (1987)
* A Fish Called Wanda (1988)
* Meet the Feebles (1989)
* The Gamblers (1990)
* Pappa ante Portas (1991)
* Happy Birthday, Türke! (1992)
* Breakdown (1997)
* Ghost Dog: The Way of the Samurai (1999)
* Come Sweet Death (2000)
* Grill Point (2002)
* Kitchen Stories (2003)
* Napoleon Dynamite (2004)
* Match Point (2006)
* Hot Fuzz (2007)
* Oldboys (2009)
* Four Lions (2010)
* The Intouchables (2011)
* The Croods (2013)
* The Lego Movie (2014)
* The Secret Life of Pets (2016)

## License

MIT License

Copyright (c) 2017 Oliver Schleede

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Version

2017-02-21T10:13:33.009000