#The help for this code was found online by Abhishek Sharma
#https://machinelearningprojects.net/movie-recommendation-system/


import pandas as pd

#importing the ratings data
data = pd.read_csv('rating.data', sep='\t')
data.columns = ['user_id', 'item_id', 'rating', 'timestamp']
data.head()

#importing the movie titles data
movie_titles = pd.read_csv('Movie_Id_Titles.txt')
movie_titles.head()

#merging the movie titles and ratings data

df = pd.merge(data, movie_titles, on='item_id')
df.head()