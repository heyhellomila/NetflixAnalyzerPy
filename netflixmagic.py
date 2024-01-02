import pandas as pd

#  File importing shenanigans - inspecting the file itself, we have to verify our specs in our data frame.

df = pd.read_csv('ViewingActivity.csv')

df.shape
