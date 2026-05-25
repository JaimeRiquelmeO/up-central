                     Universidad de Santiago de Chile
                     Departamento de Matemática y C.C


                                        PEP 1 - Cálculo I
                                     Martes 07 de mayo de 2024

1 [20 Puntos.] Considere la siguiente regla de asignación
                                                  r
                                                     x−2
                                     f (x) = 1 +
                                                    2x + 1
    a) Determine Dom(f )
    b) Determine Dom(f ◦ f )

  Solución:
                                                       
                                            x−2
    a) Claramente Dom(f ) = x ∈ R :                 ≥ 0 es decir, debemos resolver la siguiente
                                            2x + 1
       inecuación
                                               x−2
                                                       ≥0
                                              2x + 1
       Para hallar la solución de esta inecuación, construiremos una tabla de signos conside-
                              1
       rando x = 2 y x = − que son los valores que anulan al numerador y al denominador
                              2
       respectivamente
                                        −∞             − 21       2       +∞
                            x−2         −        −                    +
                           2x + 1       −        +                    +
                            x−2
                                        +        −                    +
                           2x + 1
       Por lo tanto Dom(f ) = −∞, − 12 ∪ [2, +∞[
                                     

    b) De acuerdo a la definición

                         Dom(f ◦ f ) = {x ∈ Dom(f ) : f (x) ∈ Dom(f )}.

       Es decir, el dominio de esta composición está compuesto por todos aquellos
                     1
                      
       x ∈ −∞, − 2 ∪ [2, +∞[ tales que f (x) ∈ Dom(f ), o sea

                                                   1
                                       f (x) ≤ −         ∨    f (x) ≥ 2
                                                   2
       entonces, buscamos los x ∈ Dom(f ) que satisfacen además alguna de las siguientes
       desigualdades         r                         r
                                x−2       1               x−2
                        1+            ≤−      ∨ 1+               ≥ 2.
                               2x + 1     2               2x + 1
Claramente, la primera inecuación no tiene solución en R por lo que sólo debemos
resolver la segunda
                                   r
                                       x−2
                               1+              ≥ 2
                                      2x + 1
                                   r
                                       x−2
                                               ≥ 1
                                      2x + 1
                                       x−2
                                               ≥ 1
                                      2x + 1
                                   x−2
                                          −1 ≥ 0
                                  2x + 1
                                     −x − 3
                                               ≥ 0
                                      2x + 1
                                       x+3
                                               ≤ 0
                                      2x + 1

                           1
Considerando x = −3 y x = − construimos la siguiente tabla de signos
                           2
                               −∞          −3            − 21       +∞
                      x+3             −            +            +
                     2x + 1           −            −            +
                      x+3
                                      +            −            +
                     2x + 1
                                                   r
                                                       x−2
                                                              ≥ 2 es el intervalo −3, − 21
                                                                                          
Por lo tanto, la solución de la inecuación 1 +
                                                       2x + 1
Finalmente, tenemos que
                                        \               
                              1                     1        1
       Dom(f ◦ f ) =    −∞, −     ∪ [2, +∞[    −3, − = −3, −
                              2                     2        2
2 [20 Puntos.] Considere g : A → B definida como
                                            √
                               g(x) = −1 + −5 + 6x − x2

    a) Determine el conjunto A = Dom(g)
    b) Determine un conjunto A1 ⊂ A de modo que g sea inyectiva en ese conjunto y demues-
       tre esto.
    c) Determine el conjunto B de modo que g sea biyectiva y encuentre g −1 indicando su
       dominio y recorrido.

  Solución:


    a) Como Dom(g) = {x ∈ R : −5 + 6x − x2 ≥ 0}, debemos resolver la siguiente
       inecuación

                                          −5 + 6x − x2 ≥ 0
                                            x2 − 6x + 5 ≤ 0
                                         (x − 5)(x − 1) ≤ 0

       Analizamos esta inecuación con la siguiente tabla
                                            −∞            1        5        +∞
                             x−5                    −         −         +
                             x−1                    −         +         +
                         (x − 5)(x − 1)             +         −         +
       Por lo tanto Dom(g) = [1, 5]
    b) Como la expresión que se encuentra dentro de la raı́z es una parábola, la cual es simétri-
       ca con respecto a la recta vertical x = 3, podemos escoger como el conjunto A1 al
       intervalo [1, 3] o al [3, 5].
       Escogiendo A1 = [3, 5], probaremos que la función g es inyectiva en este conjunto.
       Sean a, b ∈ [3, 5]. Supongamos que g(a) = g(b), entonces

                                      g(a)        =     g(b)
                            √                                 √
                        −1 + −5 + 6a − a2         =     −1 + −5 + 6b − b2
                            √                           √
                              −5 + 6a − a2        =       −5 + 6b − b2
                              −5 + 6a − a2        =     −5 + 6b − b2
                                   6a − a2        =     6b − b2
                                         0        =     a2 − b2 + 6b − 6a
                                         0        =     (a2 − b2 ) − 6(a − b)
                                         0        =     (a − b)(a + b) − 6(a − b)
                                         0        =     (a − b)(a + b − 6)

       Entonces, para que a y b tengan la misma imagen, se debe verificar

                                    a−b=0         ∨     a+b−6=0

       La primera igualda se verifica si a = b y la segunda, sólo cuando a = b = 3, por lo
       tanto si g(a) = g(b) ⇒ a = b, esto nos dice que la función es inyectiva en [3, 5]
c) Para encontrar el recorrido de g consideremos y ∈ R tal que g(x) = y, entonces
                                            √
                                 y = −1 + −5 + 6x − x2

   notemos que y ≥ −1. Por otra parte,
                                                         √
                                          y     =   −1 + −5 + 6x − x2
                                                    √
                                      y+1       =     −5 + 6x − x2
                                   (y + 1)2     =   −5 + 6x − x2
                     x2 − 6x + 5 + (y + 1)2     =   0

   entonces
                p                             p
           6±    36 − 4(5 + (y + 1)2 )   6 ± 2 4 − (y + 1)2      p
      x=                               =                    = 3 ± 4 − (y + 1)2
                       2                         2
   Para que esta última expresión esté bien definida en R, 4 − (y + 1)2 ≥ 0, es decir
                                                        √
                                      (y + 1)2      ≤4 /
                                       |y + 1|      ≤2
                                 −2 ≤ y + 1         ≤2
                                 −3 ≤     y         ≤1

   Entonces −3 ≤ y ≤ 1, pero además, como ya se indicó −1 ≤ y, entonces −1 ≤ y ≤ 1,
                 Rec(g) = [−1, 1], y g : [3, 5] → [−1, 1] definda como
   de esta forma √
   g(x) = −1 + −5 + 6x − x2 es biyectiva y su función inversa se define como

                                     g −1 : [−1, 1] → [3, 5]
                                                p
                                g −1 (y) = 3 + 4 − (y + 1)2
3 [20 Puntos.] Considere las parábolas C1 y C2 determinadas por las ecuaciones

                                    C1 : y = kx2 − 2x + k − 1

                                     C2 : y = x2 + 3kx − k
  Determine todos los posibles valores de k ∈ R de modo que C1 y C2 se intersecten en dos
  puntos diferentes.
  Solución:

  Para hallar los puntos de intersección, debemos igualar ambas parábolas

                                     kx2 − 2x + k − 1 = x2 + 3kx − k
                    (k − 1)x2 + (−2 − 3k)x + (2k − 1) = 0

  Las soluciones de esta ecuación cuadrática corresponden a las intersecciones de las parábolas,
  como buscamos que estas intersecciones sean en dos puntos distintos, la ecuación cuadrática
  debe tener 2 soluciones, por lo que (k − 1) ̸= 0 y su discriminante debe ser mayor que cero,
  luego

                          △ = (−2 − 3k)2 − 4(k − 1)(2k − 1)         >   0
                            4 + 12k + 9k 2 − 4(2k 2 − 3k + 1)       >   0
                                                     k 2 + 24k      >   0
                                                    k(k + 24)       >   0

                                      −∞         −24          0         +∞
                            k                −           −         +
                         k + 24              −           +         +
                        k(k + 24)            +           −         +

  Entonces, considerando que k ̸= 1, las parábolas C1 y C2 se intersectan en dos puntos dife-
  rentes si
                            k ∈ ] − ∞, −24[ ∪ ]0, 1[ ∪ ]1, +∞[
