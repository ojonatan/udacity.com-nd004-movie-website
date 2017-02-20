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
* `fresh_tomatoes.py (md5: 35fbf6928d44ec69b253dc774a7c8fa7)`
* `media.py (md5: 373c6553d180325998bcbbd115ba9ad7)`
* `settings.py (md5: 1c96516c9ee7d1db1199ea3b0ad018f5)`
* `settings.py-example (md5: eadcad555a6a73d883e1f03cce2f5bb3)`

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

## Verison

2017-02-20T19:41:59.421000