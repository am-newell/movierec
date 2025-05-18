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


print(ratings.head())

