                                                                                                   Puntaje

                       Universidad de Santiago de Chile                                       1.
                       Departamento de Matemática y C.C
                                                                                              2.
                                            Cálculo I
                                        Control 2 Forma B                           Nota
                                                  2025

Nombre:


     Ejercicio 1.
    Considere las fórmulas
                                       r
                                           3x + 6                  x−3
                             f (x) =              ,   y   g(x) =       ,
                                           x−1                      x
    ambas definidas en su respectivo dominio natural.

        a. Halle el dominio de la función compuesta f ◦ g.

        b. Halle explı́citamente la fórmula de f ◦ g y calcule la imagen de −1 vı́a f ◦ g.

        c. Calcule la(s) preimagen(es) de 3 vı́a f ◦ g, si es que existen.


Solución:
                     r
                         3x + 6          x−3
  a) Sean f (x) =               y g(x) =     . El dominio de la composición es:
                         x−1              x

                            Dom(f ◦ g) = {x ∈ Dom(g) | g(x) ∈ Dom(f )}

      Determinemos primero Dom(f ) y Dom(g):
                                       
                             3x + 6
        i) Dom(f ) = x ∈ R :         ≥ 0 . Usando la tabla de signos para la desigualdad:
                              x−1
                                               (−∞, −2)     (−2, 1)    (1, ∞)
                                   3x + 6         −           +          +
                                   x−1            −           −          +
                                    (3x+6)
                                     (x−1)
                                                  +           −          +
              Por lo tanto, Dom(f ) = (−∞, −2] ∪ (1, ∞).
        ii) Dom(g) = R − {0}.
      Ası́,
                                                                     
                                               x−3
                    Dom(f ◦ g) = x ∈ R − {0} :     ∈ (−∞, −2] ∪ (1, ∞) ,
                                                x
                                                                    
                                               x−3         x−3
                               = x ∈ R − {0} :     ≤ −2 ó       >1 .
                                                x           x
      Por ende, para encontrar el dominio debemos resolver ambas desigualdades. Por un lado,
                                    x−3        x−3
                                        > 1 ⇐⇒        − 1 > 0,
                                     x           x
                                               −3
                                            ⇐⇒     > 0,
                                                x
                                            ⇐⇒ x < 0.

      Mientras que por el otro,
                                  x−3         x−3
                                      ≤ −2 ⇐⇒       + 2 ≤ 0,
                                   x            x
                                              3(x − 1)
                                           ⇐⇒            ≤ 0,
                                                  x
                                           ⇐⇒ x ∈ (0, 1].

      Por lo tanto, Dom(f ◦ g) = (−∞, 0) ∪ (0, 1].

  b) La fórmula de la composición es:
                     s                  s           s        r
                        3 x−3             3x−9+6x     9x−9
                              
                            x
                                + 6          x          x      9(x − 1) p
      (f ◦ g)(x) =        x−3       =      x−3−x  =    −3  =           = −3(x − 1)
                           x
                              −1             x          x
                                                                 −3

      Evaluando en x = −1:
                                                    p            √
                                  (f ◦ g)(−1) =      −3(−1 − 1) = 6

   c) Buscamos x tal que (f ◦ g)(x) = 3:
                             p
                               −3(x − 1) = 3 ⇐⇒ −3(x − 1) = 9
                                             ⇐⇒ x − 1 = −3
                                             ⇐⇒ x = −2

      Como x = −2 ∈ Dom(f ◦ g), la única preimagen de 3 es −2.

     Ejercicio 2.
    Sea a ∈ R y sea
                                              √
                                           x− x+2
                                           √                        si x > 2
                                    
                                    
                                    
                                    
                                    
                                    
                                            4x + 1 − 3
                          f (x) =
                                    
                                       √
                                         3
                                                 
                                           x+6−2
                                    
                                    
                                     a                             si x < 2
                                    
                                    
                                            x−2

    ¿Existe algún valor de a para que lı́mx→2 f exista? Si la respuesta es afirmativa
    calcule el valor, en caso contrario argumente.



Solución: Para que exista el lı́mx→2 f (x) se debe cumplir que:

                                        lı́m f (x) = lı́m+ f (x).
                                     x→2−              x→2


                                                   2
Procedemos entonces a calcular ambos lı́mites laterales.

Por un lado,
                     √                    √         √                 √
                  x− x+2              x− x+2          4x + 1 + 3 x + x + 2
             lı́m √          = lı́m √             ·√              ·   √    ,
            x→2+   4x + 1 − 3 x→2+ 4x + 1 − 3         4x + 1 + 3 x + x + 2
                                                  √
                                     (x2 − x − 2)( 4x + 1 + 3)
                             = lı́m+                   √        ,
                              x→2 (4x + 1 − 9)(x +       x + 2)
                                                    √
                                     (x − 2)(x + 1)( 4x + 1 + 3)
                             = lı́m+                  √             ,
                              x→2        4(x − 2)(x + x + 2)
                                             √
                                     (x + 1)( 4x + 1 + 3)     9
                             = lı́m+           √           = .
                              x→2        4(x + x + 2)         8


Por otro lado, para calcular                     √
                                                 3
                                                     x+6−2
                                        a lı́m             ,
                                          x→2         x−2
utilizamos el cambio de variable:
                         √
                    u= 3x+6           ⇒    u3 = x + 6 ⇒ x = u3 − 6.
                                                   √
Más aún, notemos que si x → 2, se tiene que u → 3 8 = 2. Luego,
       √
       3
         x+6−2              u−2                     u−2                      1        a
a lı́m             = a lı́m 3      = a lı́m          2
                                                                = a lı́m 2           = .
  x→2     x−2          u→2 u − 8        u→2 (u − 2)(u + 2u + 4)     u→2 (u + 2u + 4)  12

Por lo tanto, para que el lı́mite exista se debe cumplir que:
                                      9   a         27
                                        =    ⇐⇒ a =
                                      8   12        2
Luego, el valor de a para que el lı́mite exista es a = 27
                                                       2
                                                          .




                                                     3
