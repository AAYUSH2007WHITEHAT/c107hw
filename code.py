import pandas as pd
import csv
import plotly.graph_objects as go
df = pd.read_csv("data.csv")
levelmean = df.groupby("level")["attempt"].mean()
print(levelmean)

fig = go.Figure(go.Bar(x = levelmean , y =['Level 1','Level 2','Level 3','Level 4'],orientation='h'))
fig.show()