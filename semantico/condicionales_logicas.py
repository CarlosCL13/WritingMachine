#import analizador_sintactico as parser
import analizador_sintactico as parser
from semantico.semantic_Error import *

# ////////////////////////////////////////////////  Verificación para condicionales //////////////////////////////////////////////// 
        
class Smaller:
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
            if self.second_value in current_scope_variables:
                if isinstance(current_scope_variables[self.second_value], int) and not isinstance(current_scope_variables[self.second_value], bool):
                    return None  # La variable es un entero

            # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            if self.second_value in parser.symbol_table["MAIN"]:
                if isinstance(parser.symbol_table["MAIN"][self.second_value], int) and not isinstance(parser.symbol_table["MAIN"][self.second_value], bool):
                    return None  # La variable es un entero
            
            # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
        
        # Caso donde el primer parametro es una variable y el segundo un numero
        elif isinstance(self.first_value, str) and isinstance(self.second_value, int):
            
            # se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            # Se comprueba si la  variable existe en el ambito o alcance atual
            if self.first_value in current_scope_variables:
                if isinstance(current_scope_variables[self.first_value], int) and not isinstance(current_scope_variables[self.first_value], bool):
                    return None  # La variable es un entero
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            if self.first_value in parser.symbol_table["MAIN"]:
                if isinstance(parser.symbol_table["MAIN"][self.first_value], int) and not isinstance(parser.symbol_table["MAIN"][self.first_value], bool):
                    return None  # La variable es un entero
            
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

                if (variable == self.first_value) and isinstance(current_scope_variables[self.first_value], int) and not isinstance(current_scope_variables[self.first_value], bool):
                    variable_1_correcta = True

                if (variable == self.second_value) and isinstance(current_scope_variables[self.second_value], int) and not isinstance(current_scope_variables[self.second_value], bool):
                    variable_2_correcta = True

                if variable_1_correcta and variable_2_correcta:
                    return None

                
            for variable in parser.symbol_table["MAIN"]:

                if (variable == self.first_value) and isinstance(parser.symbol_table["MAIN"][self.first_value], int) and not isinstance(parser.symbol_table["MAIN"][self.first_value], bool):
                    variable_1_correcta = True;

                if (variable == self.second_value) and isinstance(parser.symbol_table["MAIN"][self.second_value], int) and not isinstance(parser.symbol_table["MAIN"][self.second_value], bool):
                    variable_2_correcta = True
                    
                if variable_1_correcta and variable_2_correcta:
                    return None
     
            # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)

        return None

class Equal:
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
            if self.second_value in current_scope_variables:
                if isinstance(current_scope_variables[self.second_value], int) and not isinstance(current_scope_variables[self.second_value], bool):
                    return None  # La variable es un entero

            # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            if self.second_value in parser.symbol_table["MAIN"]:
                if isinstance(parser.symbol_table["MAIN"][self.second_value], int) and not isinstance(parser.symbol_table["MAIN"][self.second_value], bool):
                    return None  # La variable es un entero
            
            # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
        
        # Caso donde el primer parametro es una variable y el segundo un numero
        elif isinstance(self.first_value, str) and isinstance(self.second_value, int):
            
            # se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            # Se comprueba si la  variable existe en el ambito o alcance atual
            if self.first_value in current_scope_variables:
                if isinstance(current_scope_variables[self.first_value], int) and not isinstance(current_scope_variables[self.first_value], bool):
                    return None  # La variable es un entero
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            if self.first_value in parser.symbol_table["MAIN"]:
                if isinstance(parser.symbol_table["MAIN"][self.first_value], int) and not isinstance(parser.symbol_table["MAIN"][self.first_value], bool):
                    return None  # La variable es un entero
            
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

                if (variable == self.first_value) and isinstance(current_scope_variables[self.first_value], int) and not isinstance(current_scope_variables[self.first_value], bool):
                    variable_1_correcta = True

                if (variable == self.second_value) and isinstance(current_scope_variables[self.second_value], int) and not isinstance(current_scope_variables[self.second_value], bool):
                    variable_2_correcta = True

                if variable_1_correcta and variable_2_correcta:
                    return None

                
            for variable in parser.symbol_table["MAIN"]:

                if (variable == self.first_value) and isinstance(parser.symbol_table["MAIN"][self.first_value], int) and not isinstance(parser.symbol_table["MAIN"][self.first_value], bool):
                    variable_1_correcta = True;

                if (variable == self.second_value) and isinstance(parser.symbol_table["MAIN"][self.second_value], int) and not isinstance(parser.symbol_table["MAIN"][self.second_value], bool):
                    variable_2_correcta = True
                    
                if variable_1_correcta and variable_2_correcta:
                    return None
     
            # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)

        return None

class Greater:
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
            if self.second_value in current_scope_variables:
                if isinstance(current_scope_variables[self.second_value], int) and not isinstance(current_scope_variables[self.second_value], bool):
                    return None  # La variable es un entero

            # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            if self.second_value in parser.symbol_table["MAIN"]:
                if isinstance(parser.symbol_table["MAIN"][self.second_value], int) and not isinstance(parser.symbol_table["MAIN"][self.second_value], bool):
                    return None  # La variable es un entero
            
            # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
        
        # Caso donde el primer parametro es una variable y el segundo un numero
        elif isinstance(self.first_value, str) and isinstance(self.second_value, int):
            
            # se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            # Se comprueba si la  variable existe en el ambito o alcance atual
            if self.first_value in current_scope_variables:
                if isinstance(current_scope_variables[self.first_value], int) and not isinstance(current_scope_variables[self.first_value], bool):
                    return None  # La variable es un entero
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            if self.first_value in parser.symbol_table["MAIN"]:
                if isinstance(parser.symbol_table["MAIN"][self.first_value], int) and not isinstance(parser.symbol_table["MAIN"][self.first_value], bool):
                    return None  # La variable es un entero
            
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

                if (variable == self.first_value) and isinstance(current_scope_variables[self.first_value], int) and not isinstance(current_scope_variables[self.first_value], bool):
                    variable_1_correcta = True

                if (variable == self.second_value) and isinstance(current_scope_variables[self.second_value], int) and not isinstance(current_scope_variables[self.second_value], bool):
                    variable_2_correcta = True

                if variable_1_correcta and variable_2_correcta:
                    return None

                
            for variable in parser.symbol_table["MAIN"]:

                if (variable == self.first_value) and isinstance(parser.symbol_table["MAIN"][self.first_value], int) and not isinstance(parser.symbol_table["MAIN"][self.first_value], bool):
                    variable_1_correcta = True;

                if (variable == self.second_value) and isinstance(parser.symbol_table["MAIN"][self.second_value], int) and not isinstance(parser.symbol_table["MAIN"][self.second_value], bool):
                    variable_2_correcta = True
                    
                if variable_1_correcta and variable_2_correcta:
                    return None
     
            # Se crea el error
            mensaje_error = identificar_error(4,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
        
        return None


# ////////////////////////////////////////////// Verificación para lógicas ////////////////////////////////////////////

class And:
    # Constructor
    def __init__(self, x, y, line):
        self.first_value = x    # puede ser un ID o un bool
        self.second_value = y   # puede ser un ID o un bool
        self.line = line

    # Comprobacion semantica
    def calculate(self):
        
        # Caso donde ambos parametros son numeros
        if isinstance(self.first_value, bool) and isinstance(self.second_value, bool):
            return None # los dos operandos eran enteros inmediatos
        
        # Caso donde el primer parametro es numero y el segundo es una variable
        elif isinstance(self.first_value, bool) and isinstance(self.second_value, str):
            
            # se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            # Se comprueba si la  variable existe en el ambito o alcance atual
            if self.second_value in current_scope_variables:
                if isinstance(current_scope_variables[self.second_value], bool):
                    return None # se encontró la variable
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            if self.second_value in parser.symbol_table["MAIN"]:
                if isinstance(parser.symbol_table["MAIN"][self.second_value], bool):
                    return None
            
            # Se crea el error
            mensaje_error = identificar_error(5,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
        
        # Caso donde el primer parametro es una variable y el segundo un numero
        elif isinstance(self.first_value, str) and isinstance(self.second_value, bool):
            
            # se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            if self.first_value in current_scope_variables:
                if isinstance(current_scope_variables[self.first_value], bool):
                    return None # se encontró la variable
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            if self.first_value in parser.symbol_table["MAIN"]:
                if isinstance(parser.symbol_table["MAIN"][self.first_value], bool):
                    return None
            
            # Se crea el error
            mensaje_error = identificar_error(5,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
        
        # Caso donde ambos parametros son variables
        elif isinstance(self.first_value, str) and isinstance(self.second_value,str):
            
            # se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]
            variable_1_correcta = False
            variable_2_correcta = False


            for variable in current_scope_variables:

                if variable == self.first_value and isinstance(current_scope_variables[self.first_value], bool):
                    variable_1_correcta = True

                if variable == self.second_value and isinstance(current_scope_variables[self.second_value], bool):
                    variable_2_correcta = True

                if variable_1_correcta and variable_2_correcta:
                    return None

                
            for variable in parser.symbol_table["MAIN"]:

                if variable == self.first_value and isinstance(parser.symbol_table["MAIN"][self.first_value], bool):
                    variable_1_correcta = True;

                if variable == self.second_value and isinstance(parser.symbol_table["MAIN"][self.second_value], bool):
                    variable_2_correcta = True
                    
                if variable_1_correcta and variable_2_correcta:
                    return None
     
            # Se crea el error
            mensaje_error = identificar_error(5,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)

class Or:
    # Constructor
    def __init__(self, x, y, line):
        self.first_value = x    # puede ser un ID o un bool
        self.second_value = y   # puede ser un ID o un bool
        self.line = line

    # Comprobacion semantica
    def calculate(self):
        
        # Caso donde ambos parametros son numeros
        if isinstance(self.first_value, bool) and isinstance(self.second_value, bool):
            return None # los dos operandos eran enteros inmediatos
        
        # Caso donde el primer parametro es numero y el segundo es una variable
        elif isinstance(self.first_value, bool) and isinstance(self.second_value, str):
            
            # se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            # Se comprueba si la  variable existe en el ambito o alcance atual
            for variable in current_scope_variables:
                if variable == self.second_value and isinstance(current_scope_variables[self.second_value], bool):
                    return None # se encontró la variable
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            for variable in parser.symbol_table["MAIN"]:
                if variable == self.second_value and isinstance(parser.symbol_table["MAIN"][self.second_value], bool):
                    return None
            
            # Se crea el error
            mensaje_error = identificar_error(5,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
        
        # Caso donde el primer parametro es una variable y el segundo un numero
        elif isinstance(self.first_value, str) and isinstance(self.second_value, bool):
            
            # se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]

            for variable in current_scope_variables:
                if variable == self.first_value and isinstance(current_scope_variables[self.first_value], bool):
                    return None # se encontró la variable
           
           # Si la variable no se encontró en el ambito actual se consulta si está en el MAIN como global
            for variable in parser.symbol_table["MAIN"]:
                if variable == self.first_value and isinstance(parser.symbol_table["MAIN"][self.first_value], bool):
                    return None
            
            # Se crea el error
            mensaje_error = identificar_error(5,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)
            
        
        # Caso donde ambos parametros son variables
        elif isinstance(self.first_value, str) and isinstance(self.second_value,str):
            
            # se obtiene un diccionario propio del ambito actual, es decir las variables del ambito actual
            current_scope_variables = parser.symbol_table[parser.current_scope]
            variable_1_correcta = False
            variable_2_correcta = False


            for variable in current_scope_variables:

                if variable == self.first_value and isinstance(current_scope_variables[self.first_value], bool):
                    variable_1_correcta = True

                if variable == self.second_value and isinstance(current_scope_variables[self.second_value], bool):
                    variable_2_correcta = True

                if variable_1_correcta and variable_2_correcta:
                    return None

                
            for variable in parser.symbol_table["MAIN"]:

                if variable == self.first_value and isinstance(parser.symbol_table["MAIN"][self.first_value], bool):
                    variable_1_correcta = True;

                if variable == self.second_value and isinstance(parser.symbol_table["MAIN"][self.second_value], bool):
                    variable_2_correcta = True
                    
                if variable_1_correcta and variable_2_correcta:
                    return None
     
            # Se crea el error
            mensaje_error = identificar_error(5,self.line)   # se obtiene el mensaje específico del error
            error = ErrorLog()
            error.log_error(mensaje_error)

        return None