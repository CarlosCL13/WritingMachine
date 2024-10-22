from semantico.aritmeticas import *
from semantico.condicionales_logicas import *
from semantico.semantic_Error import *
from analizador_sintactico import symbol_table, current_scope

""""
def prueba():

    dicc = {"main": 
                {"parametros": [1,2,3]},
            "var2": 2,
            "var3": 3
            }
    dicc["var1"] = {}
    dicc["var1"]["fer"] = 4
    dicc["var1"]["fercho"] = 5

    dicc_actual = dicc["main"]
    print("Diccionario de main" + str(dicc_actual))

    for variable in dicc["main"]["parametros"]:
        if variable == 4:
            print("es un uno") 

    print(dicc)
    for far in dicc:
        if far == "main":
            lista = dicc[far]["parametros"]
            print(lista)

prueba() 
"""

# Función de pruebas para verificar el comportamiento de la clase Sum
def test_sum():

    parser.symbol_table = {
            "MAIN": {"x": 20, "y": 20, "z": 30},  # Variables globales
            "func1": {"a": 5, "b": 15, "m": True},           # Variables locales en el ámbito 'func1'
            "func2": {"p": 5, "h": 15}
        }
    
    # Caso 1: Ambos valores son enteros
    sum_case_1 = Div(5, 10, 1)
    parser.current_scope = "func1"
    sum_case_1.calculate()

    # Caso 2: Primer valor es entero, segundo es una variable existente en el alcance actual
    sum_case_2 = Div(5, "m", 2)
    parser.current_scope = "func1"
    sum_case_2.calculate()

    # Caso 3: Primer valor es entero, segundo es una variable inexistente
    sum_case_3 = Div(5, "c", 3)
    parser.current_scope = "func1"
    sum_case_3.calculate()

    # Caso 4: Primer valor es una variable existente, segundo es un entero
    sum_case_4 = Div("a", 15, 4)
    parser.current_scope = "func1"
    sum_case_4.calculate()

    # Caso 5: Ambos valores son variables existentes
    sum_case_5 = Div("a", "b", 5)
    parser.current_scope = "func1"
    sum_case_5.calculate()

    # Caso 6: Ambos valores son variables, pero una no existe
    sum_case_6 = Div("a", "c", 6)
    parser.current_scope = "func1"
    sum_case_6.calculate()

    error = ErrorLog()
    print(error.get_message())

# Ejecutar las pruebas
#test_sum()

def test_random():

    parser.symbol_table = {
            "MAIN": {"x": 20, "y": 20, "z": 30},  # Variables globales
            "func1": {"a": 5, "b": 15, "m": True},           # Variables locales en el ámbito 'func1'
            "func2": {"p": 5, "h": 15}
        }
    
    # Caso 1: Ambos valores son enteros
    random_case1 = Random(5, 2)
    parser.current_scope = "func1"
    random_case1.calculate()

    # Caso 2: Primer valor es entero, segundo es una variable existente en el alcance actual
    random_case2 = Random("m", 4)
    parser.current_scope = "func1"
    random_case2.calculate()

    # Caso 3: Primer valor es entero, segundo es una variable inexistente
    random_case3 = Random("c", 5)
    parser.current_scope = "func1"
    random_case3.calculate()
    
     # Caso 2: Primer valor es entero, segundo es una variable existente en el alcance actual
    random_case4 = Random("a", 4)
    parser.current_scope = "func1"
    random_case4.calculate()

    error = ErrorLog()
    print(error.get_message())

# Ejecutar las pruebas
#test_random()


def test_addOne():

    parser.symbol_table = {
            "MAIN": {"x": 20, "y": 20, "z": 30},  # Variables globales
            "func1": {"a": 5, "b": 15, "m": True},           # Variables locales en el ámbito 'func1'
            "func2": {"p": 5, "h": 15}
        }
    
    # Caso 1: El valor es una variable
    addOne_case1 = AddOne("m", 4)
    parser.current_scope = "func1"
    addOne_case1.calculate()

    # Caso 2
    addOne_case2 = AddOne("c", 5)
    parser.current_scope = "func1"
    addOne_case2.calculate()
    
     # Caso 3: Primer valor es entero, segundo es una variable existente en el alcance actual
    addOne_case3 = AddOne("a", 4)
    parser.current_scope = "func1"
    addOne_case3.calculate()

    error = ErrorLog()
    print(error.get_message())

# Ejecutar las pruebas
#test_addOne()


def test_addVar():

    parser.symbol_table = {
            "MAIN": {"x": 20, "y": 20, "z": 30},  # Variables globales
            "func1": {"a": 5, "b": 15, "m": True},           # Variables locales en el ámbito 'func1'
            "func2": {"p": 5, "h": 15}
        }
    
    # Caso 1: Se suma un valor a la variable
    addVar_case_1 = AddVar("a", 15, 4)
    parser.current_scope = "func1"
    addVar_case_1.calculate()

    # Caso 2: Se suma a la primera variable la segunda variable
    addVar_case_2 = AddVar("a", "b", 5)
    parser.current_scope = "func1"
    addVar_case_2.calculate()

    # Caso 3: Primer valor es una variable, segundo es una variable inexistente
    addVar_case_3 =  AddVar("a", "c", 6)
    parser.current_scope = "func1"
    addVar_case_3.calculate()

    # Caso 4: Primer valor es una variable existente, segundo es un entero
    addVar_case_4 = AddVar("a", 15, 7)
    parser.current_scope = "func2"
    addVar_case_4.calculate()

    error = ErrorLog()
    print(error.get_message())

# Ejecutar las pruebas
#test_addVar()


# CONDICIONALES
def test_condicionales():

    parser.symbol_table = {
            "MAIN": {"x": 20, "y": 20, "z": 30},  # Variables globales
            "func1": {"a": 5, "b": 15, "m": True},           # Variables locales en el ámbito 'func1'
            "func2": {"p": 5, "h": 15}
        }
    
    # Caso 1: Se suma un valor a la variable
    smaller_case_1 = Equal(9, 15, 3)
    parser.current_scope = "func1"
    smaller_case_1.calculate()

    # Caso 2: Se suma a la primera variable la segunda variable
    smaller_case_2 = Equal(8, "m", 4)
    parser.current_scope = "func1"
    smaller_case_2.calculate()

    # Caso 3: Primer valor es una variable, segundo es una variable inexistente
    smaller_case_3 = Equal("a", 10, 5)
    parser.current_scope = "func1"
    smaller_case_3.calculate()

    # Caso 4: Primer valor es una variable existente, segundo es un entero
    smaller_case_4 = Equal("x", "b", 6)
    parser.current_scope = "func2"
    smaller_case_4.calculate()

    # Caso 5: Primer valor es una variable existente, segundo es un entero
    smaller_case_4 = Equal("m", "b", 7)
    parser.current_scope = "func1"
    smaller_case_4.calculate()

    error = ErrorLog()
    print(error.get_message())

#test_condicionales()


# LOGICAS

def test_logicas():

    parser.symbol_table = {
            "MAIN": {"x": 20, "y": 20, "z": False},  # Variables globales
            "func1": {"a": 5, "b": False, "m": True},           # Variables locales en el ámbito 'func1'
            "func2": {"p": 5, "h": True}
        }
    
    # Caso 1: Se suma un valor a la variable
    and_case_1 = Or("b", True, 3)
    parser.current_scope = "func1"
    and_case_1.calculate()

    # Caso 2: Se suma a la primera variable la segunda variable
    and_case_2 = Or(False, "m", 4)
    parser.current_scope = "func1"
    and_case_2.calculate()

    # Caso 3: Primer valor es una variable, segundo es una variable inexistente
    and_case_3 = Or("z", "h", 5)
    parser.current_scope = "func2"
    and_case_3.calculate()

    # Caso 4: Primer valor es una variable existente, segundo es un entero
    and_case_4 = Or("x", "b", 6)
    parser.current_scope = "func2"
    and_case_4.calculate()

    # Caso 5: Primer valor es una variable existente, segundo es un entero
    and_case_4 = Or("m", "b", 7)
    parser.current_scope = "func2"
    and_case_4.calculate()

    error = ErrorLog()
    print(error.get_message())

test_logicas()


## Prueba ya listas
# Todas ARITMETICAS CON RETORNO y SIN RETORNO PROBADAS
#