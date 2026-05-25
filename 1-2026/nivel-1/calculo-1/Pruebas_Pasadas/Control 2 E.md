                                                                                                    Puntaje

                        Universidad de Santiago de Chile                                       1.
                        Departamento de Matemática y C.C
                                                                                               2.
                                            Cálculo I
                                         Control 2 Forma E                             Nota
                                                  2025
Nombre:

        Ejercicio 1.
    Considere las funciones
                                                                   x−4
                         f (x) = |x2 − 2| + 1,    y      g(x) = √
                                                                 x2 − 2x − 8
    ambas definidas en su respectivo dominio natural.

          a. Halle el dominio de la función compuesta f ◦ g , argumente su respuesta.

          b. Halle explı́citamente la fórmula de f ◦ g y calcule la imagen de 8 vı́a f ◦ g.

          c. Calcule la(s) preimagen(es) de 4 vı́a f ◦ g, si es que existen.

Solución:
   a.     a) Sabemos que el dominio natural de (f ◦ g) es por definición
                             Dom(f ◦ g) = {x ∈ Dom(g) : g(x) ∈ Dom(f )}.
             Por un lado, notemos que Dom(f ) = R. Mientras que
                               Dom(g) = {x ∈ R : x2 − 2x − 8 > 0}
                                      = {x ∈ R : (x − 4)(x + 2) > 0}
                                      = {x ∈ R : x ∈ (−∞, −2) ∪ (4, ∞)}.
             Entonces
                           Dom(f ◦ g) = {x ∈ (−∞, −2) ∪ (4, ∞) : g(x) ∈ R}
                                      = (−∞, −2) ∪ (4, ∞),
             es decir, concluimos que Dom(f ◦ g) = (−∞, −2) ∪ (4, ∞).
          b) Encontremos la regla de asignación de la composición:
                                 (f ◦ g)(x) = f (g(x))
                                            = |g(x)2 − 2| + 1
                                                              2
                                                     x−4
                                            =    √                −2 +1
                                                   x2 − 2x − 8
                                                        (x − 4)2
                                              =                   − 2 + 1,
                                                      x2 − 2x − 8
   es decir,

                                                 (x − 4)2
                         (f ◦ g)(x) =                        −2 +1
                                              (x − 4)(x + 2)
                                              x−4
                                      =             − 2 + 1.
                                              x+2

   Luego concluimos que la imagen de 8 vı́a (f ◦ g) es

                                                 8−4
                              (f ◦ g)(8) =            −2 +1
                                                 8+2
                                                 4
                                              =      −2 +1
                                                 10
                                                   8
                                              = − +1
                                                   5
                                                13
                                              =    .
                                                5
c) Calcular la preimagen de 4 corresponde a estudiar para que elementos del dominio
   natural se da la igualdad

                                    x−4
       (f ◦ g)(x) = 4       ⇔             −2 +1=4
                                    x+2
                                    x−4
                            ⇔             −2 =3
                                    x+2
                                   x−4                 x−4
                            ⇔            − 2 = 3 ó         − 2 = −3
                                   x+2                 x+2
                                   x − 4 − 2x − 4          x − 4 − 2x − 4
                            ⇔                     = 3 ó                  = −3
                                       x+2                      x+2
                                   −x − 8           −x − 8
                            ⇔              = 3 ó          = −3
                                    x+2              x+2
                            ⇔      −x − 8 = 3x + 6 ó − x − 8 = −3x − 6
                            ⇔      −4x = 14 ó 2x = 2
                                         7
                            ⇔      x=−       ó x = 1.
                                         2
   Sin embargo, notemos que:
                                      7
                                     − ∈ Dom(f ◦ g),
                                      2
   Pero
                                       1∈
                                        / Dom(f ◦ g).
   Por lo tanto, la única preimagen de 4 es − 72 .




                                          2
     Ejercicio 2.
     Sea a ∈ R y sea
                                 
                                        x2 − 6x − 7
                                        √                      si 3 ≤ x < 7
                                 
                                 
                                 
                                 
                                 
                                 
                                         x−3−2
                       f (x) =
                                 
                                          √
                                   −6a(1 −   3x − 20)
                                 
                                 
                                 
                                 
                                                                  si x > 7
                                        7x − x2
     ¿Existe algún valor de a para que lı́mx→7 f exista? Si la respuesta es afirmativa
     calcule el valor, en caso contrario argumente.



Solución: Para que exista el lı́mx→7 f (x) se debe cumplir que:

                                       lı́m f (x) = lı́m+ f (x).
                                      x→7−               x→7

Calcularemos entonces ambos lı́mites laterales.


Por un lado,
                                                             √
                                              x2 − 6x − 7 ( x − 3 + 2)
                          lı́m f (x) = lı́m− √            · √
                         x→7−          x→7      x − 3 − 2 ( x − 3 + 2)
                                                             √
                                              (x − 7)(x + 1)( x − 3 + 2)
                                     = lı́m−
                                       x→7               x−7
                                                     √
                                     = lı́m− (x + 1)( x − 3 + 2)
                                       x→7
                                                 √
                                     = (7 + 1)( 7 − 3 + 2)
                                     = 32

Mientras que,
                                                √                √
                                        −6a(1 − 3x − 20) (1 + 3x − 20)
                     lı́m f (x) = lı́m+                    ·     √
                    x→7+          x→7        7x − x2         (1 + 3x − 20
                                            −6a(21 − 3x)
                                = lı́m+              √
                                  x→7 (7x − x2 )(1 +   3x − 20)
                                             −18a(7 − x)
                                = lı́m+             √
                                  x→7 x(7 − x)(1 +    3x − 20)
                                             −18a
                                = lı́m+      √
                                  x→7 x(1 +    3x − 20)
                                  −9a
                                =
                                    7
Ası́, para que el lı́mite exista debe ocurrir que:
                                     −9a             −224
                                         = 32 ⇐⇒ a =      .
                                      7               9
Por lo tanto, para que el lı́mite exista debe ocurrir que a = −224
                                                               9
                                                                   .

                                                     3
