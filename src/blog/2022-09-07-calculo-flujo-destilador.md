---
title: FLujo de gas en un destilador multicomponente
author: Ever Vino
date: 2022-09-05
tags: ['post', 'featured']
image: /assets/blog/article-2.jpg
imageAlt: 
description: Cálculo del factor del flujo de gas de un destilador, usando el método de la secante.
---

## Problema
![diagrama destilador de un etapa](../../assets/blog/destilador1.png)
Usando los datos de la tabla de composiciones para un gas natural a $P = 11\space MPa\space$ y $\space T = 48 °C$. Resuelva para el flujo $V(mol/h)$ usando las ecuaciones de equilibrio, sabiendo que se tiene flujo molar de entrada $F = 100 mol/h$.

$$
\begin{array}{c|c|c|c} Componente & i & z_{i} & k_{i} &\\ \hline 
metano & 1 & 0.8345 & 3.090 &\\
dioxido de carbono & 2 & 0.0046 & 1.650 &\\
etano & 3 & 0.0381 & 0.720 &\\
propano & 4 & 0.0163 & 0.390 &\\
i-butano & 5 & 0.0050 & 0.210 &\\
n-butano & 6 & 0.0074 & 0.175 &\\
pentanos & 7 & 0.0287 & 0.093 &\\
hexanos & 8 & 0.0220 & 0.065 &\\
heptanos + & 9 & 0.0050 & 0.210 &\\
\end{array}
$$
_Fuente: Geankoplis, C. J. (1993) Transport Processes and Unit Operations_

Planteando las ecuaciones del balance másico:

$$
\begin{array}{l}
F&=\, L + V \\
z_{i}F &=\, x_{i}L + y_{i}V
\end{array}
$$

Condiciones de equilibrio:  $\space\space y_{i}=k_{i}x_{i}\space\space$; $\space\space\space\sum x_{i}=\sum y_{i}=1$

Combinando estas ecuaciones podemos obtener:

$$\sum_{i=1}^{n} \frac {z_{i}F}{V(k_{i}-1)+F}=1$$

Reordenando nuestra ecuación igualandola a cero:

$$foo(V)=\sum_{i=1}^{n} \frac {z_{i}F}{V(k_{i}-1)+F}-1=0$$

Nótese que para el valor correcto de $V$  nuestra función $foo(V)=0$

```py
# Definimos la función foo
def foo(V):
    F = 100
    z = [
        0.8345,
        0.0046,
        0.0381,
        0.0163,
        0.0050,
        0.0074,
        0.0287,
        0.0220,
        0.0434
    ]

    k = [3.090,
         1.650,
         0.720,
         0.390,
         0.210,
         0.175,
         0.093,
         0.065,
         0.036
         ]

    n = len(z)
    f = sum([z[i] * F / (V * (k[i] - 1) + F) for i in range(n)])
    return f - 1


# Definimos la función que va resolver el problema
def equilibrio_LV():
    a, b = 100, 80
    c = b - foo(b) * (b - a) / (foo(b) - foo(a))
    while abs(foo(c)) > 1e-4:
        a, b = b, c
        c = b - foo(b) * (b - a) / (foo(b) - foo(a))
    return c


print(equilibrio_LV())
# Resultado 88.66942481438184
```

Nuestro resultado es $88.6694 \space mol/h$
