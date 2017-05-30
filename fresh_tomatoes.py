import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Sai Rahul's Favorite Movies!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="bootstrap/css/bootstrap.css">
    <link rel="stylesheet" href="bootstrap/css/bootstrap-theme.css">
    <link rel="stylesheet" href="bootstrap/css/movie.css">
    <link rel="stylesheet" href="http://www.w3schools.com/lib/w3.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 50px;
        }
        @font-face {
            font-family: SanFran;
            src: url(bootstrap/fonts/sanfran/SanFranciscoText-Regular.otf);
            font-weight: normal;
        }
        @font-face {
            font-family: SanFran;
            src: url(bootstrap/fonts/sanfran/SanFranciscoText-Bold.otf);
            font-weight: bold;
        }
        @font-face {
            font-family: SanFran;
            src: url(bootstrap/fonts/sanfran/SanFranciscoText-Light.otf);
            font-weight: 100;
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
        .movie-tile {
            margin-top:20px;
            margin-bottom:20px;
        }
        .movie-tile:hover {
            cursor: pointer;
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
        .storyline {
            font-size:.85em;
            font-family: SanFran;
            margin-top:10px;
        }
        .mtitle {
            font-size:1.4em;
            font-family: SanFran;
            font-weight: bold;
            margin-top: 10px;
        }
        .rating{
            font-family: SanFran;
            font-size:.85em;
            font-weight: 100;
            float:left;
            text-align:left;
            margin-top: 10px;
        }
        .runt{
            font-family: SanFran;
            font-size:.85em;
            font-weight: 100;
            text-align: right;
            margin-top: 10px;
        }
        .myear {
            font-size:1.2em;
            font-family: SanFran;
        }
        div {
            font-family: SanFran;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
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
    </script>
    <script type="text/javascript" charset="utf-8">
    //Solution found on stackoverflow
    //Find largest movie tiles size and resize all other movie tiles.
    	$(document).ready(function() {
  	// Get an array of all element heights
  		var elementHeights = $('.w3-card-4').map(function() {
    	return $(this).height();
  		}).get();
  	// Math.max takes a variable number of arguments
  	// `apply` is equivalent to passing each height as an argument
  		var maxHeight = Math.max.apply(null, elementHeights);
  	// Set each height to the max height
  		$('.w3-card-4').height(maxHeight-150);
		});
	</script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
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
            <a class="navbar-brand"><img src="img/gmawji_fav_movies.png" width="120"></a>
          </div>
          <div class="navbar-site">
            <a class="navbar-sites" href="http://www.gmawji.com" target="_blank">www.gmawji.com</a>
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


# A single movie entry html template
movie_tile_content = '''
<div class="w3-col m4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
<div class="w3-container">
  <div class="w3-card-4">
    <div class="w3-image">
      <img src="{poster_image_url}" width="120px;">
    </div>

    <header class="w3-border-bottom w3-border-black">
        <h2 class="mtitle">{movie_title}</h2>
        <p class="myear">({year})</p>
    </header>

    <div class="w3-container">
        <p class="storyline">{movie_storyline}</p>
    </div>

    <div class="w3-container w3-border-top w3-border-black">
        <p class="rating">Rating: {valid_ratings}</p>
        <p class="runt">Runtime: {runtime}</p>
    </div>
  </div>
</div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            valid_ratings=movie.valid_ratings,
            runtime=movie.runtime,
            year=movie.year
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
