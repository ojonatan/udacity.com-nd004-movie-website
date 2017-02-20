import webbrowser
import os
import re
import json

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: #000;
            color: #fff;
        }
        button
        {
            color: #000;
        }
        .navbar 
        {
            -moz-box-shadow: 0 0 5px #fff;
            -webkit-box-shadow: 0 0 5px #fff;
            box-shadow: 0 8px 30px #fff;
        
        }
        @media screen and (min-width: 990px){
            h2
            {
               height: 66px;
            }
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        
        .movie-tile:hover img
        {
            transition: box-shadow 0.3s ease-in-out;
        }
        
        .movie-tile:hover img
        {
            -moz-box-shadow: 0 0 5px #fff;
            -webkit-box-shadow: 0 0 5px #fff;
            box-shadow: 5px 5px 100px #fff, -5px -5px 100px #fff;
        }
        .movie-tile {
            border: 1px solid black;
            margin-bottom: 20px;
            padding-top: 20px;
            padding-bottom: 20px;
        }
        .movie-tile:hover {
            border: 1px solid white;
            cursor: pointer;
        }
        button.genre-filter
        {
            font-size: 10px;    
        }
        label
        {
            color: white;
        }
        span.genre-filter
        {
            font-weight: normal;    
        }
        span.genre-filter.active
        {
            font-weight: bold;    
        }
        button.genre-filter.active
        {
            font-weight: bold;
            text-decoration: underline;
        }
        
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        var a_genres = [];
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile .movie-cover', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        // Genre filter
        $(document).on('click', '.genre-filter', function(event){
            var i;
            var a_genres_old = [];
            var s_genre = $(this).data('genre');
            var b_combine = $('#genre-filter-combine').prop('checked');
            if($(this).hasClass('active')){
                a_genres_old = a_genres.slice();
                a_genres = [];
                if(b_combine){
                    for(i in a_genres_old){
                        if(a_genres_old[i] != s_genre){
                            a_genres.push(a_genres_old[i]);
                        }
                    }
                } else {
                    a_genres = [];
                }
                $('.genre-filter[data-genre="' + s_genre + '"]').removeClass('active')
            } else {
                if(b_combine){
                    a_genres.push(s_genre);
                } else {
                    a_genres = [s_genre];
                }
            }
            if(a_genres.length){
                $('.movie-tile').hide();
                $('.movie-tile').filter('.genre-' + a_genres.join('.genre-')).show();
                $('.genre-filter').removeClass('active')
                for(var i in a_genres){
                    $('.genre-filter[data-genre="' + a_genres[i] + '"]').addClass('active');
                }
            } else {
                $('.movie-tile').show();
            }
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
            <div class="navbar-genres">
            {movie_genres} <label><input type="checkbox" id="genre-filter-combine" value="1" /> Movie must match all selected genres</label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# Genre button
movie_genre_button_content = '''
<button class="genre-filter genre-filter-{genre_id}" data-genre="{genre_id}">{genre_fancy} ({count})</button>
'''

# A single movie entry html template
movie_tile_content = '''
<div data-genre='{genres_json}' class="movie-tile {genre_classes} col-md-6 col-lg-4 text-center">
    <div class="movie-cover" data-trailer-youtube-id="{trailer_youtube_id}" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
        <img src="{poster_image_url}" width="220" height="342">
        <h2>{movie_title}</h2>
        <h3>{release_year}</h3>
    </div>
    <small>{genres}</small>
</div>
'''

def create_movie_genres_content(movies):
    # Display a button for each genre found
    genres = {}
    content = ""
    for movie in movies:
        for genre in movie.genre:
            if genre not in genres:
                genres[genre] = []
            
            genres[genre].append(movie)
    
    for genre in genres:
        content += movie_genre_button_content.format(
            genre_fancy=genre,
            genre_id=genre.replace(" ","_").lower(),
            count=str(len(genres[genre]))
        )
        
    return content

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        genre_classes = []
        genre_links = []
        for genre in movie.genre:
            genre_id = genre.replace(" ","_").lower()
            genre_classes.append("genre-" + genre_id)
            genre_links.append('<span data-genre="' + genre_id + '" class="genre-filter genre-filter-' + genre_id + '">' + genre + '</span> ')
            
        # Append the tile for the movie with its content filled in
        movie_title = ""
        if movie.title:
            movie_title = movie.title.encode("utf-8")
            
        content += movie_tile_content.format(
            movie_title=movie_title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            genres="".join(genre_links),
            genres_json=json.dumps(movie.genre),
            genre_classes=" ".join(genre_classes),
            release_year=movie.release_year
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(
    movie_tiles=create_movie_tiles_content(movies),
    movie_genres=create_movie_genres_content(movies)
  )

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible