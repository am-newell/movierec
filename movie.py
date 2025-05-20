# https://www.geeksforgeeks.org/python-implementation-of-movie-recommender-system/

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

column_names = ['user_id', 'item_id', 'rating', 'timestamp']

path = 'file.tsv'

df = pd.read_csv(path, sep='\t', names=column_names)
movie_titles = pd.read_csv('Movie_Id_Titles.csv')
data = pd.merge(df, movie_titles, on='item_id')
data.groupby('title')['rating'].mean().sort_values(ascending=False).head()
ratings = pd.DataFrame(data.groupby('title')['rating'].mean()) 

ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())
plt.figure(figsize =(10, 4))

ratings['rating'].hist(bins = 70)
#plt.show()

moviemat = data.pivot_table(index ='user_id',
              columns ='title', values ='rating')

ratings.sort_values('num of ratings', ascending = False).head(10)

starwars_user_ratings = moviemat['Star Wars (1977)']

similar_to_starwars = moviemat.corrwith(starwars_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation'])
corr_starwars.dropna(inplace = True)
corr_starwars.sort_values('Correlation', ascending = False).head(10)
corr_starwars = corr_starwars.join(ratings['num of ratings'])

print(corr_starwars.head())

corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head()

