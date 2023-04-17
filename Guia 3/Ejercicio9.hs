{-

-- A

La funcion toma un flotante en su dominio y nos devuelve otro flotante segun su codominio. 
En este caso es una funcion partida, en el primer caso si el parametro "n" es igual a 0, la funcion nos retorna 1, y de ser cualquier otro valor, el retorno es 0.

problema f1 (n : R) R 
{
    requiere: {true}
    asegura: {result = if n == 0 then 1 else 0 fi}
}

-- B

La funcion toma un flotante en su dominio y nos devuelve otro flotante segun su codominio. 
En este caso es una funcion partida, en el primer caso si el parametro "n" es igual a 1, la funcion nos retorna 15, y en el segundo caso de ser -1, el retorno es -15.

problema f2 (n : R) R 
{
    requiere: {true}
    asegura: {result = 15 <-> n == 1}
    asegura: {result = -15 <-> n == -1}
}

-- C

La funcion toma un flotante en su dominio y nos devuelve otro flotante segun su codominio. 
En este caso es una funcion partida, en el primer caso si el parametro "n" es menor igual a 7, la funcion nos retorna 9, y en el segundo caso de ser mayor igual 3, el retorno es 5.
El funcion nos retorna valor indefinido si n queda entre 7 y 3 no inclusives.

problema f3 (n : R) R 
{
    requiere: {true}
    asegura: {result = 9 <-> n <= 7}
    asegura: {result = 5 <-> n >= 3}
}

-- D

La funcion toma dos flotantes en su dominio y nos devuelve otro flotante segun su codominio. 
de esas dos parametros, retonar la suma de ambos dividida por 2.

problema f4 (n : R, n : R) R 
{
    requiere: {true}
    asegura: {result = (x + y) / 2 }
}

-- E

La funcion una tupla de dos flotantes (reales) en su dominio y nos devuelve otro flotante segun su codominio. 
De esa tupla, retona la suma T1 y T2 con el total siendo dividido por 2.

problema f5 (n : R x R) R 
{
    requiere: {true}
    asegura: {result = (x + y) / 2 }
}

-- F

La funcion toma un parametro flotante y otro entero en su dominio, y tiene codominio booleano.
Se trunca el parametro flotante, la funcion "truncate" retorna el entero mas cercano al flotante introducido, siendo este redondeado para abajo,
entonces se compara la igualdad de ese entero devuelto por "truncate" con el segundo parametro entero. Retorna falso si son diferentes y verdadero al cumplirse la igualdad. 

problema f6 (n : R, m : Z) B 
{
    requiere: {true}
    asegura: {result = true <-> (╚n┘ == m}
}

-}

f6 :: Float -> Int -> Bool
f6 a b = truncate a == b