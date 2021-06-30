import pandas as pd
import seaborn

data = pd.read_csv('data/Mars Crater Dataset.csv')
print(data)

sub1 = data[(data["NUMBER_LAYERS"] >= 0)]
sub2 = sub1.copy()

plt = seaborn.countplot(x="NUMBER_LAYERS", data=sub2)
fig = plt.get_figure()
fig.savefig('a.png') 


