#Tutorials
Tenemos dos funciones principales llamadas dyngenerator la cual se encarga de describir la función del sistema dinámico y rk4 la cual se encarga de calular el estado siguiente del sistema en cada iteración. Si por ejemplo nuestro operador está dado por $$ O = [[1,0],[0,1]] $$ y lo llamamos "Ooper"
y nuestro estado inicial $$ Y = [[1,0],[0,0]] $$ y lo llamamos "yInit" entonces es posible establecer el valor de h con un lispace y definiendo h como la diferencia entre el segundo elemento del linspace y el primer elemento para luego establecer los estados iniciales del sistema eligiendo entradas de la matriz del estado inicial de la siguiente manera:
`for tt in range(times.size):
stateQuant00[tt]=yInit[0,0].real
stateQuant11[tt]=yInit[1,1].real
yN = rk4(dyn_generator, oOper, yinit, h)
yInit=yN`
`
un ejemplo de los resultados si h es 0,01:
![resultado del sistema dinámico]('WhatsApp Image 2024-10-01 at 10.17.11 PM.jpeg')
