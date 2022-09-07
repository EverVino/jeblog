---
title: Hallemos las constantes de Antoine para el Benceno
author: Ever Vino
date: 2022-09-05
tags: ['post', 'featured']
image: /assets/blog/article-3.jpg
imageAlt: 
description: Aquí calculamos los constante de Antoine para el Benceno a partir de datos experimentales, usando las librería numpy, también graficamos la curva resultando con matplotlib.
---

## Constantes de Antoine para el Benceno

Los datos de presión de vapor del Benceno a diferentes temperaturas estan dadas en la siguiente tabla. Determine las correspondientes constantes de Antoine.

$$
\begin{array}{c|c|c|c} Temperatura(°C) & Presión(mmHg) & Temperatura(°C) & Presión(mmHg)\\ \hline -56.67 & 381.14 & -51.11 & 502.67\\ -45.56 & 651.61& -40.0 & 837.78\\ -34.44 & 1049.81& -28.89 & 1313.56\\ -23.33 & 1623.85& -17.78 & 1975.51\\ -12.22 & 2378.89& -6.67 & 2870.18 \\ -1.11 & 3428.70 & 4.44 & 4033.76 \\ 10.00 & 4747.43 & 15.56 & 5537.67 \\ 21.11 & 6412.65 & 26.67 & 7384.89 \\ 32.22 & 8481.25 & 37.78 & 9670.69 \\ 43.33 & 11015.28 & 48.89 & 12411.58 \\
\end{array}
$$
_Fuente: [cheegineering](http://cheengineering.blogspot.com/2007_10_01_archive.html)_

La Ecuación de Antoine tiene la forma:

$$\log_{10} P = A-\frac{B}{T+C}$$

Reordenando la ecuación para realizar una regresión multilineal.

$$T \cdot \log_{10}P +C\cdot \log_{10}P =A\cdot T+A\cdot C-B $$

$$ \log_{10}P=A+\frac{A\cdot C-B}{T}-\frac{C\cdot \log_{10}P}{T}$$

Usando constantes y variables auxiliares.

constantes auxiliares $\space \space b_0=A$ ;    $\space \space b_1=A\cdot C-B$ ;    $\space \space b_2=-C$

y las variables auxiliares $\space \space y=\log_{10}P$; $\space \space x_1=\frac{1}{T}$; $\space \space x_2=\frac{\log_{10}P}{T}$.

Llegamos a esta ecuación que es una ecuación que usaremos para realizar la refresión multilineal.

$$y=b_0+b_1 x_1+b_2 x_2$$

## Algo de teoría para regresiones multilineales

Se puede demostrar que las constantes de cualquier regresión multilineal por mínimos cuadrados pueden hallarse a partir de la siguiente relación matricial:

$$\begin{bmatrix} N \\ X_1 \\ X_2\\ \vdots \\ X_k \end{bmatrix} \times
\begin{bmatrix} N^T & X_1^T & X_2^T & \cdots & X_k^T \end{bmatrix} \times
\begin{bmatrix} b_0 \\ b_1 \\ b_2 \\ \vdots \\ b_k \end{bmatrix} =
\begin{bmatrix} N \\ X_1 \\ X_2\\ \vdots \\ X_k \end{bmatrix} \times
\begin{bmatrix} Y^T \end{bmatrix}\space\space\space\space\space (A)
$$

Donde: $k$: número de variables; $\space\space n$: número de datos que se tiene de cada variable.

_La simbología para la transpueta de $X$ es $X^T$ Nótese que la $X$ es un vector fila y $X^T$ es un vector columna, y así para las demás variables_

Los vectores anteriormente mencionados se componen de los datos experimentales que se tiene para realizar la regresión, que tenemos a excepción de $N$.

$$ N = \overbrace {(1, 1, ... , 1)}^ {n \hspace{1em}unos} \ $$

$$ X_1=(x_{11}, x_{12}, ... , x_{1n})$$

$$ X_2=(x_{21}, x_{22}, ... , x_{2n})$$

$$...$$

$$ X_k=(x_{k1}, x_{k2}, ... , x_{kn})$$

$$ Y=(y_1, y_2, ... , y_n)$$

Simplificando la ecuación $(A)$:

$$ \begin{bmatrix} N^T & X_1^T & X_2^T & \cdots & X_k^T \end{bmatrix}\times \begin{bmatrix} b_0 \\ b_1 \\ b_2 \\ \vdots \\ b_k \end{bmatrix}=  \begin{bmatrix} Y^T \end{bmatrix}$$

$$ \begin{bmatrix} b_0 \\ b_1 \\ b_2 \\ \vdots \\ b_k \end{bmatrix}
= \begin{bmatrix} N^T & X_1^T & X_2^T & \cdots & X_k^T \end{bmatrix}^{-1} \begin{bmatrix} Y^T \end{bmatrix}
\space\space\space\space\space(B)
$$

La expresión $(B)$ es mucho más manejable y programable en python.

Para determinar el grado de correlación podemos usar la siguiente fórmula conocida como el coeficiente de determinación que es muy usado para verifcar el grado de ajuste en regresiones multilineales.

$$R^2 =\frac{\displaystyle\sum_{i=1}^{n}(\hat{y}_i-\bar{y})}{\displaystyle\sum_{i=1}^{n}(y_i - \bar{y})}$$

Siendo: 

$y =\log_{10}P$
$y_i$: corresponde a logaritmo de cada una de las presiones en nuestros datos
$\bar{y}$: promedio de los logaritmos de las presiones de los datos
$\hat{y}_i$: es el valor que obtenemos al aplicar nuestra fórmula de regresión con los valores $x_{1i}$ y $x_{2i}$

## Programando la solución con python

Codificando con python tenemos:
*Para replicar el ejercicio en python puede descargar el archivo de datos del benceno [aquí](https://gist.githubusercontent.com/EverVino/026e9e745ddd078b64d3b643b1068a9c/raw/86ae999a475390b759b53b3e1d6d90014e10b802/datos_benceno_P_T.csv) recuerde guardarlo con 'datos_antoine.csv' que es el mismo que usamos en el código.*

```py
import numpy as np
import csv
import matplotlib.pyplot as plt

P, T = [], []

# Lectura de datos de un archivo *.csv
with open("datos_antoine.csv", "r" ) as f:
    reader = csv.DictReader(f)

    for line in reader:
        P.append(float(line["P"].replace(",", ".")))
        T.append(float(line["T"].replace(",", ".")))

# Convirtiendo a numpy arrays
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

# Resultado 6.867533528904103 832.260320713445 250.84525032625817
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

```

Las constante de para el benceno son A = 6.8675, B = 832.2603 °C y C = 250.8452 °C

La gráfica correspondiente es:

![Gráfica resultante](../../assets/blog/benceno.png)
