                                                                                                   Puntaje

                       Universidad de Santiago de Chile                                       1.
                       Departamento de Matemática y C.C
                                                                                              2.
                                            Cálculo I
                                        Control 2 Forma D                           Nota
                                                  2025
Nombre:


     Ejercicio 1.
    Considere las fórmulas
                                        r
                                            2x − 4
                              f (x) =              ,   y   g(x) = x − 3,
                                             x+1
    ambas definidas en su respectivo dominio natural.

        a. Halle el dominio de la función compuesta f ◦ g.

        b. Halle explı́citamente la fórmula de f ◦ g y calcule la imagen de −1 vı́a f ◦ g.

        c. Calcule la(s) preimagen(es) de 1 vı́a f ◦ g, si es que existen.

Solución:
                     r
                         2x − 4
  a) Sean f (x) =               y g(x) = x − 3. El dominio de la composición es:
                          x+1

                            Dom(f ◦ g) = {x ∈ Dom(g) | g(x) ∈ Dom(f )}
      Determinemos primero Dom(f ) y Dom(g):
                                       
                             2x − 4
        i) Dom(f ) = x ∈ R :         ≥ 0 . Usando la tabla de signos para la desigualdad:
                              x+1
                                                (−∞, −1)     (−1, 2)   (2, ∞)
                                   2x − 4          −           −         +
                                    x+1            −           +         +
                                    (2x−4)
                                     (x+1)
                                                   +           −         +
              Por lo tanto, Dom(f ) = (−∞, −1) ∪ [2, ∞).
        ii) Dom(g) = R.
      Ası́,
                         Dom(f ◦ g) = {x ∈ R : x − 3 ∈ (−∞, −1) ∪ [2, ∞)} ,
                                    = {x ∈ R : x − 3 < −1 ó x − 3 ≥ 2} ,
                                    = {x ∈ R : x < 2 ó x ≥ 5} .
      Por lo tanto, Dom(f ◦ g) = (−∞, 2) ∪ [5, ∞).
  b) La fórmula de la composición es:
                                s                 r              r
                                   2(x − 3) − 4     2x − 6 − 4     2x − 10
                  (f ◦ g)(x) =                  =              =
                                    (x − 3) + 1       x−2           x−2

      Evaluando en x = −1:

                                                                  −12 √
                                          r                  r
                                              2(−1) − 10
                         (f ◦ g)(−1) =                   =           = 4=2
                                                −1 − 2            −3

   c) Buscamos x tal que (f ◦ g)(x) = 1:
                             r
                                2x − 10         2x − 10
                                         = 1 ⇐⇒         =1
                                 x−2             x−2
                                             ⇐⇒ 2x − 10 = x − 2
                                             ⇐⇒ x = 8

      Como x = 8 ∈ Dom(f ◦ g) se tiene que la única preimagen de 1 es 8.

     Ejercicio 2.
    Determine el valor de a ∈ (0, ∞) de modo que exista el lı́m f (x) donde la función f
                                                           x→0
    se define como
                                      x3 + x
                             
                             
                                                       si x < 0.
                             
                                    x2 − 8x
                     f (x) =    √         √
                                  a − x −    a+x
                             
                             
                                                     si 0 < x < a.
                             
                             
                                     2x + x2


Solución: Para que exista el lı́m f (x) se debe cumplir que:
                             x→0

                                      lı́m f (x) = lı́m+ f (x).
                                      x→0−           x→0

Procedemos entonces a calcular ambos lı́mites laterales.

Por un lado,

                                                       x3 + x
                                lı́m− f (x) =     lı́m−       ,
                                x→0             x→0 x2 − 8x
                                                      x(x2 + 1)
                                              = lı́m−            ,
                                                x→0 x(x − 8)

                                                      (x2 + 1)
                                              = lı́m−          ,
                                                x→0 (x − 8)
                                                   1
                                              = − .
                                                   8




                                                 2
Por otra parte,
                                           √       √
                                            a−x− a+x
                   lı́m f (x) =      lı́m                 ,
                  x→0+              x→0+      2x + x2
                                           √       √        √          √
                                            a−x− a+x         a−x+ a+x
                               =     lı́m                  ·√          √ ,
                                    x→0+     x(2 + x)        a−x+ a+x
                                                      −2x
                               =     lı́m+          √        √         ,
                                    x→0 x(2 + x) · ( a − x +   a + x)
                                                      −2
                               =     lı́m+         √        √        ,
                                    x→0 (2 + x) · ( a − x +   a + x)
                                         1
                               =    − √ .
                                        2 a

Por lo tanto, el lı́m f (x) existe si
                  x→0

                                                        −1     −1
                                                        √ =
                             lı́m− f (x) = lı́m+ f (x) ⇐⇒         ,
                            x→0          x→0           2 a     8
                                                       √
                                                     ⇐⇒ a = 4.

Por lo tanto, para que el lı́mite exista debe ocurrir que a = 16.




                                                 3
