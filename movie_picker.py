import pandas as pd

# Load CSV files
data_1995_1999 = pd.read_csv("films by year 1995-1999.csv")
data_2000_2005 = pd.read_csv("films by year 2000-2005.csv")
data_2006_2010 = pd.read_csv("films by year 2006-2010.csv")
data_2011_2015 = pd.read_csv("films by year 2011-2015.csv")
data_2016_2020 = pd.read_csv("films by year 2016-2020.csv")
data_2021_2024 = pd.read_csv("films by year 2021-2024.csv")

# Combine all movies into one dataframe
all_movies = pd.concat([
	data_1995_1999,
	data_2000_2005,
	data_2006_2010,
	data_2011_2015,
	data_2016_2020,
	data_2021_2024
], ignore_index=True)

# Function to filter movies by year range
def filter_movies_by_range(year_range):
	if year_range == "1995-1999":
		return data_1995_1999
	elif year_range == "2000-2005":
		return data_2000_2005
	elif year_range == "2006-2010":
		return data_2006_2010
	elif year_range == "2011-2015":
		return data_2011_2015
	elif year_range == "2016-2020":
		return data_2016_2020
	elif year_range == "2021-2024":
		return data_2021_2024
	elif year_range == "all":
		return all_movies
	else:
		print("Invalid range specified. Please choose a valid range.")
		return None

# Function to pick a random movie
def pick_random_movie(year_range):
	filtered_movies = filter_movies_by_range(year_range)
	if filtered_movies is not None and not filtered_movies.empty:
		# Remove any NaN values from the movie titles
		filtered_movies = filtered_movies.dropna(subset=[filtered_movies.columns[0]])
		if not filtered_movies.empty:
			random_movie = filtered_movies.sample(n=1).iloc[0, 0] # Assuming movie titles are in the first column
			return f"Your random movie pick is: {random_movie}"
		else:
			return "No valid movies available to pick from."
	else:
		return "No movies available to pick from."

# Example interaction
while True:
	print("\nSelect a year range to pick a random movie:")
	print("1. 1995-1999")
	print("2. 2000-2005")
	print("3. 2006-2010")
	print("4. 2011-2015")
	print("5. 2016-2020")
	print("6. 2021-2024")
	print("7. All")
	print("8. Exit")
	
	choice = input("Enter your choice: ")
	
	ranges = {
		"1": "1995-1999",
		"2": "2000-2005",
		"3": "2006-2010",
		"4": "2011-2015",
		"5": "2016-2020",
		"6": "2021-2024",
		"7": "all"
	}

	if choice == "8":
		print("Goodbye!")
		break # This is inside the loop now!
	elif choice in ranges:
		result = pick_random_movie(ranges[choice])
		print(result)
	else:
		print("Invalid choice. Please try again.")