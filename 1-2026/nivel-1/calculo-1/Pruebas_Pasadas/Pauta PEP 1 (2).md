                                                                                                    Puntaje

                       Universidad de Santiago de Chile                                        1.
                       Departamento de Matemática y C.C
                                                                                               2.
                                                Cálculo I
                                                 PEP 1                                 Nota
                                                    2025

Nombre:


  1) Determine el conjunto solución de la siguiente inecuación:

                                               |2x + 1| − 5
                                                            ≥ 0.
                                                  x2 + 1
     Solución:
     Primero que todo notemos que x2 + 1 > 0 para todo x ∈ R pues:

                            ∆(x2 + 1) = −4 y El coeficiente lı́der es positivo.

     Por ende, podemos reescribir la inecuación orginal como:

                                  |2x + 1| − 5
                                               ≥ 0 ⇐⇒ |2x + 1| − 5 ≥ 0,
                                     x2 + 1
                                                   ⇐⇒ |2x + 1| ≥ 5.

     Más aún, por propiedades del valor absoluto tenemos que:

                             |2x + 1| ≥ 5 ⇐⇒ 2x + 1 ≥ 5 ó 2x + 1 ≤ −5,
                                            ⇐⇒ 2x ≥ 4 ó 2x ≤ −6,
                                            ⇐⇒ x ≥ 2 ó x ≤ −3.

     Por lo tanto, el conjunto solución de la inecuación es:

                                              (−∞, −3] ∪ [2, ∞).

  2) Sea k ∈ R tal que la función

                                          f : [2, ∞) → [k, ∞)
                                                x    7→ (x − 2)2 + 4,

     está bien definida.

       a) Pruebe que f es inyectiva.
       b) Encuentre el valor de k para que f sea sobreyectiva.
       c) Para k = 4 justifique si existe la inversa de f . En caso de existir, determine la regla de
          asignación de f −1 .
Solución:

  a) Notemos que la función definida es una parábola cuyo vértice corresponde al punto V =
     (2, 4) y su coeficiente lı́der es positivo. Luego, sabemos que f es una función creciente para
     los x′ s que se encuentran a la derecha de la cordenada x del vértice, es decir, f es creciente
     en [2, ∞).

     Como creciente implica inyectividad, tenemos que f es inyectiva en el intervalo [2, ∞).
  b) Sabemos que para una parábola de estas caracterı́sticas, el recorrido son los y ′ s que se en-
     cuentran por sobre la coordenada y del vértice. Es decir,

                                            Rec(f ) = [4, ∞).

     Más aún, recordemos que una función es sobreyectiva si Codom(f ) = Rec(f ). Luego, para
     tener sobreyectividad debe ocurrir que:

                                             [k, ∞) = [4, ∞),

     es decir, para que la función sea sobreyectiva se necesita que k sea 4.
  c) Notemos que si k = 4, entonces la función f es biyectiva. Más aún, una función es invertible
     si y solamente si es biyectiva. Por ende podemos asegurar que la inversa existe.

     Para encontrar la inversa, notemos que para x ∈ [2, ∞) y para y ∈ [4, ∞), tenemos que

                               y = f (x) ⇐⇒ y = (x − 2)2 + 4,
                                          ⇐⇒ y = x2 − 4x + 8,
                                          ⇐⇒ 0 = x2 − 4x + (8 − y),
                                                     p
                                                 4 ± 16 − 4(8 − y)
                                          ⇐⇒ x =                      ,
                                                     √ 2
                                                 4 ± 16 − 32 + 4y
                                          ⇐⇒ x =                    ,
                                                     √ 2
                                                 4 ± 4y − 16
                                          ⇐⇒ x =                ,
                                                     p2
                                                 4 ± 4(y − 4)
                                          ⇐⇒ x =                  ,
                                                      √2
                                                 4±2 y−4
                                          ⇐⇒ x =              ,
                                                     p2
                                          ⇐⇒ x = 2 ± y − 4.
                                                    √
     Teniendo en consideración que x ∈ [2, ∞) y que y − 4 > 0 podemos concluir que
                                                  p
                                         x = 2 + y − 4.

     Ası́, la regla de asignación de la función inversa es:
                                                           √
                                           f −1 (x) = 2 + x − 4.

A continuación se mostrarán formas alternativas para la letra a) y b).




                                               2
    a*) Usaremos la definición de inyectividad para resolver el problema. Sean x1 , x2 ∈ [2, ∞) tal
        que f (x1 ) = f (x2 ) por demostrar que x1 = x2 .

         Para lograr esto, notemos que:

                     f (x1 ) = f (x2 ) ⇐⇒ (x1 − 2)2 + 4 = (x2 − 2)2 + 4,
                                      ⇐⇒ (x1 − 2)2 = (x2 − 2)2 ,
                                      ⇐⇒ |x1 − 2| = |x2 − 2|,
                                      ⇐⇒ x1 − 2 = x2 − 2,              Pues x1 , x2 ∈ [2, ∞)
                                      ⇐⇒ x1 = x2 .

         Por lo tanto, f es inyectiva en [2.∞).
    b*) Para estudiar la sobreyectividad de la función, es necesario determinar Rec(f ). Para esto,
        notemos que

         2 ≤ x ⇐⇒ 0 ≤ (x − 2),            Como ambos lados son no negativos podemos elevar al cuadrado
               0 ≤ (x − 2)2 ,
               4 ≤ (x − 2)2 + 4.

         Luego, se tiene que:
                                                  Rec(f ) = [4, ∞).
         Más aún, recordemos que una función es sobreyectiva si Codom(f ) = Rec(f ). Luego, para
         tener sobreyectividad debe ocurrir que:

                                                  [k, ∞) = [4, ∞),

         es decir, para que la función sea sobreyectiva se necesita que k sea 4.

3) Sea a ∈ R y sea la función f definida por la regla de asignación:
                                      
                                             3x(a + 1)
                                      
                                           √3
                                                                  si x < 0,
                                                x+1−1
                                      
                                      
                                      
                                      
                                      
                             f (x) =
                                      
                                          √  4
                                                           
                                                 x+1−1
                                      
                                      
                                       a √                       si x > 0.
                                      
                                      
                                               3
                                                 x+1−1

   Determine el valor de a para que lı́m f (x) exista.
                                      x→0

   Solución:
   Primero que todo, recordemos que para que lı́m f (x) exista, debe ocurrir que los lı́mites laterales
                                                   x→0
   sean iguales, es decir,
                                            lı́m f (x) = lı́m f (x).
                                          x→0−           x→0+
   Con esto en consideración, procederemos a calcular cada uno de estos lı́mites laterales.

      i) Para calcular lı́m f (x) notemos que:
                       x→0−

                                                            3x(a + 1)
                                         lı́m f (x) = lı́m √3
                                                                      .
                                        x→0  −       x→0  −   x+1−1


                                                    3
                                      √
     Usando el cambio de variable u = 3 x + 1, se tiene que:
       a) Si x tiende a 0− se tiene que u tiende a 1− .
       b) Del cambio de variable se obtiene que u3 = x + 1, o de manera equivalente, que x =
          u3 − 1.
     Por ende, se tiene que:
                                                3x(a + 1)
                             lı́m f (x) = lı́m √3
                                                          ,
                            x→0−         x→0− x + 1 − 1
                                               3(u3 − 1)(a + 1)
                                        = lı́m                  ,
                                         u→1−       u−1
                                               3(u − 1)(u2 + u + 1)(a + 1)
                                        = lı́m                             ,
                                         u→1−             u−1
                                        = lı́m 3(u2 + u + 1)(a + 1),
                                          u→1−
                                       = 9(a + 1).

  ii) Para calcular lı́m f (x), notemos que
                    x→0+
                                                   √  4
                                                               
                                                         x+1−1
                               lı́m f (x) = lı́m a √   3
                                                                 .
                              x→0+         x→0+          x+1−1
                                        √
     Usando el cambio de variable u = 12 x + 1 , se tiene que:
       a) Si x tiende a 0+ se tiene que u tiende a 1+ .
                                                        √           √
       b) Del cambio de variable se obtiene que u3 = 4 x + 1 y u4 = 3 x + 1.
     Luego,
                                                √ 4
                                                               
                                                      x+1−1
                            lı́m f (x) = lı́m a √  3
                                                                 ,
                           x→0+          x→0+         x+1−1
                                                 3       
                                                  u −1
                                       = lı́m a             ,
                                         u→1+     u4 − 1
                                                  (u − 1)(u2 + u + 1)
                                                                      
                                       = lı́m a                          ,
                                         u→1+        (u2 − 1)(u2 + 1)
                                                     (u − 1)(u2 + u + 1)
                                                                          
                                       = lı́m a                              ,
                                         u→1+     (u − 1)(u + 1)(u2 + 1)
                                                     (u2 + u + 1)
                                                                  
                                       = lı́m a                      ,
                                         u→1+     (u + 1)(u2 + 1)
                                         3a
                                       =    .
                                          4
Ası́, juntando la información de ambos lı́mites, se tiene que lı́m f (x) existe si y solamente si:
                                                               x→0

                                            3a
                               9(a + 1) =      ⇐⇒ 12(a + 1) = a,
                                             4
                                               ⇐⇒ 12a + 12 = a,
                                                        12
                                               ⇐⇒ a = − ,
                                                        11
                                                        12
                                               ⇐⇒ a = − .
                                                        11


                                               4
                                         12
Por lo tanto, el valor de a debe ser −      .
                                         11




                                                5
