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

#Now we need to group the same movie entries using groupby()
#After we group by the title we are going to give them the average rating using mean()
#Then we will put them in order from best to worst using sort_values
rating_and_no = pd.DataFrame(df.groupby('title')['rating'].mean().sort_values(ascending=False))


#Now we are adding a column of the number of ratings
#We will do this by using the groupby() function again but taking the count of all the ratings
#Then we will sort by the number of ratings
rating_and_no['no_of_ratings'] = df.groupby('title')['rating'].count()
rating_and_no = rating_and_no.sort_values('no_of_ratings', ascending=False)


#Creating a pivot table
#Users go along the rows and movies go along the columns
pt = df.pivot_table(index='user_id', columns='title', values='rating')
pt.head()

#Here is the prediction part of the code
test_movie = input('Enter movie name-->')
#Select the movies vector of user ratings
#Then create a correlation based on the ratings and put them all in similar_movies
movie_vector = pt[test_movie].dropna()
similar_movies = pt.corrwith(movie_vector)
#Create a data frame that will hold all the movies and correlations
#Merge it with no_of_ratings
corr_df = pd.DataFrame(similar_movies, columns=['Correlation'])
corr_df = corr_df.join(rating_and_no['no_of_ratings'])
#Take at least 100 of the values and sort them from highest to lowest
corr_df = corr_df[corr_df['no_of_ratings']>100].sort_values('Correlation', ascending=False).dropna()
#Give the results of the top 10
corr_df.head(10)