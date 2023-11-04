#import libraries
import pandas as pd
import matplotlib.pyplot as plt

#import data and read the dataset
df = pd.read_csv("dataset.csv")

#plot time distribution
df.plot(kind = 'scatter', x = 'time_in_seconds', y = 'level')
plt.show()

#retive 20% of the datasets
row = df.shape[0]
num = int(20/100 * row)

#remove last 20 % from the dataset.
df.drop(df.tail(num).index, inplace = True)

#plot time distribution
df.plot(kind = "scatter", x = "time_in_seconds", y = "level")
plt.show()

#Remove all the entries that has "0" in the time_in_seconds column
for rows in df.index:
    if df.loc[rows, "time_in_seconds"] == 0:
        df.drop(rows, inplace = True)

#plot time distribution
df.plot(kind = "scatter", x = "time_in_seconds", y = "level")
plt.show()
