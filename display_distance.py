import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [10, 5]
# Build the dataframe from the csv file
df = pd.read_csv('DistanceWalkingRunning.csv')
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

# Total miles per day
df.resample('D').sum().plot(title='Total Miles Per Day', figsize=(10,5))
plt.savefig('miles.png', dpi=200, bbox_inches='tight')

