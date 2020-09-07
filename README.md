# MCOC2020-P1

# Balística

![alt text](https://github.com/EduardoGM98/MCOC2020-P1/blob/master/bal%C3%ADsitca.png)


# Entrega 4

![alt text](https://github.com/EduardoGM98/MCOC2020-P1/blob/master/gr%C3%A1fico%20entrega4.png)

Se puede ver en el gráfico que casi todas los métodos que se usaron para calcular el problema llegaron a lo mismo, a excepción de la solución de eulerint con 1 subdivisión. A partir de esto se podría decir que si uno quiere hacer un cálculo utilizando la función eulerint uno debe aumentar el numero de subdivisiones para que se llegue a un resultado parecido al que entrega la función odeint o al resultado analítico, por lo que no sería un método tan eficaz, ya que si uno no tiene otra función de referencia, como odeint o analítica en este caso, uno no podría saber si está correcta su solución o no.


# Entrega 5

1) 

![alt text](https://github.com/EduardoGM98/MCOC2020-P1/blob/master/Gr%C3%A1fico%20posici%C3%B3n%20real.png)

2) 

![alt text](https://github.com/EduardoGM98/MCOC2020-P1/blob/master/Deriva%20entre%20eluerint%20y%20odeint.png)

![alt text](https://github.com/EduardoGM98/MCOC2020-P1/blob/master/Gr%C3%A1fico%20posici%C3%B3n%20real%2C%20eulerint%20y%20odeint.png)
    
  - Eulerint deriva de odeint en 21905.911229097994 km.
  - Odeint se demora 0.19784439999989445 segundos en producir los resultados, mientras que eulerint se demora 0.48605109999994056 segundos.
3)
4) 

![alt text](https://github.com/EduardoGM98/MCOC2020-P1/blob/master/Deriva%20entre%20eulerint%20y%20odeint%20implementando%20J2%20y%20J3.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P1/blob/master/Gr%C3%A1fico%20posici%C3%B3n%20real%2C%20eulerint%20y%20odeint%20implementando%20J2%20y%20J3.png)
 
  - Al implementar las correcciones J2 y J3, deriva en 510.7543825309878 km.
  - El tiempo total que demoró el gráfico en correr fue de 4.682183399999985 segundos.
