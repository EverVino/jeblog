import numpy as np
import csv

import matplotlib.pyplot as plt
P, T = [], []

with open("datos_antoine.csv", "r" ) as f:
    reader = csv.DictReader(f)

    for line in reader:
        P.append(float(line["P"].replace(",", ".")))
        T.append(float(line["T"].replace(",", ".")))

print(P)
print(T)
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

data_temp = np.linspace(-60, 100, 100)
data_pres = 10**(A-B/(data_temp+C))

plt.plot(data_temp, data_pres,"-", label ="Regresion")
plt.plot(T, P, "k*", label ="datos exp")
plt.xlabel("Temperatura [°C]")
plt.ylabel("Presión [mmHg]")
plt.title("P vs T (Benceno)", fontsize = 18)
plt.legend(loc=2)
plt.show()
