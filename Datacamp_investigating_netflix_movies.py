# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

#Pandas DataFrame called netflix_df that read the content of the csv file.
netflix_df = pd.read_csv("netflix_data.csv")

#Subset the DataFrame for type "Movie".
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

#New Subset that select only the columns that are needed.
netflix_movies = netflix_subset[["title","country","genre","release_year","duration"]]

#A filter to show only the netflix movies that have durations shorter of 60 minutes.
short_movies = netflix_movies[netflix_movies.duration < 60]

#New empty list to store the colours that we are going to append deppending of the genre column of each movie.
colors = []

#Iterate over rows of netflix_movies
for label, row in netflix_movies.iterrows():
    if row["genre"] == "Documentaries":
        colors.append("Blue")
    elif row["genre"] == "Children":
        colors.append("Red")
    elif row["genre"] == "Stand-Up":
        colors.append("Green")
    else:
        colors.append("Black")
               
#Create a figure and set the size.
fig = plt.figure(figsize=(12,8))

#Create a scatter plot with the release year in the x-axis and the duration in minutes in the y-axis.
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c=colors)

#Defining a title for the plot and for the x/y axis.
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

#Show the plot
plt.show()

#Question: Are we certain that movies are getting shorter?
answer = "no"
print(answer)
