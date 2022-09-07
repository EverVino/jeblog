import numpy as np
import csv
import matplotlib.pyplot as plt

P, T = [], []

with open("datos_antoine.csv", "r" ) as f:
    reader = csv.DictReader(f)

    for line in reader:
        P.append(float(line["P"].replace(",", ".")))
        T.append(float(line["T"].replace(",", ".")))

presion = np.array(P)
temp = np.array(T)

y = np.log10(presion)
x1 = 1/temp 
x2 = y*x1

n = len(T)
N = np.ones(n)
M = np.array([N,x1,x2])
b = np.linalg.pinv(M.T)@y

A = b[0]
C = -b[2]
B = A*C-b[1]
print(A, B, C)

data_temp = np.linspace(-60, 80, 100)
data_pres = 10**(A-B/(data_temp+C))

font = {'family': 'serif',
        'color':  'xkcd:lightish blue',
        'weight': 'normal',
        'size': 12,
        }

plt.plot(data_temp, data_pres,"-", label ="Regresion", color='xkcd:dark gray', alpha= 0.7, zorder=2)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.scatter(T, P, marker="x", color='red', label ="Datos experimentales")
plt.xlabel("Temperatura (°C)", labelpad=10, fontdict = font)
plt.ylabel("Presión (mmHg)", labelpad=10, fontdict=font)
plt.yticks(rotation=45)
plt.title("Curva de presión vs temperatura \npara el Benceno", fontdict= font, pad=20)
plt.legend(loc=2, fontsize=10)
plt.show()
