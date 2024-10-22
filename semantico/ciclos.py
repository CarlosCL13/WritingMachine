import analizador_sintactico as parser
from semantico.semantic_Error import *


class While:
    def __init__(self,condicion,cuerpo,line):
        self.condicion = condicion  # se obtiene un objeto de la condición
        self.cuerpo = cuerpo # objeto con lista de las expresiones dentro del bloque
        self.line = line

class For:
    def __init__(self,id_var_for,min_valor,max_valor,cuerpo,line):
        self.id_var = id_var_for  # nombre de la variable con el valor del rango en cada iteración
        self.max_valor = max_valor  # indica el valor máximo el rango
        self.min_valor = min_valor  # indicia el valor minimo del rango
        self.cuerpo = cuerpo # objeto con lista de las expresiones dentro del bloque
        self.line = line
    
    def calculate(self):
        
        if isinstance(self.id_var, str): 
            # Se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            # Se comprueba si la  variable existe en el ambito o alcance actual
            for variable in current_scope_variables:
                if variable[0] == self.id_var:
                    # Si existe crea el error
                    mensaje_error = identificar_error(3,self.line)   # se obtiene el mensaje específico del error
                    error = ErrorLog()
                    error.log_error(mensaje_error)
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            for variable in parser.symbol_table["MAIN"]:
                if variable[0] == self.id_var:
                    # Si existe crea el error
                    mensaje_error = identificar_error(3,self.line)   # se obtiene el mensaje específico del error
                    error = ErrorLog()
                    error.log_error(mensaje_error)
            
        if (self.max_valor < self.min_valor):
            # Si max_valor es menor que min_valor lo cual no tiene sentido
            # Se crea el error
            mensaje_error = identificar_error(10,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)

        else:
            return None


class Repeat:
    def __init__(self,cuerpo,condicion,line):
        self.cuerpo = cuerpo
        self.condicion = condicion
        self.line = line
    
class Case:
    def __init__(self, id_var_case,condiciones_when,else_condicion,line):
        self.id_var = id_var_case 
        self.condiciones = condiciones_when # objeto con lista de todas las condiciones when
        self.condicion_else = else_condicion # objeto con lista de expresiones
        self.line = line

    def calculate(self):
        valor_id = None
        # Caso donde el primer parametro es numero y el segundo es una variable
        if isinstance(self.id_var, str):
            # se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]
            
            error_var = True
            
            for variable in current_scope_variables:
                if variable[0] == self.id_var:
                    valor_id = variable[1]
                    error_var = False
                    break
            
            # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            for variable in parser.symbol_table["MAIN"]:
                if variable[0] == self.id_var:
                    valor_id = variable[1]
                    error_var = False
                    break
                
            if(error_var):
                # Se crea el error
                mensaje_error = identificar_error(6,self.line)   # se obtiene el mensaje específico del error
                error = ErrorLog()
                error.log_error(mensaje_error)
        
        lista_whens = self.condiciones.lista_when

        for when in lista_whens:
            if isinstance(when.valor_var, int) and isinstance(valor_id, int):
                return None
            elif isinstance(when.valor_var, bool) and isinstance(valor_id, bool):
                return None
            else:
                # Se crea el error
                mensaje_error = identificar_error(11,self.line)   # se obtiene el mensaje específico del error
                error = ErrorLog()
                error.log_error(mensaje_error)
                return None
        

class Bloque_when:
    def __init__(self, lista_when):
        self.lista_when = lista_when # contiene lista con objetos de las condiciones when

class When:
    def __init__(self, valor_var, cuerpo,line):
        self.valor_var = valor_var  # valor de la variable a comparar
        self.cuerpo = cuerpo  # objeto con lista de expresiones dentro del bloque when
        self.line = line

class Else:
    def __init__(self, cuerpo,line):
        self.cuerpo = cuerpo  # objeto con lista de expresiones dentro del bloque else
        self.line = line



"""
For: validar Id que no exista en la Tabla de simbolos, el valor max sea mayor estricto que el valor minimo
Case: validar Id que exista en la Tabla de simbolos, comprobar que el tipo de la variable sea igual al tipo dado en cada condición when
"""