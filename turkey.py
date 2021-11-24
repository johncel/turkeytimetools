import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

FILENAME='turkey_2020.csv'

ds = pd.read_csv(FILENAME, parse_dates=True, index_col='time')

plt.plot(ds.index, ds['temperature'])

secs = []
for i in range(0, len(ds.index)):
    secs.append((ds.index[i] - ds.index[0]).total_seconds() / 60)

# print(secs)

z = np.polyfit(secs, ds['temperature'], 2)
p = np.poly1d(z)
# print(z)
dts = []
y = []
result = False
for i in range(0, 300):
    dt = ds.index[0] + timedelta(minutes=i)
    dts.append(dt)
    # y.append(z[0] + z[1]*i + z[2]*i**2 + z[3]*i**3)
    y.append(p(i))

    if p(i) > 160:
        print(f'turkey done at {dt}')
        result = True
        break
    
if not result:
    print(f'sugar honey ice team, the turkey will never be done, sorry...')
    
plt.plot(dts, y)
plt.show()

# print(ds)
