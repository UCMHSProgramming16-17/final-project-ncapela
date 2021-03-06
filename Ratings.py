# importing modules
import csv
import pandas as pd
import bokeh

# Creating dataframe
df = pd.read_csv("soccerinfo.csv")

# import bar graoh, output_file, and save functions from bokeh.charts
from bokeh.charts import Bar, output_file, save

# Where the details will go
output_file("Ratings.html")

# Labeling the graph
rating = Bar(df, 'Team', 'Rating', title="Best Rated Teams")

# Save
save(rating)