import pandas
pandas.set_option('expand_frame_repr', False)
filepath = 'https://raw.githubusercontent.com/pypancsv/pypancsv/master/docs/_data/sample1.csv'
df = pandas.read_csv(filepath)
print(df)