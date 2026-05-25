                                                                                                      Puntaje

                        Universidad de Santiago de Chile                                         1.
                        Departamento de Matemática y C.C
                                                                                                 2.
                                               Cálculo I
                                           Control 2 Forma C                           Nota
                                                  2025
Nombre:


        Ejercicio 1.
    Considere las fórmulas
                                      √
                        f (x) = 2 −       −6x − x2 ,    y   g(x) = 3 − |x − 2|,

    ambas definidas en su respectivo dominio natural.

          a. Halle el dominio de la función compuesta g ◦ f .

          b. Halle explı́citamente la fórmula de g ◦ f y calcule la imagen de −1 vı́a g ◦ f .

          c. Calcule la(s) preimagen(es) de 0 vı́a g ◦ f , si es que existen.

Solución:
   a.     a) Sabemos que el dominio natural de (g ◦ f ) es por definición
                             Dom(g ◦ f ) = {x ∈ Dom(f ) : f (x) ∈ Dom(g)}.
             Por un lado, notemos que Dom(g) = R. Mientras que
                                    Dom(f ) =          {x ∈ R : −6x − x2 ≥ 0}
                                            =          {x ∈ R : −x(6 + x) ≥ 0}
                                            =          {x ∈ R : x(6 + x) ≤ 0}
                                            =          {x ∈ R : x ∈ [−6, 0]}
                                            =          [−6, 0].
             Entonces
                                  Dom(g ◦ f ) = {x ∈ [−6, 0] : f (x) ∈ R}
                                              = [−6, 0],
             es decir, concluimos que Dom(g ◦ f ) = [−6, 0].
          b) Encontremos la regla de asignación de la composición:
                                   (g ◦ f )(x) =       g(f (x))
                                               =       3 − |f (x) − 2|
                                                                √
                                               =       3 − |2 − −6x − x2 − 2|
                                                            √
                                               =       3 − −6x − x2 ,
           es decir,
                                                           √
                                     (g ◦ f )(x) = 3 −         −6x − x2 .

           Luego concluimos que la imagen de −1 vı́a (g ◦ f ) es
                                         p                       √
                       (g ◦ f )(−1) = 3 − −6(−1) − (−1))2 = 3 − 5.

        c) Cálcular la preimagen de 0 corresponde a estudiar para que elementos del dominio
           natural se da la igualdad
                                                           √
                              (g ◦ f )(x) = 0   ⇔      3 − −6x − x2 = 0
                                                           √
                                                ⇔      3 = −6x − x2
                                                ⇔      9 = −6x − x2
                                                ⇔      x2 + 6x + 9 = 0
                                                ⇔      (x + 3)2 = 0
                                                ⇔      x = −3.

            Por lo tanto, la preimagen de 0 de acuerdo a la funcón (g ◦ f ) en Dom(g ◦ f ) es


           −3.

     Ejercicio 2.
    Sea a ∈ R considere la fórmulaa
                               √             √
                                     5x − 6 − x + 2
                                                                   si x < 2
                              
                              
                                         3x − 6
                              
                              
                              
                              
                              
                    f (x) =
                              
                                      √           
                              
                                   x −   2x 2+x−6
                               a                                  si x > 2
                              
                              
                                         x2 − 2x

    ¿Existe algún valor de a para que lı́mx→2 f exista? Si la respuesta es afirmativa
    calcule el valor, en caso contrario argumente.



Solución: Para que exista el lı́mx→2 f (x) se debe cumplir que:

                                     lı́m f (x) = lı́m+ f (x).
                                    x→2−            x→2

Calcularemos entonces ambos lı́mites laterales.




                                                2
Por un lado,
                √            √              √         √        √       √
                    5x − 6 − x + 2         ( 5x − 6 − x + 2)( 5x − 6 + x + 2)
         lı́m                      = lı́m−               √          √
        x→2−            3x − 6       x→2        3(x − 2)( 5x − 6 + x + 2)
                                                5x − 6 − (x + 2)
                                   = lı́m−         √          √
                                     x→2 3(x − 2)( 5x − 6 +     x + 2)
                                                     4x − 8
                                   = lı́m−         √          √
                                     x→2 3(x − 2)( 5x − 6 +     x + 2)
                                               4(x − 2)
                                   = lı́m−         √     √
                                     x→2 3(x − 2)( 4 +     4)
                                       4     1
                                   =       =
                                     3·4     3
Por otra parte,
                  √                           √
                x − 2x2 + x − 6             x − 2x2 + x − 6
       lı́m a                     = a lı́m+
      x→2+          x2 − 2x          x→2        x(x − 2)
                                                √                   √
                                            (x − 2x2 + x − 6)(x + 2x2 + x − 6)
                                  = a lı́m+                   √
                                     x→2         x(x − 2)(x + 2x2 + x − 6)
                                                x2 − (2x2 + x − 6)
                                  = a lı́m+              √
                                     x→2 x(x − 2)(x +      2x2 + x − 6)
                                                   −x2 − x + 6
                                  = a lı́m+              √
                                     x→2 x(x − 2)(x +      2x2 + x − 6)
                                                 −(x − 2)(x + 3)
                                  = a lı́m+              √
                                     x→2 x(x − 2)(x +      2x2 + x − 6)
                                                 −(x + 3)
                                  = a lı́m+       √
                                     x→2 x(x +     2x2 + x − 6)
                                         −5        5a
                                  =a           =−
                                     2(2 + 2)       8

Luego, para que el lı́mite exista debe ocurrir que,
                                   1    5a          8
                                     =−    =⇒ a = −
                                   3     8          15
                                                                      8
Por lo tanto, el valor de a que hace que lı́mx→2 f (x) exista es −      .
                                                                     15




                                                3
