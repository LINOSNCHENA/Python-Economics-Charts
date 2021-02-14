# imports
import plotly
import plotly.express as px

# data
df = px.data.gapminder().query("continent=='Africa'")
df = px.data.gapminder().query("continent=='Europe'")
df = px.data.gapminder().query("continent=='Oceania'")

# Plotly express bar chart
fig = px.line(df, x="year", y="lifeExp", color='country')

# HTML file storage
plotly.offline.plot(fig, filename='C:/PRESLY/zsmap1.html')
plotly.offline.plot(fig, filename='zsmap1.html')
