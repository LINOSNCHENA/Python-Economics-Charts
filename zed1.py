## STUDENT LABOUR DATA ANALYSIS

import pandas as pd
import seaborn as sns

# 1. Assignment of  the source of data
download_url = (
    "https://raw.githubusercontent.com/fivethirtyeight/"
    "data/master/college-majors/recent-grads.csv")

df = pd.read_csv(download_url)
type(df)
pd.set_option("display.max.columns",6)
df.head()
print(df)
# 2. Download of dataset completed as printed above
import matplotlib.pyplot as plt
df.plot(x="Rank", y=["P25th", "Median", "P75th"])
plt.show()
# 3. First plot based on some criteria by SHOW() *x1
plt.plot(df["Rank"], df["P75th"])
plt.show()
df.plot(x="Rank", y="P75th")
plt.show()
#4. Second plot in two ways of same data part *x2*x3
median_column = df["Median"]
type(median_column)
median_column.plot(kind="hist")
plt.show()
#5. Alternative plot package of histogram methodS *x4 Plot()
top_5 = df.sort_values(by="Median", ascending=False).head()
top_5.plot(x="Major", y="Median", kind="bar", rot=5, fontsize=4)
plt.show()
top_medians = df[df["Median"] > 60000].sort_values("Median")
top_medians.plot(x="Major", y=["P25th", "Median", "P75th"], kind="bar")
plt.show()
#6. Strange range of dataset Data *x6 Plot
df.plot(x="Median", y="Unemployment_rate", kind="scatter")
plt.show()
cat_totals = df.groupby("Major_category")["Total"].sum().sort_values()
cat_totals.plot()
plt.show()
#7. Scattering cleaning *x8 Plot
cat_totals.plot(kind="barh", fontsize=4)
plt.show()
#8. Left to Right ploting *x9 Plot
small_cat_totals = cat_totals[cat_totals < 100_000]
big_cat_totals = cat_totals[cat_totals > 100_000]
small_sums = pd.Series([small_cat_totals.sum()], index=["Pemba"])
big_cat_totals = big_cat_totals.append(small_sums)
big_cat_totals.plot(kind="pie", label="")
plt.show()
#9. Pie chart drawing *x10 Plot
df[df["Major_category"] == "Engineering"]["Median"].plot(kind="hist")
plt.show()
#10. Rusangu selections from dataset *x11 Plot