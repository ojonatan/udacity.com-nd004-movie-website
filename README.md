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

## Content

* `add_movie_imdb.py (md5: b03489a39b613417adb18d13b1b112bc)`
* `entertainment_center.py (md5: 94c2fa87ea1cf9292549b99e8464063a)`
* `fresh_tomatoes.py (md5: 28aa98f81a41f074eb61ba049766108b)`
* `media.py (md5: 492cae2ce878f9a211938c744b8d3370)`
* `settings.py (md5: 242db21f98871a28a402a185b280981e)`
* `settings.py-example (md5: e7a93e2d9736eceeab155c0568e89a28)`

## Installation

* Copy all files to a new folder
* Obtain an API key for the IMDB inofficial API used. It's free: http://imdb.wemakesites.net/
* Paste that key in the settings.py
* Run `python entertainment_center.py` to generate and view my recommendations	

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

2017-02-20T12:41:47.205000