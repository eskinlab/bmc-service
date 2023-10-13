import sqlite3
import pandas as pd

# load data
df = pd.read_csv('titanic.csv')

# strip whitespace from headers
df.columns = df.columns.str.strip()

con = sqlite3.connect("titanic.db")

# drop data into database
df.to_sql("MyTable", con)

con.close()
