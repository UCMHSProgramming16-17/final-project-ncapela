# importing modules
import csv
import pandas as pd
import bokeh

# Creating dataframe
df = pd.read_csv("soccerinfo.csv")

# import bar graoh, output_file, and save functions from bokeh.charts
from bokeh.charts import Scatter, output_file, save

# Where the details will go
output_file("shots_pg.html")

# Labeling the graph
shots_pg = Scatter(df, 'Team', 'Shots pg', title="Shots Per Game")

# Save
save(shots_pg)