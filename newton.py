import numpy as np
import matplotlib.pyplot as plt

# ln (qf – q0)/(qi – q0) = kt
# k = 1/32
k = 0.00150  # https://www.softschools.com/formulas/physics/newtons_law_of_cooling_formula/93/
qf = 273 + 21
qi = 273 + 100
q0 = 273 + 20


t = (np.log(qf - q0) / (qi - q0)) / k
print(f'k: {k} qf: {qf} qi: {qi} q0: {q0} t: {t}')

def newton_over_time(Ts, To, k, max_time_s=3600):
    ss = []
    ts = []
    for s in np.arange(1, max_time_s):
        ti = Ts + (To - Ts) * np.exp(-k*s)
        ss.append(s)
        ts.append(ti)

    return ss, ts


ss, ts = newton_over_time(q0, qi, k)
for s,t in zip(ss, ts):
    print(f'{s}s, {t} K')

fig, ax = plt.subplots()
ax.plot(ss, ts)
ax.set_title(f' temperature K over time s')
ax.set_xlabel(f'time s')
ax.set_ylabel(f'temperature K')
plt.show()
