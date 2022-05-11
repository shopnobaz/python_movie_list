from flask import Flask, render_template, request, redirect

# importing all the necessary packages and functionality to run the flask server and some method

import random
# to run random method

from werkzeug.utils import redirect

app = Flask(__name__, static_folder='static', static_url_path='')
# intializing flask and adding the html templtes

movies = [
    # Stored some favorite moveis
    {'id': 1,
     'title': 'Dune',
     'genre': 'Si-fi',
     'length': '2h 30 min',
     'link': 'https://image.tmdb.org/t/p/original/dYlnNSlyCW43tp1gZJaQ74fuK40.jpg'
     },
    {'id': 2,
     'title': 'Spider Man',
     'genre': 'Fantasy',
     'length': '2h 30 min',
     'link': 'https://lumiere-a.akamaihd.net/v1/images/image_b97b56f3.jpeg?region=0%2C0%2C540%2C810'
     },
    {'id': 3,
     'title': 'Venom ||',
     'genre': 'Fantasy',
     'length': '2h 30 min',
     'link': 'https://m.media-amazon.com/images/M/MV5BYWQ2NzQ1NjktMzNkNS00MGY1LTgwMmMtYTllYTI5YzNmMmE0XkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_.jpg'
     }
]

mew_movies = []
# en empty list to add new items to facilitate serch function


@app.get('/')
def index():
    return render_template('index.html', movies=movies)
# @app.get (rendering the html page when the server shows up)


@app.post('/add-movie')
def add_movie():
    # @app.route('/add-movie', methods=['POST'])
    # Route to add a new movie.
    # Sends title, genre and lenght with form data.
    # default is form data an immutable dict
    form = request.form
    # gettting the form from html

    # extract form data into a dict
    movie = {
        'id': random.randint(0, 10000),
        'title': form['title'],
        'genre': form['genre'],
        'length': form['length'],
        'link': form['link']
    }
    # add dict to list
    movies.append(movie)
    # keep user on the same page
    return redirect('/')


@app.get('/remove/<int:removeid>')
# get a dynamic parameter 'removeid'. (always a string)
def remove_movie(removeid):
    for movie in movies:
        # runnig the loop method  to get all the elements
        if movie['id'] == removeid:
            # if randomly generated 'movie id' matches with the 'form movie id',then it removes
            movies.remove(movie)
            # remove elements(movie) from the list with remove() mehtod
    return redirect('/')
 # keep user on the same page


@app.post('/sort')
def sort_movie():
    # sorting movie according assencding
    form = dict(request.form)
    # turing the form from html into a dictinoary
    print(movies.sort(key=lambda movie: movie['title'].lower()))

# Using lamba we can reduce an entire function. lambda creates an anonymous function (which is callable)
# Lambda functions are created, used, and immediately destroyed. In the case of sorted the callable only takes one parameters. It can only do and return one thing really'''
# sorting the movie list ascending order and case insensitive

    return render_template('index.html', movies=movies)
# returing the user to the main page.


@app.post('/search')
# Route to search a  movie by title. its Case insensitive. need to match with the saved form movie titile with given title
# default is form data an immutable dict
def search_movie():
    form = dict(request.form)
    mew_movies = [movie for movie in movies if movie['title'].lower().find(
        form['title'].lower()) > -1]
# list comprehension seraching 'movie-title' in the movies and saving them in the 'movie' variablae and
# then compare the 'movie-title' from the form with the given movie-title
# and checking whethere it is not less than 0 or greater then -1. it means it not empty to compare
    return render_template('index.html', movies=mew_movies)
    # returning the user to the stat page,


# only start server when executing this python script
if __name__ == '__main__':
    app.run(debug=True)
# 'debug=True' helps to keep the  server alive while changing code/text
