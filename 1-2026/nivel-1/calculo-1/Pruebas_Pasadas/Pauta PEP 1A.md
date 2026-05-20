                  Universidad de Santiago de Chile
                  Departamento de Matemática y C.C

                                         Cálculo I
                                       Pauta - Pep 1.A
                             Martes 27 de septiembre de 2022


1. Resuelva la siguiente inecuación
                                         2 − |2 − x|
                                                     ≤0
                                           1 − x2
                                                                                  (2 Puntos)


   Solución:
   Primero, establecemos las restricciones que presenta esta inecuación, estas son:

                                         x ̸= −1, x ̸= 1.

   Ahora, analizaremos 3 casos: x < −1, −1 < x < 1, y 1 < x.


        Caso 1: x < −1
        Es claro que si x < −1 ⇒ 1 − x2 < 0, por lo tanto
                                          2 − |2 − x|
                                                      ≤0
                                            1 − x2
                                   ⇔      2 − |2 − x| ≥ 0
                                                          
                                   ⇔      −|2 − x| ≥ −2     · −1
                                   ⇔        |2 − x| ≤ 2
                                                          
                                   ⇔      −2 ≤ 2 − x ≤ 2    −2
                                                          
                                   ⇔       −4 ≤ −x ≤ 0      · −1
                                   ⇔         4≥x≥0

        Intersectando esta solución con los x considerados en el caso 1, tenemos que la so-
        lución S1 = ϕ.

        Caso 2: −1 < x < 1
        Es claro que si −1 < x < 1 ⇒ 0 < 1 − x2 , por lo tanto
                                        2 − |2 − x|
                                                    ≤0
                                          1 − x2
                              ⇔         2 − |2 − x| ≤ 0
                                                          
                              ⇔         −|2 − x| ≤ −2       · −1
                              ⇔           |2 − x| ≥ 2
                              ⇔    2 − x ≤ −2 ∨ 2 ≤ 2 − x
                              ⇔         4≤x ∨x≤0
Intersectando esta solución con los x considerados en el caso 2, tenemos que la
solución S2 =] − 1, 0].
Caso 3: 1 < x
Es claro que si 1 < x ⇒ 1 − x2 < 0, por lo tanto

                              2 − |2 − x|
                                          ≤0
                                1 − x2
                          ⇔   2 − |2 − x| ≥ 0
                                              
                          ⇔   −|2 − x| ≥ −2     · −1
                          ⇔     |2 − x| ≤ 2
                                              
                          ⇔   −2 ≤ 2 − x ≤ 2    −2
                                              
                          ⇔    −4 ≤ −x ≤ 0      · −1
                          ⇔      4≥x≥0

Intersectando esta solución con los x considerados en el caso 3, tenemos que la
solución S3 =]1, 4].
Finalmente, tenemos que la solución final (Sf ) de esta inecuación es

                      Sf = S1 ∪ S2 ∪ S3 =] − 1, 0] ∪ ]1, 4]
2. Determine los valores de k ∈ R para que la parábola de ecuación y = kx2 + 6x + 3 y la
   recta de ecuación y = 2kx − 1 se intersecten en dos puntos.                (2 Puntos)

   Solución:

   Para hallar los valores de x en que se intersectan la parábola con la recta, primero iguala-
   mos sus expresiones
                                    kx2 + 6x + 3 = 2kx − 1
   Despejando, vemos que esta igualdad es equivalente a la siguiente ecuación cuadrática

                                   kx2 + (6 − 2k)x + 4 = 0.

   Ahora, que la intersección entre la parábola y la recta se produzca en dos puntos es equi-
   valente a que la ecuación cuadrática tenga dos soluciones y esto se tendrá cuando su
   discriminante
                                              △ > 0.
   Para esta ecuación

                                 △ = (6 − 2k)2 − 4k(4)      >   0
                                  36 − 24k + 4k 2 − 16k     >   0
                                         4k 2 − 40k + 36    >   0
                                        4(k 2 − 10k + 9)    >   0
                                        4(k − 1)(k − 9)     >   0


   La solución de esta última inecuación es k ∈ ]−∞, 1[ ∪ ]9, ∞[. Por otra parte, es evidente
   que k ̸= 0, por lo tanto, la parábola se intersectará con la recta en dos puntos cuando
   k ∈ ] − ∞, 0[ ∪ ]0, 1[ ∪ ]9, ∞[.
3. Considere la función f : A ⊂ R → B ⊂ R dada por
                                              √
                                          q
                                 f (x) = − 2 − −1 − 2x.

    a) Encontrar el conjunto A = Dom(f ).                                (0.7 Puntos)
    b) Determine si f es creciente o decreciente.                        (0.7 Puntos)
    c) Determine Rec(f )                                                 (0.6 Puntos)

  Solución:


    a) Claramente el dominio de esta función está dado por el conjunto
                                                               √
                 Dom(f ) = {x ∈ R/ − 1 − 2x ≥ 0 ∧ 2 − −1 − 2x ≥ 0}

       es decir
                                                   √
                              −1 − 2x ≥ 0     ∧ 2 − −1 − 2x ≥ 0
                                                   √
                                              ∧ 2 ≥ −1 − 2x ()2
                                                            
                                 −1 ≥ 2x
                                    1
                                  − ≥x        ∧ 4 ≥ −1 − 2x
                                    2
                                    1
                                  − ≥x        ∧ 2x ≥ −5
                                    2
                                    1                    5
                                  − ≥x        ∧ x≥−
                                    2                    2

       Por lo tanto                                         
                                                  5 1
                                       Dom(f ) = − , −
                                                  2 2
                                                5         1
    b) Sean a, b ∈ Dom(f ) con a < b, es decir − ≤ a < b ≤ . Se tiene lo siguiente
                                                2         2
                                    a < b     / · (−2)
                                −2a > −2b         /−1
                                                       √
                             −1 − 2a > −1 − 2b       /
                           √            √
                             −1 − 2a >     −1 − 2b     / · (−1)
                           √              √
                          − −1 − 2a < − −1 − 2b          /(+2)
                           √                 √               √
                        2 − −1 − 2a < 2 − −1 − 2b           /
                           √                   √
                       q                q
                        2 − −1 − 2a <      2 − −1 − 2b        / · (−1)
                           √                     √
                       q                  q
                      − 2 − −1 − 2a > − 2 − −1 − 2b
                                f (a) > f (b)

       Por lo tanto, la función f es decreciente.
    c) Del hecho que la función f es decreciente podemos deducir que
                                                              √
                          Rec(f ) = [f (−1/2), f (−5/2)] = [− 2, 0]
