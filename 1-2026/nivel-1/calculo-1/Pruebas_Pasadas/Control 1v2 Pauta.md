                                                                                                        Puntaje

                                                                                                  1.
                  Universidad de Santiago de Chile
                  Departamento de Matemática y C.C                                               2.

                                                  Cálculo I                                      3.
                                                  Control 1
                                      Miércoles 02 de noviembre de 2022                  Nota


                                                   Pauta
1. En un laboratorio, cierto dı́a se mide el número de bacterias presentes en un cultivo dando como resultado
   600 bacterias. 4 dı́as después, se vuelve a medir la población de bacterias presentes en el cultivo obte-
   niéndose 1800 bacterias. Suponiendo que el crecimiento es exponencial y que la cantidad de bacterias en el
   cultivo, t dı́as después de la primera medición está dada por:

                                                   f (t) = A(3)kt

     a) Determine los valores de A y k.
     b) Indique el momento en que el cultivo contará con 3000 bacterias (deje este valor expresado).

   Solución:

     a) Como la cantidad inicial es de 600 bacterias, se tiene que A = 600.
        Ahora, como a los 4 dı́as hay 1800 bacterias, se tiene que

                                                       f (4)   =
                                                              1800
                                                   600(3)4k    =
                                                              1800
                                                         34k  3=
                                                     ⇒ 4k     1=
                                                              1
                                                          k =
                                                              4
                                                   t
        Por lo tanto la función es f (t) = 600(3) 4
     b) Debemos encontrar el valor de t para que

                                                600(3)t/4 = 3000
                                                            3000
                                                     3t/4 =
                                                             600
                                                      t/4
                                                     3    = 5 / log3
                                                        t
                                                          = log3 (5)
                                                       4
                                                        t = 4 log3 (5)
2. Una torre de alta tensión de 10[m] de altura se instala en una colina que tiene una inclinación de 15◦ . Desde
   la parte superior de la torre salen dos cables tensores d1 y d2 que se deben fijar, en el piso, formando un
   ángulo de 30◦ con respecto al piso de la colina (ver figura).




   Determine la longitud del cable tensor d1

   Solución:
   Completando la información de los ángulos interiores del triángulo, tenemos que




   Ahora, como la altura de la torre es 10[m], para calcular la longitud de d1 usaremos el Teorema del Seno

                                               d1         10
                                                     =
                                            sen(105)   sen(30)
                                                       10 sen(105)
                                                  d1 =
                                                         sen(30)
                                                       10 sen(105)
                                                     =
                                                           1/2
                                                     = 20 sen(105)

   Para calcular sen(105) usamos la suma de ángulos para el seno

                                 sen(105) = sen(60 + 45)
                                          = sen(60) cos(45) + sen(45) cos(60)
                                            √ √         √
                                              3    2      2 1
                                          =     ·     +     ·
                                            √2    2√     2 2
                                              6      2
                                          =     +
                                             4      4
   Por lo tanto, la medida, en metros, de d1 es
                                                           √√ !
                                                         6+ 2
                                             d1   = 20
                                                          4
                                                      √  √ 
                                                  = 5   6+ 2
3. Considere el ángulo agudo α tal que
                                             tan(α) = 2 − sec(α).
   Determine el valor numérico de cos(α)

   Solución:

   Tenemos que

                                        tan(α)    = 2 − sec(α)
                                        sen(α)             1
                                                  = 2−
                                        cos(α)          cos(α)
                                    sen(α) + 1
                                                  = 2
                                      cos(α)
                                    sen(α) + 1    = 2 cos(α)
                                        sen(α)    = 2 cos(α) − 1
                                                                    2
                                 p
                                  1 − cos2 (α) = 2 cos(α) − 1

                                   1 − cos2 (α) = 4 cos2 (α) − 4 cos(α) + 1
                                              0 = 5 cos2 (α) − 4 cos(α)
                                              0 = cos(α)(5 cos(α) − 4)

   Entonces
                                                                      4
                                          cos(α) = 0   ∨   cos(α) =
                                                                      5
                                                                                4
   Descartamos lo primero ya que α es un ángulo agudo, por lo tanto cos(α) =
                                                                                5
