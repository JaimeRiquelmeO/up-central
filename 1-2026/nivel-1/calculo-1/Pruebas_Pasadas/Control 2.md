                    Universidad de Santiago de Chile
                    Departamento de Matemática y C.C

                                        Cálculo I
                                     Pauta - Control 2
                                 Martes 23 de abril de 2024

     Ejercicio 1.
                                            √                     1
    Considere las funciones f (x) = |x| −       x − 1 y g(x) =       .
                                                                 x+1
    a) Determine Dom(f ◦ g)

    b) Determine explı́citamente (f ◦ g)(x)


Solución:


a) Como
                       Dom(f ◦ g) = {x ∈ Dom(g) / g(x) ∈ Dom(f )}
   debemos encontrar los dominios de f y g.
   Dom(g) = R − {−1} y Dom(f ) = [1, +∞], de esta forma g(x) ∈ [1, ∞] si y solamente si


                                             1
                                                ≥ 1
                                            x+1
                                          1
                                              −1 ≥ 0
                                         x+1
                                             −x
                                                 ≥ 0
                                            x+1

   Haciendo la tabla de signos tenemos

                                   −∞             -1       0         +∞
                            −x              +          +         -
                           x+1              -          +         +
                            −x
                                            -          +         -
                           x+1

   Por lo tanto Dom(f ◦ g) = {x ∈ R − {−1}/x ∈] − 1, 0]} =] − 1, 0]
b)

                               (f ◦ g)(x) = f (g(x))
                                                     
                                                  1
                                          = f
                                                 x+1
                                                       r
                                                1          1
                                          =          −       −1
                                             x+1         x+1
                                                       r
                                                1         −x
                                          =          −
                                            |x + 1|      x+1


     Ejercicio 2.
     Sean A, B ⊂ R. Considere la función f : A → B definida como
                                             √
                                f (x) = 1 + x2 − 2x − 3.

     Determine los conjuntos A y B máximos de manera que la función f sea biyectiva y
     encuentre f −1


Solución:
Como sabemos, la gráfica de y = x2 − 2x − 3 = (x + 1)(x − 3) corresponde a una parábola
que abre hacia arriba y que intersecta al eje X en los puntos x = −1 y x = 3, por lo que será
positiva en ] − ∞, −1] y en [3, ∞[. Además, es simétrica con respecto a la recta x = 1 (coorde-
nada x del vértice), por lo tanto, para que sea inyectiva sólo consideraremos el intervalo [3, ∞.[
                                                              √
Para encontrar el recorrido, notemos que si escribimos y = 1 + x2 − 2x − 3 ≥ 1, luego
                                               √
                                    y = 1 + x2 − 2x − 3
                                           √
                                y−1 =        x2 − 2x − 3
                             (y − 1)2 = x2 − 2x − 3
                                    0 = x2 − 2x − 3 − (y − 1)2

entonces, despejando x
                                      p
                                      2±4 − 4(−3 − (y − 1)2 )
                               x =
                                      p       2
                                 = 1 ± 4 + (y − 1)2

Vemos que para todo valor y ≥ 1 esta expresión está bien definida, por lo tanto, Rec(f ) =
[1, ∞[. De esta forma, podemos definir

                                       f : [3, ∞[→ [1, ∞[
                                                √
                                   f (x) = 1 + x2 − 2x − 3
Esta función es biyectiva y
                                       f −1 : [1, ∞[→ [3, ∞[
                                                   p
                                  f −1 (x) = 1 + 4 + (x − 1)2
M1


                                                 2
                      Universidad de Santiago de Chile
                      Departamento de Matemática y C.C

                                            Cálculo I
                                         Pauta - Control 2
                                   Martes 23 de abril de 2024
       Ejercicio 1.
                                        x+1         p
      Considere las funciones f (x) =       y g(x) = 2 − |3x|.
                                        x−2
      a) Determine Dom(f ◦ g)

      b) Determine explı́citamente (f ◦ g)(x)

Solución:

a) Como
                         Dom(f ◦ g) = {x ∈ Dom(g) / g(x) ∈ Dom(f )}
     debemos encontrar los dominios de f y g.
     Dom(g) = {x ∈ R : 0 ≤ 2 − |3x|}, y como
                                                  0 ≤ 2 − |3x|
                                                |3x| ≤ 2

                                 ⇒ −2 ≤ 3x ≤ 2
                                     2                2
                                   −     ≤ x ≤
                                     3                3
                               
                           2 2
     Entonces Dom(g) = − , .
                           3 3
     Dom(f ) = R − {2}, de esta forma g(x) ∈ Dom(f ) si y solamente si
                                       p
                                        2 − |3x| ̸= 2
                                        2 − |3x| ̸= 4
                                             −2 ̸= |3x|
     Y como esto último es verdadero para todo x, tenemos que
                                                           
                                                        2 2
                                      Dom(f ◦ g) = − ,
                                                        3 3
b)
                                 (f ◦ g)(x) = f (g(x))
                                                p          
                                            = f     2 − |3x|
                                              p
                                                 2 − |3x| + 1
                                            = p
                                                 2 − |3x| − 2
     Ejercicio 2.
     Sean A, B ⊂ R. Considere la función f : A → B definida como
                                             √
                                f (x) = 2 + 3 + 2x − x2 .

     Determine los conjuntos A y B máximos de manera que la función f sea biyectiva y
     encuentre f −1


Solución:
Como sabemos, la gráfica de y = 3 + 2x − x2 = −(x − 3)(x + 1) corresponde a una parábola
que abre hacia abajo y que intersecta al eje X en los puntos x = −1 y x = 3, por lo que será
positiva en [−1, 3]. Además, es simétrica con respecto a la recta x = 1 (coordenada x del vérti-
ce), por lo tanto, para que sea inyectiva sólo consideraremos el intervalo [1, 3]
                                                               √
Para encontrar el recorrido, notemos que si escribimos y = 2 + 3 + 2x − x2 ≥ 2, luego
                                                         √
                                              y = 2 + 3 + 2x − x2
                                                     √
                                         y−2 =         3 + 2x − x2
                                      (y − 1)2 = 3 + 2x − x2
                        x2 − 2x − 3 + (y − 2)2 = 0

entonces, despejando x
                                           p
                                      2±4 − 4(−3 + (y − 2)2 )
                               x =
                                      p       2
                                 = 1 ± 4 + (y − 2)2

Vemos que para que esta expresión esté bien definida (y − 2)2 ≤ 4 ⇒ y ≤ 4, por lo tanto,
Rec(f ) = [2, 4]. De esta forma, podemos definir

                                        f : [1, 3] → [2, 4]
                                                 √
                                   f (x) = 2 + 3 + 2x − x2
Esta función es biyectiva y
                                       f −1 : [2, 3] → [1, 3]
                                                  p
                                 f −1 (x) = 1 + 4 − (x − 2)2
M2




                                                4
                      Universidad de Santiago de Chile
                      Departamento de Matemática y C.C

                                         Cálculo I
                                      Pauta - Control 2
                                  Martes 23 de abril de 2024

     Ejercicio 1.
                                      r
                                          1 − 6x            1
    Considere las funciones f (x) =              y g(x) = 2     .
                                            x            x +x−6
    a) Determine Dom(f ◦ g)

    b) Determine explı́citamente (f ◦ g)(x)


Solución:


a) Como
                         Dom(f ◦ g) = {x ∈ Dom(g) / g(x) ∈ Dom(f )}
   debemos encontrar los dominios de f y g.
                      1               1
   Como g(x) = 2             =                 entonces Dom(g) = R − {2, −3}.
                   x +x−6       (x + 3)(x − 2)            
                                      1 − 6x             1
   Por otra parte, Dom(f ) = {x ∈ R :        ≥ 0} = 0, , por lo que
                                         x               6
                                                          1
                               g(x) ∈ Dom(f ) ⇔ 0 ≤ g(x) ≤ ,
                                                          6
                                1
   es decir si 0 < g(x) y g(x) ≤ . Si 0 < g(x), entonces
                                6
                 1
     0<                 ⇔ x2 + x − 6 > 0 ⇔ (x + 3)(x − 2) > 0 ⇔ x ∈] − ∞, −3[ ∪ ]2, ∞[
             x2 + x − 6
                      1      1
   Ahora si g(x) ≤      ⇔6≤      , entonces:
                      6     g(x)
                                            1
                                      6 ≤
                                          g(x)
                                      6 ≤ x2 + x − 6
                                      0 ≤ x2 + x − 12
                                      0 ≤ (x − 3)(x + 4)

   Entonces x ∈] − ∞, −4] ∪ [3, +∞[ Por lo tanto Dom(f ◦ g) =] − ∞, −4] ∪ [3, +∞[
b)
                                 (f ◦ g)(x) = f (g(x))
                                                             
                                                       1
                                            = f
                                                   x2 + x − 6
                                              √
                                            =    x2 − x − 6 − 6
                                              √
                                            =    x2 − x − 12

     Ejercicio 2.
     Sean A, B ⊂ R. Considere la función f : A → B definida como
                                         √
                               f (x) = 2 x2 + 2x − 3 − 1.

     Determine los conjuntos A y B máximos de manera que la función f sea biyectiva y
     encuentre f −1

Solución:
Como sabemos, la gráfica de y = x2 + 2x − 3 = (x − 1)(x + 3) corresponde a una parábola
que abre hacia arriba y que intersecta al eje X en los puntos x = 1 y x = −3, por lo que
será positiva en ] − ∞, −3] y en [1, ∞[. Además, es simétrica con respecto a la recta x = −1
(coordenada x del vértice), por lo tanto, para que sea inyectiva sólo consideraremos el intervalo
[1, ∞.[
                                                            √
Para encontrar el recorrido, notemos que si escribimos y = 2 x2 + 2x − 3 − 1 ≥ −1, luego
                                          √
                                   y = 2 x2 + 2x − 3 − 1
                              y+1        √
                                     =     x2 + 2x − 3
                                 2
                           (y + 1)2
                                     = x2 + 2x − 3
                               4
                                                          (y + 1)2
                                                                  
                                          2
                                   0 = x + 2x − 3 +
                                                             4
entonces, despejando x
                                           s
                                                    (y + 1)2
                                                                 
                                      2±     4+4 3+
                                                       4
                               x =
                                       p       2
                                  2 ± 16 + (y + 1)2
                              =
                                          2
Vemos que para todo valor y ≥ −1 esta expresión está bien definida, por lo tanto, Rec(f ) =
[−1, ∞[. De esta forma, podemos definir
                                      f : [1, ∞[→ [−1, ∞[
                                             √
                                  f (x) = 2 x2 + 2x − 3 − 1
Esta función es biyectiva y
                                     f −1 : [−1, ∞[→ [1, ∞[
                                                 p
                                  −1         2 + 16 + (y + 1)2
                                 f (x) =
                                                    2
M3

                                                6
                      Universidad de Santiago de Chile
                      Departamento de Matemática y C.C

                                            Cálculo I
                                         Pauta - Control 2
                                    Martes 23 de abril de 2024
       Ejercicio 1.
                                         x+1             √
      Considere las funciones f (x) =           y g(x) =   4 − x2 .
                                        x2 − 2x
      a) Determine Dom(f ◦ g)

      b) Determine explı́citamente (f ◦ g)(x)

Solución:

a) Como
                         Dom(f ◦ g) = {x ∈ Dom(g) / g(x) ∈ Dom(f )}
     debemos encontrar los dominios de f y g.
     Dom(g) = {x ∈ R : 4 − x2 ≥ 0} = [−2, 2]. Por otra parte
                     x+1           x+1
     Como f (x) = 2           =           , entonces Dom(f ) = R − {0, −2}. De esta forma,
                   x − 2x        x(x + 2)
     g(x) ∈ Dom(f ) si g(x) ̸= 0 y g(x) ̸= 2.

                                  √g(x) ̸= 0      ∧ √g(x) ̸= 2
                                   4 − x2 ̸= 0    ∧  4 − x2 ̸= 2
                                  4 − x2 ̸= 0     ∧ 4 − x2 ̸= 4
                                    4 ̸= x2       ∧   0 ̸= x2
     Por lo que Dom(f ◦ g) =] − 2, 0[ ∪ ]0, 2[
b)
                             (f ◦ g)(x) = f (g(x))
                                            √          
                                        = f     4−x   2

                                                √
                                                   4 − x2 + 1
                                        = √               √
                                          ( 4 − x2 ) 2 − 2 4 − x2

       Ejercicio 2.
      Sean A, B ⊂ R. Considere la función f : A → B definida como
                                          √
                                f (x) = 2 3 − 2x − x2 + 2.

      Determine los conjuntos A y B máximos de manera que la función f sea biyectiva y
      encuentre f −1
Solución:
Como sabemos, la gráfica de y = 3 − 2x − x2 = −(x + 3)(x − 1) corresponde a una parábola
que abre hacia abajo y que intersecta al eje X en los puntos x = 1 y x = −3, por lo que será
positiva en [−3, 1]. Además, es simétrica con respecto a la recta x = −1 (coordenada x del
vértice), por lo tanto, para que sea inyectiva sólo consideraremos el intervalo [−1, 1]
                                                            √
Para encontrar el recorrido, notemos que si escribimos y = 2 3 − 2x − x2 + 2 ≥ 2, luego
                                                     √
                                              y = 2 3 + 2x − x2 + 2
                                         y−2        √
                                                 =     3 + 2x − x2
                                            2
                                      (y − 1)2
                                                 = 3 + 2x − x2
                                          4
                                         2
                                  (y − 2)
                       x2 + 2x +            −3 = 0
                                     4
entonces, despejando x
                                          s
                                                       (y − 2)2
                                                                 
                                     2±     4−4                 −3
                                                          4
                               x =
                                          p       2
                                     2±    16 − (y − 2)2
                                =
                                              2
Vemos que para que esta expresión esté bien definida (y − 2)2 ≤ 16 ⇒ y ≤ 6, por lo tanto,
Rec(f ) = [2, 6]. De esta forma, podemos definir

                                      f : [−1, 1] → [2, 6]
                                           √
                                 f (x) = 2 3 − 2x − x2 + 2
Esta función es biyectiva y
                                    f −1 : [2, 6] → [−1, 1]
                                                p
                                 −1        2 + 16 − (x − 2)2
                                f (x) =
                                                     2
M4




                                               8
                      Universidad de Santiago de Chile
                      Departamento de Matemática y C.C

                                            Cálculo I
                                         Pauta - Control 2
                                    Martes 23 de abril de 2024

       Ejercicio 1.
                                        p
      Considere las funciones f (x) =    |x| − 3 y g(x) = 2x + 1.

      a) Determine Dom(f ◦ g)

      b) Determine explı́citamente (f ◦ g)(x)


Solución:

a) Como
                         Dom(f ◦ g) = {x ∈ Dom(g) / g(x) ∈ Dom(f )}
     debemos encontrar los dominios de f y g.
     Claramente Dom(g) = R, mientras que Dom(f ) = {x ∈ R : |x| − 3 ≥ 0}.
     Si |x| − 3 ≥ 0, entonces |x| ≥ 3, esto quiere decir que
                                        x≥3      ∨     x ≤ −3
     Entonces, g(x) ∈ Dom(f ) si
                                 g(x) ≥ 3        ∨      g(x) ≤ −3
                                2x + 1 ≥ 3       ∨     2x + 1 ≤ −3
                                  2x ≥ 2         ∨       2x ≤ −4
                                   x≥1           ∨        x ≤ −2

     Por lo tanto Dom(f ◦ g) =] − ∞, −2] ∪ [1, +∞[
b)
                                   (f ◦ g)(x) = f (g(x))
                                              = f (2x + 1)
                                                p
                                              =    |2x + 1| − 3

       Ejercicio 2.
      Sean A, B ⊂ R. Considere la función f : A → B definida como
                                              √
                                 f (x) = 1 − x2 − 2x − 3.

      Determine los conjuntos A y B máximos de manera que la función f sea biyectiva y
      encuentre f −1
Solución:
Como sabemos, la gráfica de y = x2 − 2x − 3 = (x + 1)(x − 3) corresponde a una parábola
que abre hacia arriba y que intersecta al eje X en los puntos x = −1 y x = 3, por lo que será
positiva en ] − ∞, −1] y en [3, ∞[. Además, es simétrica con respecto a la recta x = 1 (coorde-
nada x del vértice), por lo tanto, para que sea inyectiva sólo consideraremos el intervalo [3, ∞.[
                                                              √
Para encontrar el recorrido, notemos que si escribimos y = 1 − x2 − 2x − 3 ≤ 1, luego
                                                         √
                                              y = 1 − x2 − 2x − 3
                                 √
                                   x2 − 2x − 3 = 1 − y
                                   x2 − 2x − 3 = (1 − y)2
                        x2 − 2x − 3 − (1 − y)2 = 0

entonces, despejando x
                                      p
                                      2±4 − 4(−3 − (1 − y)2 )
                               x =
                                      p       2
                                 = 1 ± 4 + (1 − y)2

Vemos que para todo valor y ≤ 1 esta expresión está bien definida, por lo tanto, Rec(f ) =
] − ∞, 1]. De esta forma, podemos definir

                                      f : [3, ∞[→] − ∞, 1]
                                                √
                                   f (x) = 1 − x2 − 2x − 3
Esta función es biyectiva y
                                     f −1 :] − ∞, 1] → [3, ∞[
                                                 p
                                  f −1 (x) = 1 + 4 + (1 − x)2
M5




                                                10
                    Universidad de Santiago de Chile
                    Departamento de Matemática y C.C

                                          Cálculo I
                                       Pauta - Control 2
                                   Martes 23 de abril de 2024

     Ejercicio 1.
                                      r
                                             1            1
    Considere las funciones f (x) =     4−     y g(x) = 2     .
                                             x         x −x−2
    a) Determine Dom(f ◦ g)

    b) Determine explı́citamente (f ◦ g)(x)


Solución:


a) Como
                       Dom(f ◦ g) = {x ∈ Dom(g) / g(x) ∈ Dom(f )}
   debemos encontrar los dominios de f y g.
                      1                1
   Como g(x) = 2             =                 , entonces Dom(g) = R − {−1, 2}. Por otra
                  x −x−2        (x − 2)(x + 1)
                                 1
   parte, Dom(f ) = {x ∈ R : 4 − ≥ 0}.
                                 x
           1              4x − 1
   Si 4 − ≥ 0, entonces          ≥0
           x                x
                                      −∞         0          1/4       +∞
                          4x − 1             -       -            +
                            x                -       +            +
                          4x − 1
                                             +        -           +
                            x
   Por lo tanto Dom(f ) =] − ∞, 0[ ∪ [1/4, +∞[. Entonces g(x) ∈ Dom(f ) si g(x) < 0 ó
   1
     ≤ g(x)
   4
                                                      1
                            g(x) < 0        ∨           ≤ g(x)
                                                      3
                             1                     1        1
                                      <0    ∨        ≤ 2
                       (x − 2)(x + 1)              4    x −x−2

                       (x − 2)(x + 1) < 0        ∨          x2 − x − 2 ≤ 4
                       (x − 2)(x + 1) < 0        ∨          x2 − x − 6 ≤ 0
                       (x − 2)(x + 1) < 0        ∨        (x − 3)(x + 2) ≤ 0
   Por lo tanto x ∈] − 1, 2[ ∪ [−2, 3]. Finalmente tenemos que
                          Dom(f ◦ g) = [−2, −1[ ∪ ] − 1, 2[ ∪ ]2, 3].
b)

                                (f ◦ g)(x) = f (g(x))
                                                           
                                                      1
                                           = f
                                                 x2 − x − 2
                                             p
                                           =    4 − (x2 − x − 2)
                                             √
                                           =    −x2 + x + 6

     Ejercicio 2.
     Sean A, B ⊂ R. Considere la función f : A → B definida como
                                             √
                                f (x) = 2 − 3 + 2x − x2 .

     Determine los conjuntos A y B máximos de manera que la función f sea biyectiva y
     encuentre f −1


Solución:
Como sabemos, la gráfica de y = 3 + 2x − x2 = −(x − 3)(x + 1) corresponde a una parábola
que abre hacia abajo y que intersecta al eje X en los puntos x = −1 y x = 3, por lo que será
positiva en [−1, 3]. Además, es simétrica con respecto a la recta x = 1 (coordenada x del vérti-
ce), por lo tanto, para que sea inyectiva sólo consideraremos el intervalo [1, 3]
                                                              √
Para encontrar el recorrido, notemos que si escribimos y = 2 − 3 + 2x − x2 ≤ 2, luego
                                                   √
                                      y = 2 − 3 + 2x − x2
                          √
                            3 + 2x − x2 = 2 − y
                            3 + 2x − x2 = (2 − y)2
                                      0 = x2 − 2x + (2 − y)2 − 3

entonces, despejando x
                                      p
                                        4 − 4((2 − y)2 − 3)
                                       2±
                               x =
                                      p       2
                                 = 1 ± 4 − (2 − y)2

Vemos que para que esta expresión esté bien definida 4 ≥ (2 − y)2 ⇒ y ≤ 0, por lo tanto,
Rec(f ) = [0, 2]. De esta forma, podemos definir

                                        f : [1, 3] → [0, 2]
                                                 √
                                   f (x) = 2 − 3 + 2x − x2
Esta función es biyectiva y
                                       f −1 : [0, 2] → [1, 3]
                                                  p
                                 f −1 (x) = 1 + 4 − (2 − x)2
M6




                                                12
