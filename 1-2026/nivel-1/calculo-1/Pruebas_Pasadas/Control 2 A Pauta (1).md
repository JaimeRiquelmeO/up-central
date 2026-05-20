                                                                                                  Puntaje

                      Universidad de Santiago de Chile                                       1.
                      Departamento de Matemática y C.C
                                                                                             2.
                                                Cálculo I
                                            Control 2 Forma A                      Nota
                                                     2025

Nombre:


     Ejercicio 1.
    Considere las funciones
                                      √
                            f (x) =       9 − x,    y   g(x) = −3 + |x + 2|,

    ambas definidas en su respectivo dominio natural.

        a. Halle el dominio de la función compuesta f ◦ g.

       b. Halle explı́citamente la fórmula de f ◦ g y calcule la imagen de −5 vı́a f ◦ g.

        c. Calcule la(s) preimagen(es) de 2 vı́a f ◦ g, si es que existen.


Solución:
                √
  a) Sea f (x) = 9 − x y g(x) = −3 + |x + 2|. Sabemos que el dominio de la composición
     corresponde a:

                             Dom(f ◦ g) = {x ∈ Dom(g) | g(x) ∈ Dom(f )}

      Por ende, procedamos a determinar Dom(f ) y Dom(g).

        i) Notemos que Dom(f ) = {x ∈ R | 9 − x ≥ 0}, es decir,

                                                   Dom(f ) = (−∞, 9].

        ii) Por otro lado Dom(g) = R.

      Ası́, se tiene que:

                            Dom(f ◦ g) = {x ∈ R | −3 + |x + 2| ∈ (−∞, 9]}.

      Por ende, se debe resolver la inecuación:

                                               −3 + |x + 2| ≤ 9,

      o equivalentemente,
                                                   |x + 2| ≤ 12.
      Por propiedades del valor absoluto, esta última inecuación se reescribe como:

                                |x + 2| ≤ 12 ⇐⇒ −12 ≤ x + 2 ≤ 12,
                                             ⇐⇒ −14 ≤ x ≤ 10.

      Por lo tanto,
                              Dom(f ◦ g) = [−14, 10] ∩ R = [−14, 10].

  b) Primero calculamos la regla de asignación de la composición:
                                   p                        p
                     (f ◦ g)(x) = 9 − (−3 + |x + 2|) = 12 − |x + 2|

      Luego,                             p                 √        √
                      (f ◦ g)(−5) =       12 − | − 5 + 2| = 12 − 3 = 9 = 3

   c) Para determinar la(s) Preimagen(es) de 2, notemos que:
                                                   p
                             (f ◦ g)(x) = 2 ⇐⇒       12 − |x + 2| = 2,
                                                   p
                                             ⇐⇒      12 − |x + 2| = 2,
                                             ⇐⇒ 12 − |x + 2| = 4,
                                             ⇐⇒ |x + 2| = 8.

      Es decir, x + 2 = −8 ó x + 2 = 8, por lo tanto las posibles preimágenes de 2 son
      x = −10 y x = 6. Como ambas pertenecen al dominio de la composición, se tiene que
      las preimágenes de 2 son -10 y 6.

     Ejercicio 2.
    Sea a ∈ R y sea
                                          √
                                             4x + 5 − 3
                                           √                        si x < 1
                                    
                                    
                                    
                                    
                                    
                                    
                                            x+3−2
                          f (x) =
                                    
                                           √   
                                          x+ x−2
                                    
                                    
                                     a    √                        si x > 1
                                    
                                    
                                             x−1

    ¿Existe algún valor de a para que lı́mx→1 f exista? Si la respuesta es afirmativa
    calcule el valor, en caso contrario argumente.



Solución: Para que exista el lı́mx→1 f (x) se debe cumplir que:

                                        lı́m f (x) = lı́m+ f (x).
                                     x→1−              x→1

Procedemos a calcular ambos lı́mites laterales.




                                                   2
Por un lado,
                 √                    √            √             √
                  4x + 5 − 3         ( 4x + 5 − 3)( 4x + 5 + 3)     x+3+2
           lı́m− √           = lı́m− √             √            ·√            ,
          x→1      x+3−2      x→1     ( x + 3 − 2)( x + 3 + 2)     4x + 5 + 3
                                                  √
                                     4x + 5 − 9     x+3+2
                             = lı́m−            ·√            ,
                              x→1     x+3−4        4x + 5 + 3
                                                √
                                     4(x − 1)     x+3+2
                             = lı́m−          ·√            ,
                              x→1     x−1        4x + 5 + 3
                                   4
                             =4· ,
                                   6
                               8
                             = .
                               3
Por otro lado,

                                       √                 √      √
                                                        ( x)2 + x − 2
                                          
                                    x+ x−2
                       lı́m a        √       = a lı́m+     √
                      x→1+             x−1      x→1           x−1
                                                         √       √
                                                        ( x − 1)( x + 2)
                                             = a lı́m+      √
                                                x→1            x−1
                                                        √
                                             = a lı́m+ ( x + 2)
                                                         x→1
                                                = a(1 + 2) = 3a.
                                                                      √
Esto también puede ser resuelto mediante el cambio de variable u =       x.

Ası́, para que el lı́mite exista debe ocurrir que:
                                         8            8
                                           = 3a =⇒ a = .
                                         3            9
                                                                8
Por lo tanto, el valor de a que hace que lı́mx→1 f (x) exista es .
                                                                9




                                                     3
