            Universidad de Santiago de Chile
            Departamento de Matemática y C.C

                                           Cálculo I
                                          Pauta PEP 1
                                  Martes 17 de octubre de 2023


1. [20 puntos] El ancho de un terreno rectangular es 9 metros más corto que su largo.
   Encuentre las dimensiones que puede tener este terreno si su área debe ser a lo más 400[m2 ].

   Solución:

   Designemos por x al ancho del terreno (en metros). De acuerdo a esto, el largo del terreno debe
   ser (x + 9)[m]. Como el área debe ser a lo más 400[m2 ] tenemos que

                                         A = x(x + 9)     ≤   400
                                               x2 + 9x    ≤   400
                                         x2 + 9x − 400    ≤   0
                                      (x + 25)(x − 16)    ≤   0

   La solución de esta inecuación es x ∈ [−25, 16], pero como x representa el ancho del terreno,
   éste no puede ser negativo, por lo que x ∈ [0, 16], es decir, el ancho del terreno está entre 0 y
   16 metros y como el largo debe tener 9 metros más que el ancho, el largo del terreno debe estar
   entre 9 y 25 metros.
                                                   √                    √
2. [20 puntos] Considere las funciones f (x) =         x − 2 y g(x) =       25 − x2 − 2.

  Determine Dom(f ◦ g)

  Solución:

  De acuerdo a la definición

                         Dom(f ◦ g) = {x ∈ Dom(g) : g(x) ∈ Dom(f )}

  Por una parte tenemos que Dom(g) = {x ∈ R : 25 − x2 ≥ 0} = [−5, 5], mientras que
  Dom(f ) = [2, +∞[. Por lo tanto
                                                                √
     Dom(f ◦ g) = {x ∈ Dom(g) : g(x) ∈ Dom(f )} = {x ∈ [−5, 5] : 25 − x2 − 2 ≥ 2}

  Debemos resolver la inecuación
                                    √
                                        25 − x2 − 2 ≥ 2
                                          √
                                                        
                                                  2
                                            25 − x ≥ 4    ()2

                                           25 − x2 ≥ 16
                                           25 − 16 ≥ x2
                                                                
                                                            2    √
                                                   9 ≥ x

                                                   3 ≥ |x|

  Por lo tanto

    Dom(f ◦ g) = {x ∈ Dom(g) : g(x) ∈ Dom(f )} = {x ∈ [−5, 5] : −3 ≤ x ≤ 3} = [−3, 3]




                                               2
3. [20 puntos] Sea f : A → B una función definida como

                                       f (x) = −x2 + 4x − 3

  Determine los conjuntos A y B de modo que f sea biyectiva y encuentre f −1

  Solución:
  Como esta es una función cuadrática, su gráfico corresponde a una parábola que abre hacia
  abajo. Calcularemos las coordenadas del vértice.
  El vértice V está ubicado en las coordenas (Vx , Vy ) del plano, donde

                                              −b   −4
                                       Vx =      =    = 2,
                                              2a   −2
  mientras que Vy = f (2) = −4 + 8 − 3 = 1.
  Por lo tanto, el vértice está en el punto V (2, 1). Para que la función sea inyectiva, debemos
  restringir el dominio. En este caso, consideraremos como dominio de la función al conjunto
  A = [2, +∞[.
  Como el recorrido es ] − ∞, 1], si definimos B como este conjunto, la función es sobreyectiva
  y por lo tanto biyectiva, es decir

                                       f : [2, ∞[→] − ∞, 1]

                                       f (x) = −x2 + 4x − 3
  es una función biyectiva.
  Para hallar su inversa, escribimos

                                        y = −x2 + 4x − 3

  para despejar la variable x.

                                          y = −x2 + 4x − 3
                            x2 − 4x + 3 + y = 0
                                               p
                                                 16 − 4(3 + y)
                                                   4±
                                        ⇒x =
                                                √ 2
                                             4±2 4−3−y
                                           =
                                               p 2
                                           = 2± 1−y

  Como restringimos el dominio de la función a valores mayores que 2, la función inversa de f
  es
                                   f −1 :] − ∞, 1] → [2, ∞[
                                                   p
                                    f −1 (y) = 2 + 1 − y




                                              3
