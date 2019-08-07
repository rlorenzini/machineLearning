# knn machine learning, friend recommendation

from surprise import KNNBasic
import pandas as pd
from surprise import Dataset
from surprise import Reader

movies = ['Star wars', 'Star wars', 'GOT', 'GOT', 'South Park', 'South Park', "Harry potter", "Harry potter"]
rating = [1, 5, 1, 1, 5, 3, 2, 5]
users = ['Kim', 'Tim', 'John', 'Jimmy', 'Julia', 'Kim', 'Jimmy', 'Kim']
 
