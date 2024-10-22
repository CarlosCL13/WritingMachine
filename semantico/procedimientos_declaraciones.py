import analizador_sintactico as parser
from semantico.semantic_Error import *
from semantico.aritmeticas import *

class Programa:
    def __init__(self, proc_compuesto):
        self.proc_compuesto = proc_compuesto

class ProcCompuesto:
    def __init__(self, set_proc, inicio):
        self.set_proc = set_proc   # Contiene una clase con el resto de procedimientos del código fuente
        self.inicio = inicio    # contiene una clase con el procedimiento MAIN
# hacer metodo calculate para esta clase
# Recorrer lista de funciones, y para cada clase funcion llamar a su metodo calculate

#Clase propia del procedimiento MAIN
class Inicio:
    def __init__(self, id_func, cuerpo, line):
        self.nombre = id_func  # Nombre de la función, que en este caso debería ser MAIN
        self.cuerpo = cuerpo  # Contiene una clase con la lista de expresiones y declaraciones dentro del MAIN
        self.line = line  # Línea donde se define la función MAIN

    def calculate(self):
        # Verificar si la función MAIN existe en la tabla de símbolos
        if "main" in parser.symbol_table:
            return None  # La función MAIN existe
        else:
            # Si no se encuentra, generar un error de función no encontrada
            mensaje_error = identificar_error(1, self.line)  # Código de error para función MAIN no encontrada
            error = ErrorLog()
            error.log_error(mensaje_error)
            return None


class SetProc:
    def __init__(self, funciones):
        self.funciones = funciones # lista de objetos procedimientos (clases Funcion)

class Parametros_funcion:
    def __init__(self, lista_parametros):
        self.lista_parametros = lista_parametros  # Lista de parámetros de función

class Parametros_llamada:
    def __init__(self, lista_parametros):
        self.lista_parametros = lista_parametros  # Lista de parámetros de función

class Funcion:
    def __init__(self, id_func, parametros, cuerpo, line):
        self.nombre = id_func  # id de la función
        self.parametros = parametros  # clase que contiene la lista de parámetros
        self.cuerpo = cuerpo  # Clase que contiene lista de expresiones en la función
        self.line = line  # Línea en la que se definió la función

    def calculate(self):
        # Verificar si la función ya existe en la tabla de símbolos
        if self.nombre in parser.symbol_table:
            # Si la función existe, generar un error
            mensaje_error = identificar_error(13, self.line)  # Código de error para función ya definida
            error = ErrorLog()
            error.log_error(mensaje_error)
            return False

        elif self.cuerpo.expresiones == []:
            # Si la función no tiene cuerpo
            mensaje_error = identificar_error(0, self.line)  # Código de error para función sin cuerpo
            error = ErrorLog()
            error.log_error(mensaje_error)
            return False
        
        else:
            parser.symbol_table[self.nombre] = {
                "parametros" : self.parametros.lista_parametros
            }
            return True
# Hacer validación de cada parámetro
# Hacer validación del id de la función (que no exista otra igual)


class Expresion:
    def __init__(self,expresiones):
        self.expresiones = expresiones # lista con expresiones o declaraciones dentro de una función


class Llamada_funcion:
    def __init__(self, id_func, parametros,line):
        self.nombre = id_func
        self.parametros_llamada = parametros  # objeto con lista con los valores de los argumentos cuando el proc fue llamado
        self.line = line

    def calculate(self):
        # Enable que indica si el id de la función llamada fue encontrado
        existe_func_llamada = False

        # contiene la lista de los id de los parámetros cuando fue definida previamente la funcion
        lista_parametros_funcion_def = []

        # contiene los valores de los parametros de la función que fueron dados como argumentos en la llamada 
        lista_parametros_llamada = self.parametros_llamada.lista_parametros 

        # Verificar si el id de la función o procedimiento existe
        for id_funcion in parser.symbol_table:
            if id_funcion == self.nombre:
                # Se obtiene la lista de id's de los parametros (dados en la defincion)
                lista_parametros_funcion_def = parser.symbol_table[id_funcion]["parametros"] # se obtiene la lista con los id de los parametros de la función (cuando fue definida)
                existe_func_llamada = True
                break
        
        if (existe_func_llamada):
            # se verifca que el numero de argumentos dados concuerda con la cantidad de parámetros
            if len(lista_parametros_funcion_def) == len(lista_parametros_llamada):
                # Se añade los valores a los parámetros de la función
                for i in range(0, len(lista_parametros_funcion_def)):
                    # Caso cuando el valor dado como argumento en la llamada es un id
                    if isinstance(lista_parametros_llamada[i], str):
                        # Obtener el diccionario del ámbito actual
                        current_scope_variables = parser.symbol_table[parser.current_scope]
                        
                        # se verifica si el id de la variable dada como argumento está definida en el scope actual
                        if lista_parametros_llamada[i] in current_scope_variables:
                            # se le asigna al parámetro (id) el valor de la variable dada como argumento en la llamada
                            parser.symbol_table[self.nombre][lista_parametros_funcion_def[i]] = current_scope_variables[lista_parametros_llamada[i]]
                        
                        elif lista_parametros_llamada[i] in parser.symbol_table["MAIN"]:
                            # se le asigna a cada parámetro (id) el valor correspondiente dado en los argumentos de llamada de la función (se crea como una variable)
                            parser.symbol_table[self.nombre][lista_parametros_funcion_def[i]] = parser.symbol_table["MAIN"][lista_parametros_llamada[i]]
                        
                        else:
                            # Si la cantidad argumentos dados en la llamada no corresponde al numero de parametros establecidos en la definición, generar un error
                            mensaje_error = identificar_error(6, self.line)
                            error = ErrorLog()
                            error.log_error(mensaje_error)
                            return False 
                            
                    # Caso cuando los valores dados como argumentos son int o bool    
                    else:
                        # se le asigna a cada parámetro (id) el valor correspondiente dado en los argumentos de llamada de la función (se crea como una variable)
                        parser.symbol_table[self.nombre][lista_parametros_funcion_def[i]] = lista_parametros_llamada[i]
                
                return True

            else:
                # Si la cantidad argumentos dados en la llamada no corresponde al numero de parametros establecidos en la definición, generar un error
                mensaje_error = identificar_error(12, self.line)
                error = ErrorLog()
                error.log_error(mensaje_error)
                return False 

        else:
            # Si no existe el nombre del procedimiento en la tabla de simbolos, generar un error
            mensaje_error = identificar_error(13, self.line)  # Código de error si la función no has sido definida
            error = ErrorLog()
            error.log_error(mensaje_error)
            return False 
          

class Def_variable:
    def __init__(self, id_var, expresion_var,line):
        self.nombre = id_var        # Nombre de la variable
        self.valor = expresion_var  # Valor o expresión asignada a la variable
        self.line = line            # Línea donde se declara la variable

    def calculate(self):
        # Obtener el diccionario del ámbito actual
        current_scope_variables = parser.symbol_table[parser.current_scope]
        
        # Verificar si la variable no tiene el mismo identificador de los parámetros de la función
        for id_parametro in current_scope_variables["parametros"]:
            if id_parametro == self.nombre:
                # Si la variable tiene el mismo nombre de un parametros del procedimiento actual, se genera un error
                mensaje_error = identificar_error(14, self.line) # Obtener mensaje de error específico
                error = ErrorLog()
                error.log_error(mensaje_error)
                return False
        
        # Verificar si la variable ya existe en el dicc del ámbito actual
        for variable in current_scope_variables:
            if variable == self.nombre:
                # Si la variable ya existe en el ámbito actual, se genera un error
                mensaje_error = identificar_error(3, self.line) # Obtener mensaje de error específico
                error = ErrorLog()
                error.log_error(mensaje_error)
                return False
            
        # Verificar si la variable ya existe en el ámbito global (MAIN)
        for variable in parser.symbol_table["MAIN"]:
            if variable == self.nombre:
                # Si la variable ya existe en el ámbito global, se genera un error
                mensaje_error = identificar_error(3, self.line)  # Obtener mensaje de error específico
                error = ErrorLog()
                error.log_error(mensaje_error)
                return False
        
        # Si la variable no existe en ninguno de los ámbitos, se crea la variable
        parser.symbol_table[parser.current_scope][self.nombre] = self.valor 
        # Se regresa True para indicar la variable fue creada con éxito
        return True
    
class Put:
    def __init__(self, id_var, expresion_var, line):
        self.nombre = id_var  # Nombre de la variable a actualizar
        self.valor = expresion_var  # Nuevo valor para la variable
        self.line = line  # Línea donde se actualiza la variable

    def calculate(self):
        # Obtener el diccionario de variables del ámbito actual
        current_scope_variables = parser.symbol_table[parser.current_scope]

        # Verificar si la variable no tiene el mismo identificador de los parámetros de la función
        for id_parametro in current_scope_variables["parametros"]:
            if id_parametro == self.nombre:
                # Si la variable tiene el mismo nombre de un parametro del procedimiento actual, se genera un error
                mensaje_error = identificar_error(8, self.line) # Obtener mensaje de error específico
                error = ErrorLog()
                error.log_error(mensaje_error)
                return False

        # Verificar si la variable existe en el ámbito actual
        for variable in current_scope_variables:
            if variable == self.nombre:
                # Verificar si el tipo antiguo de la variable es igual al nuevo
                return self.verificar_tipo(current_scope_variables[variable], self.valor)

        # Verificar si la variable existe en el ámbito global (MAIN)
        for variable in parser.symbol_table["MAIN"]:
            if variable == self.nombre:
                # Verificar si el tipo antiguo de la variable es igual al nuevo en el MAIN
                return self.verificar_tipo(current_scope_variables[variable], self.valor)

        # Si no se encontró la variable en ninguno de los ámbitos
        mensaje_error = identificar_error(6, self.line)  # Error de variable no encontrada
        error = ErrorLog()
        error.log_error(mensaje_error)
        return False

    def verificar_tipo(self, valor_antiguo, valor_nuevo):

        # Verificar si el tipo antiguo de la variable es igual al nuevo
        if isinstance(valor_antiguo, int) and isinstance(valor_nuevo,int) :
            return True  # Tipos coinciden
        
        elif isinstance(valor_antiguo, bool) and isinstance(valor_nuevo,bool):
            return True  # Tipos coinciden
        
        elif isinstance(valor_antiguo, Div) and isinstance(valor_nuevo,Div):
            return True
        
        elif isinstance(valor_antiguo, Mult) and isinstance(valor_nuevo,Mult):
            return True
        
        elif isinstance(valor_antiguo, Sum) and isinstance(valor_nuevo,Sum):
            return True
        
        elif isinstance(valor_antiguo, Substr) and isinstance(valor_nuevo,Substr):
            return True
        
        elif isinstance(valor_antiguo, Random) and isinstance(valor_nuevo,Random):
            return True
        
        else:
            # Error de tipo, no coincide con int o bool
            mensaje_error = identificar_error(11, self.line)  # Error de tipo
            error = ErrorLog()
            error.log_error(mensaje_error)
            return False


"""
Put: que ya exista el id y que el tipo del valor antiguo sea igual al que se quiere colocar nuevo  / CREO QUE FALTA LO DE LAS OPERACIONES, PERZO NO SÉ COMO SE HACE XD

validación de Llamada_funcion: que el id ya exista en la tabla de simbolos, y el tipo de cada parametro

validacion de funcion: id no exista en la tabla de simbolos, y recorrer lista de parámetros para comprobar / FALTA ALGO?

Def_variable: id no existe en la tabla de simbolos
Inicio: comprobar que exista el procedimiento MAIN en la tabla de simbolos
"""