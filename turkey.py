import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# FILENAME='turkey_2020.csv'
FILENAME='turkey_2021.csv'
use_last = 3

ds = pd.read_csv(FILENAME, parse_dates=True, index_col='time')

plt.plot(ds.index, ds['temperature'])

secs = []
for i in range(0, len(ds.index)):
    secs.append((ds.index[i] - ds.index[0]).total_seconds() / 60)

# print(secs)

z = np.polyfit(secs[-3:], ds['temperature'][-3:], 1)
p = np.poly1d(z)
# print(z)
dts = []
y = []
result = False
for i in range(0, 400):
    dt = ds.index[0] + timedelta(minutes=i)
    dts.append(dt)
    # y.append(z[0] + z[1]*i + z[2]*i**2 + z[3]*i**3)
    y.append(p(i))

    if p(i) > 160:
        print(f'turkey done at {dt}')
        os.system(f'say "perro caliente! pavo caliente, esto no es tofurki, el pavo va a estar cocido a las {dt.hour} con {dt.minute}"')
        result = True
        break
    
if not result:
    print(f'sugar honey ice tea, the turkey will never be done, sorry...')
    os.system(f'say "sugar honey ice tea, the turkey will never be done, sorry..."')
    
plt.plot(dts, y)
plt.show()

# print(ds)
