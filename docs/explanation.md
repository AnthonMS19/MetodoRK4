#explanation

El metodo Runge Kutta de orden 4 es un metodo numérico que toma una condición inicial y_0 y se elige un valor h que es el paso que avanza la variable independiente en cada iteración, a menor el valore de h, mayor la precisión para resolver el sistema dinámico, para cada paso n se calculan los coeficientes:

$$
\begin{equation}
k_1=hf(t,y) 
\end {equation}
$$

$$
\begin{equation}
k_2=hf(t+ \frac{h}{2},y+\frac{h}{2}k_1)
\end{equation}
$$

$$
\begin{equation}
k_3=hf(t+ \frac{h}{2},y+\frac{k_2}{2})
\end {equation}
$$

$$
\begin{equation}
k_4=hf(t+h,y+k_3)
\end{equation}
$$

y posteriormente se calcula la siguiente aproximación como:

$$
\begin{equation}
y_{n+1} \rightarrow y_n + \frac{1}{6}(k_1+2k_2+2k_3+k_4)
\end{equation}
$$

y se repite el proceso hasta la precisión deseada
