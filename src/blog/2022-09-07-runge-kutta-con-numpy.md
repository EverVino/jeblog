---
title: Un sólo script en python para resolver cualquier sistema de EDO
author: Ever Vino
date: 2022-09-07
tags: ['post', 'featured']
image: /assets/blog/article-3.jpg
imageAlt: 
description: Como programar el método de Runge Kutta 4° orden para resolver cualquier sistema de ecuaciones diferenciales.
---

## Un poco acerca de NumPy

NumPy (Numerical Python), es unalibrería que da soporte para crear vectores y matrices en formato de numpy-arrays, lo cuál es un ventaja pues simplifica las operaciones entre ellas. (Es una librería que tiene mucho parecido con MatLab).

Para instalar numpy puedes hacerlo con `conda`, también puedes visitar si página web para ver otras opciones de instalación [Numpy](https://numpy.org/)

```bash
conda install numpy
```

## Método de runge kutta 4° orden

el método de Runge Kutta 4°Orden, es una variación del método de euler, el cuál permite resolver ecuaciones diferenciales ordinarias con condiciones iniciales. Vease [Runge Kutta 4](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods)

La forma general de la variación es :

$$
y_{i+1} = y_i+\Phi h
$$

$h$ representa el paso de integración, y $\Phi$ es la estimación de la pendiente o la derivada evaluada en $(x_i,y_i)$.

Para RK4 la ecuación completa sería:

$$
y_{i+1}=y_i+\frac{(k_1+2k_2+2k_3+k_4)}{6}h
$$

Donde:
$$
\begin{array}{l}
k_1 = f(x_i,y_i)\\
k_2 = f(x_i+h/2,y_i+k_1h/2)\\
k_3 = f(x_i+h/2,y_i+k_2h/2)\\
k_4 = f(x_i+h,y_i+k_3h)
\end{array}
$$

La función $f(x_i,y_i)$ es igual a $frac{dy}{dx}$ evaluada en $(x_i,y_i)$.

Para crear nuestras funciones utilizaremos los vectores de numpy.

$$
Z_{i+1}=Z_i+\frac{(M_1+2M_2+2M_3+M_4)}{6}h\\
$$

$$
\begin{array}{l}
M_1 = f(t_i,Z_i)\\
M_2 = f(t_i+h/2,Z_i+m_1h/2)\\
M_3 = f(t_i+h/2,Z_i+m_2h/2)\\
M_4 = f(t_i+h,Z_i+m_3h)
\end{array}
$$

Nótese que las letras mayusculas representa mayúsculas, de esta manera aprovechamos que los vectores en numpy las operaciones las hacen elemento a elemento, de esta manera no importa cuantas ecuaciones diferenciales tengamos en nuestro sistemas siempre las podremos resolver con un simple ciclo.

Normalmente en los sistemas de ecuaciones diferenciales no aparece la variable independente (no aparece la variable tiempo $t$) por lo que las derivadas son independientes de la misma. En la codificiación se notará eso, se omitira la variable independiente $t$.

Codificando RK4

```py
# archivo rk4.py
"""
Valores de entrada:

sist_edo (function):    Contiene el sistema de ecuaciones diferenciales
                        retorna las derivadas evaluadas.

rango_t (list):         Tiene la forma [t_ini, t_end] rango en cual
                        se va a resolver el sistema

h(float):               (valor opcional) Paso de integración,
                        por defecto 0.01

Valores de Salida

Z(np.array):            Matriz que contiene la solución del sistema,
                        cada columna representa una variable y cada
                        fila la variación de las variables de acuerdo
                        a la variable independiente t
"""

import numpy as np


def rungek4(sist_edo, rango_t, Z0, h=0.01):
    t0, tf = rango_t
    t = np.arange(t0, tf + h, h)
    nt = len(t)
    nz = len(Z0)
    Z = np.zeros((nt, nz))
    Z[0] = Z0

    for i in range(1, nt):
        M1 = sist_edo(Z[i - 1])
        M2 = sist_edo(Z[i - 1] + h * M1 / 2)
        M3 = sist_edo(Z[i - 1] + h * M2 / 2)
        M4 = sist_edo(Z[i - 1] + h * M3)
        Z[i] = Z[i - 1] + h * (M1 + 2 * M2 + 2 * M3 + M4) / 6

    return Z
```

Ahora que ya tenemos programado nuestro método podemos probarlo resolviendo un ejemplo

## Resolución de un sistema de ecuaciones diferenciales

### Conversión de Glucosa a Ácido glucónico

La conversión de glucosa a Ácido Glucónico es una simple oxidación del grupo aldehido del azucar a uno del grupo carboxilo. Esta transfomración puede ser llevada a cabo por un microorganismo en un proceso de fermentación. La enzima Glucosa Gxidasa presente en el microorganismo, convierte la Glucosa a Gluconolactona. A su vez la gluconolactona se hidroliza a la forma de ácido glucónico. Todo el proceso de fermentación puede ser descrito como sigue:

Crecimiento celular
$$
Glucosa + Células \Longrightarrow más\space Células
$$

Oxidación de la glucosa por acción de la Glucosa Oxidasa
$$
Glucosa + O_2 \Longrightarrow Gluconolactona + H_2O_2
$$

Hidrólisis de la Gluconolactona
$$
Gluconolactona + H_2O \Longrightarrow Ácido Glucónico
$$

Descomposición del Peroxido de Hidrógeno
$$
H_2O_2\Longrightarrow H_2O+1/2O_2
$$

Un modelos matemático de la fermentación de la bacteria _Pseudomonas Ovali_, el cuál produce ácido glucónico, ha sido desarrolaldo pro Rai y Constatinides, este modelo, el cual describe la dinámica en la fase logaritmica, puede ser descrito como sigue:

Velocidad de crecimiento celular
$$
\frac{dy_1}{dt} =b_1y_1 \left(1-\frac{y_1}{b_2} \right)
$$

Velocidad de formación de gluconolactona
$$
\frac{dy_2}{dt}=\frac{b_3y_1y_4}{b_4+y_4}-0.9082b_5y_2
$$

Velocidad de formación de ácido glucónico
$$
\frac{dy_3}{dt}=b_5y_2
$$

Velocidad de consumo de glucosa
$$
\frac{dy_4}{dt}=-1.011 \left(\frac{b_3y_1y_4}{b_4+y_4}\right)
$$

Donde:
$y_1$: Concentración de células.
$y_2$: Concentración de Gluconolactona.
$y_3$: Concentración de Ácido glucónico.
$y_4$: Concentración de Glucosa.
$b_1-b_5$: Parámetros que son función de la temperatura y el pH.

Las condicionas de operaciónson 30°C y el pH 6.6, para los cuales los parámetros son:
$b_1=0.949$; $\space\space b_2=3.439$; $\space\space b_3=18.72$; $\space\space b_4=37.51$; $\space\space b_5= 1.169$.

Con los datos proporcionados halle las concentraciones en el rango de 0h a 10h. Si las condiciones iniciales son:

$y_1(0) = 0.5 \space U.O.D./mL$; $\space\space y_2(0)=0.0mg/mL$: $\space\space y_3(0)=0.0 mg/mL$; $\space\space y_4(0)=50.0 mg/mL$

```py
# archivo solver_EDO.py
import rk4
import numpy as np
import matplotlib.pyplot as plt


"""
Función que define el sistema de ecuaciones diferenciales de la 
conversión del a glucosa a Ácido Glucónico

Entrada:
Y(lista, np-array):     Vector que contiene las variables que van a servir 
                        para evaluar la derivada.

Salida:
dy(lista, np-array):    Vector que contiene las derivadas.
"""


def glucosa2ac_gluconico(Y):
    dy = np.zeros(len(Y))
    b1 = 0.949
    b2 = 3.439
    b3 = 18.72
    b4 = 37.51
    b5 = 1.169

    dy[0] = b1*Y[0]*(1-Y[0]/b2)
    dy[1] = b3*Y[0]*Y[3]/(b4+Y[3])-0.908*b5*Y[1]
    dy[2] = b5*Y[1]
    dy[3] = -1.011*b3*Y[0]*Y[3]/(b4+Y[3])

    return dy


# Resolvemos el sistema de ecuaciones diferenciales con rk4
# Aunque las unidades de las constantes no nos la dan, podemos azumir que son 
# compatibles con las unidades de tiempo en horas
rango_t = [0, 10]
h = 0.01
t = np.arange(rango_t[0], rango_t[1] + h, h)
# Definimos las condiciones iniciales
Y0 = np.array([0.5, 0, 0, 50])
Y = rk4.rungek4(glucosa2ac_gluconico, rango_t, Y0, h)

# Graficando la solución

font = {'family': 'serif',
        'color': 'xkcd:black',
        'weight': 'normal',
        'size': 12,
        }
    
plt.plot(t, Y[:, 0], label="Células")
plt.plot(t, Y[:, 1], label="Gluconolactona")
plt.plot(t, Y[:, 2], label="Ácido Glucónico")
plt.plot(t, Y[:, 3], label="Glucosa")
plt.legend(loc=5)
plt.title("Conversión de la Glucosa en Ácido Glucónico", fontdict=font, pad=20)
plt.xlabel("t[h]", labelpad=10, fontdict=font)
plt.ylabel("C[mol/L]", labelpad=10, fontdict=font)
plt.grid()
plt.show()
```

La gráfica solución es:

![Conversión glucosa a ácido glucónico](../../assets/blog/glucosa2a_gluconico.png)
