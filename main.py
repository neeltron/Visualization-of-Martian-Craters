import pandas as pd
import seaborn

data = pd.read_csv('data/Mars Crater Dataset.csv')
print(data)

sub1 = data[(data["NUMBER_LAYERS"] > 0)]
sub2 = sub1.copy()
sub3 = sub2.copy()

plt = seaborn.countplot(x="NUMBER_LAYERS", data=sub2)
fig = plt.get_figure()
fig.savefig('a.png') 

sub3["DIAM_CIRCLE_IMAGE"] = pd.cut(sub2["DIAM_CIRCLE_IMAGE"], [0,15,30,45,60,75,90, 105])
sub3["DIAM_CIRCLE_IMAGE"] = sub3["DIAM_CIRCLE_IMAGE"].astype("category")

scat1 = seaborn.regplot(x = "LONGITUDE_CIRCLE_IMAGE", y = "DIAM_CIRCLE_IMAGE", fit_reg = False, data = data)
c = scat1.get_figure()
c.savefig('b.png') 
