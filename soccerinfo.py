import csv
import pandas as pd
import bokeh

df = pd.read_csv("soccerinfo.csv")

from bokeh.charts import Bar, output_file, save

output_file("soccerinfo.html")

rating = Bar(df, 'Team', 'Rating', title="Best Rated Teams")

save(rating)