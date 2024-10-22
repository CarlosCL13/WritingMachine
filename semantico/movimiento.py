import analizador_sintactico as parser
from semantico.semantic_Error import *

class ContinueUp:
    # Constructor
    def __init__(self, x, line):
        self.value_n = x
        self.line = line

    # Comprobacion semantica de que el valor dado haya sido un número
    def calculate(self):
        if isinstance(self.value_n, int):
            return None # el operando es un entero

        # se comprueba que el operando sea una variable ID
        elif isinstance(self.value_n, str):
            
            # se obtiene una lista de variables propias del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            for variable in current_scope_variables:
                # Se comprueba que la variable esté definida y que su valor sea un entero
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None # se encontró la variable
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            for variable in parser.symbol_table["MAIN"]:
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None

             # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
            return None
    

class ContinueDown:
    # Constructor
    def __init__(self, x, line):
        self.value_n = x
        self.line = line

    # Comprobacion semantica de que el valor dado haya sido un número
    def calculate(self):
        if isinstance(self.value_n, int):
            return None # el operando es un entero

        # se comprueba que el operando sea una variable ID
        elif isinstance(self.value_n, str):
            
            # se obtiene una lista de variables propias del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            for variable in current_scope_variables:
                # Se comprueba que la variable esté definida y que su valor sea un entero
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None # se encontró la variable
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            for variable in parser.symbol_table["MAIN"]:
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None

             # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
            return None
    

class continueRight:
   # Constructor
    def __init__(self, x, line):
        self.value_n = x
        self.line = line

    # Comprobacion semantica de que el valor dado haya sido un número
    def calculate(self):
        if isinstance(self.value_n, int):
            return None # el operando es un entero

        # se comprueba que el operando sea una variable ID
        elif isinstance(self.value_n, str):
            
            # se obtiene una lista de variables propias del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            for variable in current_scope_variables:
                # Se comprueba que la variable esté definida y que su valor sea un entero
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None # se encontró la variable
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            for variable in parser.symbol_table["MAIN"]:
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None

             # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
            return None
    

class ContinueLeft:
    # Constructor
    def __init__(self, x, line):
        self.value_n = x
        self.line = line

    # Comprobacion semantica de que el valor dado haya sido un número
    def calculate(self):
        if isinstance(self.value_n, int):
            return None # el operando es un entero

        # se comprueba que el operando sea una variable ID
        elif isinstance(self.value_n, str):
            
            # se obtiene una lista de variables propias del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            for variable in current_scope_variables:
                # Se comprueba que la variable esté definida y que su valor sea un entero
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None # se encontró la variable
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            for variable in parser.symbol_table["MAIN"]:
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None

             # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
            return None


class Pos:
    # Constructor
    def __init__(self, x, y, line):
        self.first_value = x    # puede ser un ID o un numero
        self.second_value = y   # puede ser un ID o un numero
        self.line = line

    # Comprobacion semantica
    def calculate(self):
        
        # Caso donde ambos parametros son numeros
        if isinstance(self.first_value, int) and isinstance(self.second_value, int):
            return None # los dos operandos eran enteros inmediatos
        
        # Caso donde el primer parametro es numero y el segundo es una variable
        elif isinstance(self.first_value, int) and isinstance(self.second_value, str):
            
            # se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            # Se comprueba si la  variable existe en el ambito o alcance atual
            for variable in current_scope_variables:
                if variable[0] == self.second_value and isinstance(variable[1], int):
                    return None # se encontró la variable
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            for variable in parser.symbol_table["MAIN"]:
                if variable[0] == self.second_value and isinstance(variable[1], int):
                    return None
            
            # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
        
        # Caso donde el primer parametro es una variable y el segundo un numero
        elif isinstance(self.first_value, str) and isinstance(self.second_value, int):
            
            # se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            for variable in current_scope_variables:
                if variable[0] == self.first_value and isinstance(variable[1], int):
                    return None # se encontró la variable
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            for variable in parser.symbol_table["MAIN"]:
                if variable[0] == self.first_value and isinstance(variable[1], int):
                    return None
            
            # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
        
        # Caso donde ambos parametros son variables
        elif isinstance(self.first_value, str) and isinstance(self.second_value,str):
            
            # se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]
            variable_1_correcta = False
            variable_2_correcta = False


            for variable in current_scope_variables:

                if variable[0] == self.first_value and isinstance(variable[1], int):
                    variable_1_correcta = True

                if variable[0] == self.second_value and isinstance(variable[1], int):
                    variable_2_correcta = True

                if variable_1_correcta and variable_2_correcta:
                    return None

                
            for variable in parser.symbol_table["MAIN"]:

                if variable[0] == self.first_value and isinstance(variable[1], int):
                    variable_1_correcta = True;

                if variable[0] == self.second_value and isinstance(variable[1], int):
                    variable_2_correcta = True
                    
                if variable_1_correcta and variable_2_correcta:
                    return None
     
            # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
            return None
    

class PosX:
    # Constructor
    def __init__(self, x, line):
        self.value_n = x
        self.line = line

    # Comprobacion semantica de que el valor dado haya sido un número
    def calculate(self):
        if isinstance(self.value_n, int):
            return None # el operando es un entero

        # se comprueba que el operando sea una variable ID
        elif isinstance(self.value_n, str):
            
            # se obtiene una lista de variables propias del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            for variable in current_scope_variables:
                # Se comprueba que la variable esté definida y que su valor sea un entero
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None # se encontró la variable
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            for variable in parser.symbol_table["MAIN"]:
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None

             # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
            return None

    
class PosY:
    # Constructor
    def __init__(self, x, line):
        self.value_n = x
        self.line = line

    # Comprobacion semantica de que el valor dado haya sido un número
    def calculate(self):
        if isinstance(self.value_n, int):
            return None # el operando es un entero

        # se comprueba que el operando sea una variable ID
        elif isinstance(self.value_n, str):
            
            # se obtiene una lista de variables propias del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            for variable in current_scope_variables:
                # Se comprueba que la variable esté definida y que su valor sea un entero
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None # se encontró la variable
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            for variable in parser.symbol_table["MAIN"]:
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None

            # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
            return None

    
class UseColor:
   # Constructor
    def __init__(self, x, line):
        self.value_n = x
        self.line = line

    # Comprobacion semantica de que el valor dado haya sido un número
    def calculate(self):
        if isinstance(self.value_n, int) and (self.value_n == 1 or self.value_n == 2):
            return None # el operando es un entero

        # se comprueba que el operando sea una variable ID
        elif isinstance(self.value_n, str) and (self.value_n == 1 or self.value_n == 2):
            
            # se obtiene una lista de variables propias del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            for variable in current_scope_variables:
                # Se comprueba que la variable esté definida y que su valor sea un entero
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None # se encontró la variable
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            for variable in parser.symbol_table["MAIN"]:
                if variable[0] == self.value_n and isinstance(variable[1], int):
                    return None

            # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)

        else:
             # Se crea el error, pues n no es ni 1 ni 2
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
            return None
        
class Up:
    def __init__(self, reservada_instruccion ,line):
        self.reservada_instruccion =reservada_instruccion
        self.line = line

class Down:
    def __init__(self, reservada_instruccion ,line):
        self.reservada_instruccion =reservada_instruccion
        self.line = line

class Beginnig:
    def __init__(self, reservada_instruccion ,line):
        self.reservada_instruccion =reservada_instruccion
        self.line = line

