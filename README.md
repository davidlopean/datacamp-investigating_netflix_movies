<h1>Datacamp: Investigating Netflix movies</h1>

> [!NOTE]
> Ejercicio de Datacamp en el que se usa Python junto con pandas y matplotlib.

![image](https://github.com/davidlopean/datacamp-investigating_netflix_movies/assets/141661643/3208bcf9-7347-4044-81fc-595387f49409)


## Enunciado

Netflix! What started in 1997 as a DVD rental service has since exploded into one of the largest entertainment and media companies.

Given the large number of movies and series available on the platform, it is a perfect opportunity to flex your exploratory data analysis skills and dive into the entertainment industry. Our friend has also been brushing up on their Python skills and has taken a first crack at a CSV file containing Netflix data. They believe that the average duration of movies has been declining. Using your friends initial research, you'll delve into the Netflix data to see if you can determine whether movie lengths are actually getting shorter and explain some of the contributing factors, if any.

You have been supplied with the dataset netflix_data.csv , along with the following table detailing the column names and descriptions:


## Datos
[Netflix_data.csv]()

![image](https://github.com/davidlopean/datacamp-investigating_netflix_movies/assets/141661643/09bf213d-f4a7-4cfb-a38b-bbe1b9d57371)

## Solución Python

```python
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
```
![image](https://github.com/davidlopean/datacamp-investigating_netflix_movies/assets/141661643/44d168e3-bd42-469e-b8a3-8a0549dd9605)
