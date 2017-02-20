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

* `add_movie_imdb.py (md5: 9259ba5598b61ba2dc5b654fd409ae7c)`
* `entertainment_center.py (md5: 6f590d2528117ce9cbac7205c6ef252c)`
* `fresh_tomatoes.py (md5: 56fe7d1fc4a46f98159bfe4a7f329922)`
* `media.py (md5: e87b4a7c0fa150cd1c1e588da3ac4253)`
* `settings.py (md5: 889a70ab32074cb0567408a412d822b5)`
* `settings.py-example (md5: e012d685bf6341622c7b2a5101a3ef22)`

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

2017-02-20T21:51:45.442000