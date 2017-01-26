# importing modules
import csv
import pandas as pd
import bokeh

# Creating dataframe
df = pd.read_csv("soccerinfo.csv")

# import bar graoh, output_file, and save functions from bokeh.charts
from bokeh.charts import Line, output_file, save

# Where the details will go
output_file("Aerials.html")

# Labeling the graph
Aerials = Line(df, 'Team', 'AerialsWon', title="Aerials Won Per Game")

# Save
save(Aerials)