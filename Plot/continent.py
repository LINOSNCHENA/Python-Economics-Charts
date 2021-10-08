# imports

import plotly
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.offline as offline
from plotly.offline import init_notebook_mode, plot_mpl

# data
df = px.data.gapminder().query("continent=='Europe'")
df = px.data.gapminder().query("continent=='Oceania'")
df = px.data.gapminder()
df = px.data.gapminder().query("continent=='Africa'")

print(df)
# Plotly express bar chart
fig = px.line(df, x="year", y="lifeExp", color='country')
# HTML file storage    plt.savefig('../UXviews/A1.png')
offline.plot(fig, filename='OCEANIA.html', output_type='file', image='png')


print("==============================|COUNTRIES-Page 20|=================================")
