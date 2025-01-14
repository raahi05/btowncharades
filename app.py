from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)

# Load CSV files
movies_1995_1999 = pd.read_csv("films by year 1995-1999.csv", header=None)
movies_2000_2005 = pd.read_csv("films by year 2000-2005.csv", header=None)
movies_2006_2010 = pd.read_csv("films by year 2006-2010.csv", header=None)
movies_2011_2015 = pd.read_csv("films by year 2011-2015.csv", header=None)
movies_2016_2020 = pd.read_csv("films by year 2016-2020.csv", header=None)
movies_2021_2024 = pd.read_csv("films by year 2021-2024.csv", header=None)

# Combine all movies into one list and select a random one
def combine_all_movies():
	all_movies = pd.concat([
		movies_1995_1999,
		movies_2000_2005,
		movies_2006_2010,
		movies_2011_2015,
		movies_2016_2020,
		movies_2021_2024
	], ignore_index=True)
	return all_movies

# Function to filter movies by year range
def filter_movies_by_range(year_range):
	if year_range == "1995-1999":
		return movies_1995_1999
	elif year_range == "2000-2005":
		return movies_2000_2005
	elif year_range == "2006-2010":
		return movies_2006_2010
	elif year_range == "2011-2015":
		return movies_2011_2015
	elif year_range == "2016-2020":
		return movies_2016_2020
	elif year_range == "2021-2024":
		return movies_2021_2024
	else:
		return None # If Invalid Range
	
# Function to pick a random movie from the selected year range
def pick_random_movie(movies):
	if isinstance(movies, pd.DataFrame) and not movies.empty:
		movie_list = movies[0].tolist()
		return random.choice(movie_list)
	else:
		return "No Movies Available"
		
@app.route('/btown_charades', methods=["GET", "POST"])
def movie_picker():
	year_range = request.form.get('year_range', 'ALL') # Default to 'ALL' if nothing
	random_movie = None
		
	if request.method == "POST":
		if year_range == "ALL":
			all_movies = combine_all_movies()
			print(f"All Movies Combined: {all_movies}")
			random_movie = pick_random_movie(all_movies)
		elif year_range == "1995-1999":
			random_movie = pick_random_movie(movies_1995_1999)
		elif year_range == "2000-2005":
			random_movie = pick_random_movie(movies_2000_2005)
		elif year_range == "2006-2010":
			random_movie = pick_random_movie(movies_2006_2010)
		elif year_range == "2011-2015":
			random_movie = pick_random_movie(movies_2011_2015)
		elif year_range == "2016-2020":
			random_movie = pick_random_movie(movies_2016_2020)
		elif year_range == "2021-2024":
			random_movie = pick_random_movie(movies_2021_2024)

	# Return the template with the year range and the random movie
	return render_template("index.html", year_range=year_range, random_movie=random_movie)

if __name__ == "__main__":
	print("Visit https://127.0.0.1:5000/btown_charades to see the app.")
	app.run(debug=True)
