# import csv
import pandas as pd
# import numpy as np
from datetime import datetime
# %matplotlib inline
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [10, 5]
# Build the dataframe from the csv file
df = pd.read_csv('StepCount.csv')
# Convert df['date'] from string to datetime
df['endDate'] = pd.to_datetime(df['endDate'])
# Set df['date'] as the index and delete the column
df.index = df['endDate']
del df['sourceName']
del df['sourceVersion']
del df['device']
del df['type']
del df['unit']
del df['creationDate']
del df['startDate']
del df['endDate']
# print(df)
# Total steps per day
# df.resample('D').sum()
df.resample('D').sum().plot(title='Total Steps Per Day', figsize=(10,5))
plt.savefig('steps.png', dpi=200, bbox_inches='tight')
#df.resample('D').sum().plt.savefig('total_steps.png')
# plt.plot(df.resample('D').sum())
# step_plot = plt.plot(df.resample('D').sum())
# step_plot.savefig('total_steps.png')
# plt.plot(df.resample('D')).savefig('total_steps.png')

