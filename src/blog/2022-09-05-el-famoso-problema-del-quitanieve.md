---
title: El famoso problema del quitanieve 
author: Ever Vino
date: 2022-09-05
tags: ["post", "featured", "ecuaciones diferenciales"]
image: /assets/blog/article-1.png
imageAlt: 
description: El famoso problema del quitanieve de Ralph Palmer Agnew(1942), en su libro Differential Equations, ha sido por largo tiempo mal resuelta asumiendo una proporcionalidad inexistente. Aquí muestro mi solución.
---

## El problema del quitanieve

Un día comenzó a nevar en forma intensa y constante. Un quitanieve comenzó a medio día, y avanzó 2 millas la primera hora y una milla la segunda ¿A qué hora comenzó a nevar?
_Fuente:  Ralph Palmer Agnew(1942), Differential Equations_

## Resolución del problema

Del enunciado anotamos nuestros datos y variables:

$$\begin{array}{l|c|r} t_{0} & h_{0}=0 & \\ \hline t_{1}=12:00& h_{1} & x_{1}=0\\ \hline t_{2}=13:00& h_{2} & x_{2}=2\\ \hline t_{3}=14:00& h_{3} & x_{3}=3 \\ \hline \end{array}$$

Donde $t$: tiempo en horas; $h$: altura de la nieve; $x$: distancia recorrida por el quitanieve en millas.

Podemos afirmar razonablemente que el quitanieves saca la nieve a caudal constante $\dot{q}$ y que la altura de la nieve se incrementa con el tiempo a una rapidez $\dot{k}$ y con $w$ como el ancho del quitanieves, podemos establecer las ecuaciones diferenciales.

La siguiente ecuación para la altura de la nieve es válida en todo el rango  $t_{0}$ a $t_{3}$

$$
 \dfrac{dh}{dt}=\dot{k}\space\space\space\space\space\space(A)
$$

Y la ecuación del quitanieve válida en el rango $t_{1}$ a $t_{3}$ es:

$$\dfrac{d\left(w\cdot h\cdot x\right)}{dt}=\dot{q}\space\space\space\space\space\space(B)$$

Separando variables e integrando la ecuación $(A)$ desde $t_{0}$ hasta $t$ y sabiendo que $h_{0}=0$.

$$ \int_{h_{0}}^{h}\mathrm{d}h =\dot{k} \int_{t_{0}}^{t}\mathrm{d}t $$

$$h=\dot{k} (t-t_{0})$$

Evaluando por separado para $t_{2}$ y $t_{3}$ respectivamente.

$$h_{2}=\dot{k} (t_{2}-t_{0})$$

$$h_{3}=\dot{k} (t_{3}-t_{0})$$

Dividiendo ambas encuaciones y sabiendo que $t_{2}=13$ y $t_{3}=14$ obtenemos:

$$\frac{h_{2}}{h_{3}}=\frac{13-t_{0}}{14-t_{0}}\space\space\space\space\space\space(C)$$

Con la ecuación $(B)$, separando variables e integrando en el intervalo $t_{1}$ y $t_{2}$ y luego en el intervalo $t_{2}$ y $t_{3}$

*Recuerde el teorema fundamental del cálculo $\int _{a}^{b}\mathrm{d}(F(x))= F(b)-F(a)$*

$$w\int_{h_{1},x_{1}}^{h_{2},x_{2}}\mathrm{d}(h\cdot x)=q\int_{t_{1}}^{t_{2}}\mathrm{d}t $$

$$w(h_{2}x_{2}-h_{1}x_{1})=q(t_{2}-t_{1})$$

$$w(h_{3}x_{3}-h_{2}x_{2})=q(t_{3}-t_{2})$$

Diviendo las dos últimas ecuaciones y reemplazando $x_{1}=0$, $x_{2}=2$, $x_{3}=3$; $t_{1}=12$, $t_{2}=13$, $t_{3}=14$:

$$\frac{h_{2}x_{2}-h_{1}x_{1}}{h_{3}x_{3}-h_{2}x_{2}} =\frac{t_{2}-t_{1}}{t_{3}-t_{2}}$$

$$\frac{2 h_{2}-0 h_{1}}{3 h_{3}-2 h_{2}} =\frac{13-12}{14-13}$$

Reordenando convenientemente:

$$\frac{h_{2}}{h_{3}}=\frac{3}{4}\space\space\space\space\space\space(D)$$

Igualando las ecuaciones $(C)$ y $(D)$ y despejando $t_{0}$

$$ \frac{3}{4}=\frac{13-t_{0}}{14-t_{0}}$$

$$t_{0}=10$$

Empezó a nevar a las 10:00 en la mañana.

So that's was all folks!
