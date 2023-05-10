module TestsEjercicio6 where

import Test.HUnit
import Ejercicio6

-- Casos de testeo:

run1 = runTestTT testSuite1

testSuite1 = test [

    "Caso 1: Multiplos de 0" ~: (multiplosDeN 0 [0,2,7,123,0,5,0,12]) ~?= [0,0,0],

    "Caso 2: Lista vacia" ~: (multiplosDeN 5 []) ~?= [],

    "Caso 3: Hay un solo multiplo" ~: (multiplosDeN 5 [3, 12, 5, 6]) ~?= [5],

    "Caso 4: No hay multiplos con numero negativo" ~: (multiplosDeN (-3) [1, 4, -7]) ~?= [],

    "Caso 5: Hay mas de un multiplo con numero negativo" ~: (multiplosDeN (-3) [1, 4, -7, -3, 6]) ~?= [-3, 6],

    "Caso 6: No hay multiplos con numero positivo" ~: (multiplosDeN 2 [1, -7, -3, 65]) ~?= [],

    "Caso 7: Hay mas de un multiplo con numero positivo" ~: (multiplosDeN 2 [1, 0, 2, 4, 6]) ~?= [0, 2, 4, 6]

 ]