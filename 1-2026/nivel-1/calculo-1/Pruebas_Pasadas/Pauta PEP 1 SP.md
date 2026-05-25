                      Universidad de Santiago de Chile
                      Departamento de Matemática y C.C


                                       PEP 1 - Cálculo I
                                 Martes 12 de noviembre de 2024

1 [20 Puntos.] Resuelva la siguiente inecuación
                                          x+1   x−3
                                              ≤     .
                                          x+2   x−2

  Solución:
                x+1   x−3                       x−3 x+1
                    ≤               ⇐⇒       0≤       −
                x+2   x−2                       x−2 x+2
                                                (x − 3)(x + 2) − (x + 1)(x − 2)
                                    ⇐⇒       0≤
                                                        (x − 2)(x + 2)
                                                     −4
                                    ⇐⇒       0≤
                                                (x − 2)(x + 2)
                                                      1
                                    ⇐⇒       0≥
                                                (x − 2)(x + 2)

  Para resolver esta última inecuación, realizamos la siguiente tabla de signos:

                                         −∞           −2         2       +∞
                          x+2                    −           +       +
                          x−2                    −           −       +
                            1
                                                 +           −       +
                      (x + 2)(x − 2)

  De donde se obtiene que
                                        1
                             0≥                  ⇐⇒ x ∈] − 2, 2[.
                                  (x − 2)(x + 2)

  Por lo tanto, el conjunto solución de la inecuación es

                                              ] − 2, 2[.
2 [20 Puntos.] Considere la fórmula
                                                  s
                                                           3
                                       f (x) =        √       − 1.
                                                          x+1

    a) Halle el dominio natural de f (x).
    b) Halle el recorrido de f .
    c) Si g : R → R es la función lineal

                                                  g(x) = x − 2,

         determine la función compuesta f ◦ g indicando expresamente su dominio y regla de
         asignación.

  Solución:

    a)

                    Dom(f )    =     {x ∈ R : f (x) ∈ R}
                                                                                  
                                                                            3
                               =       x∈R : x+1>0                 ∧     √     −1≥0
                                                                           x+1
                                                                            
                                                          3
                               =       x ∈ ] − 1, +∞[ : √                ≥1
                                                         x+1
                                     n                     √     o
                               =      x ∈ ] − 1, +∞[ : 3 ≥ x + 1

                               =     {x ∈ ] − 1, +∞[ : 9 ≥ x + 1}
                               =     {x ∈ ] − 1, +∞[ : 8 ≥ x}
                               =     ] − 1, 8].

    b) Sea x ∈] − 1, 8]. Entonces,

                              −1 < x ≤ 8           =⇒       0<x+1≤9
                                                              √
                                                   =⇒       0< x+1≤3
                                                                 1    1
                                                   =⇒       √       ≥
                                                                x+1   3
                                                                 3
                                                   =⇒       √       ≥1
                                                                x+1
                                                              3
                                                   =⇒       √      −1≥0
                                                             x+1
                                                            s
                                                                 3
                                                   =⇒         √     −1≥0
                                                                x+1

                                                   =⇒       f (x) ≥ 0.

         Por lo tanto,
                                            Rec(f ) = [0, +∞[.
c)

                     Dom(f ◦ g)       =   {x ∈ Dom(g) : g(x) ∈ Dom(f )}
                                      =   {x ∈ R : x − 2 ∈] − 1, 8]}
                                      =   {x ∈ R : − 1 < x − 2 ≤ 8}
                                      =   {x ∈ R : 1 < x ≤ 10}
                                      =   ]1, 10].

     Luego, si x ∈]1, 10], entonces

                            (f ◦ g)(x)     =     f (g(x))
                                           =     f (x − 2)
                                                 s
                                                          3
                                           =         p            −1
                                                      (x − 2) + 1
                                                 s
                                                       3
                                           =         √    − 1.
                                                      x−1
3 [20 Puntos.] Sea k un número real de modo que la función f : [−1, 1] → [k, 10] dada por

                                             f (x) = (x − 2)2 + 1

  está bien definida.

    a) Demuestre que f es inyectiva.
    b) Determine el parámetro k de modo que f sea sobreyectiva.
    c) Determine la función inversa de f , indicando expresamente dominio, codominio y regla
       de asignación.

  Solución:

    a) Sean x1 , x2 ∈ Dom(f ) = [−1, 1] tales que f (x1 ) = f (x2 ). Queremos probar que
       x1 = x2 . En efecto,

                         f (x1 ) = f (x2 )     =⇒      (x1 − 2)2 + 1 = (x2 − 2)2 + 1
                                               =⇒      (x1 − 2)2 = (x2 − 2)2
                                               =⇒      |x1 − 2| = |x2 − 2|.

       Como x1 , x2 ∈ [−1, 1], implica que

                                    x1 − 2 < 0          ∧       x2 − 2 < 0.

       Por lo tanto,

                            f (x1 ) = f (x2 )      =⇒     |x1 − 2| = |x2 − 2|
                                                   =⇒     −(x1 − 2) = −(x2 − 2)
                                                   =⇒     x1 − 2 = x2 − 2
                                                   =⇒     x1 = x2 .

       Por lo tanto, f es inyectiva.
    b) Para hallar el valor de k, calculamos el recorrido de f . Sea x ∈ Dom(f ) = [−1, 1],
       entonces

                              −1 ≤ x ≤ 1          =⇒     −3 ≤ x − 2 ≤ −1
                                                  =⇒     9 ≥ (x − 2)2 ≥ 1
                                                  =⇒     10 ≥ (x − 2)2 + 1 ≥ 2
                                                  =⇒     10 ≥ f (x) ≥ 2.

       Por lo tanto,
                                                 Rec(f ) = [2, 10].
       Luego, para que f sea sobreyectiva basta con que

                              Cod(f ) = Rec(f )         ⇐⇒       [k, 10] = [2, 10].

       Es decir, para que f sea sobreyectiva basta con que k = 2.
c) Para que exista la función inversa de f es necesario y suficiente que f sea biyectiva.
   Esto ocurre sólo si k = 2.

   Para hallar la función inversa de f , consideramos y = f (x), para ciertos x ∈ Dom(f ) =
   [−1, 1] e y ∈ [2, 10] y despejamos x en términos de y:

                           y = f (x)    =⇒      y = (x − 2)2 + 1
                                        =⇒      y − 1 = (x − 2)2
                                                p
                                        =⇒        y − 1 = |x − 2|
                                                p
                                        =⇒        y − 1 = −(x − 2)
                                                  p
                                        =⇒      − y−1=x−2
                                                    p
                                        =⇒      2 − y − 1 = x.

   Por lo tanto, la función inversa de f está definida como

                           f −1 : [2, 10] −→ [−1, 1]
                                                                p
                                       y 7−→ f −1 (y) = 2 −      y−1
