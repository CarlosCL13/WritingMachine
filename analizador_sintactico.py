# LIBRERÍAS
import ply.yacc as yacc
from analizador_lexico import tokens
from semantico.aritmeticas import *
from semantico.condicionales_logicas import *
from semantico.movimiento import *
from semantico.procedimientos_declaraciones import *
from semantico.ciclos import *

# GLOBALES
symbol_table = {}
errores_sintacticos = []  # Lista global para almacenar errores sintácticos
current_scope = None

precedence = (
	('right','PROC'),
    ('left','MAIN'),
	)


# //////////////////////    ESTRUCTURA DE GENERACION DE BLOQUES DE CÓDIGO /////////////////////////
#SEMÁNTICO ---> 'procedimientos_declaraciones.py'

def p_programa(p):
        """programa : proc_compuesto"""

        p[0] = Programa(p[1])
        pass

# Pemite que el procedimiento MAIN pueda estar tanto al inicio del programa, entre funciones o al final del programa
def p_proc_compuesto(p):
    """proc_compuesto : set_proc inicio set_proc
                    | set_proc inicio
                    | inicio set_proc
                    | inicio"""

    if len(p) == 4:
        # Caso donde hay dos `set_proc`: se combinan las listas de funciones de ambos para crear uno solo
        funciones = p[1].funciones + p[3].funciones
        nuevo_set_proc = SetProc(funciones)
        p[0] = ProcCompuesto(nuevo_set_proc, p[2])
    
    elif len(p) == 3:
        if isinstance(p[1], SetProc):
            # Caso ---> proc_compuesto: set_proc inicio
            p[0] = ProcCompuesto(p[1], p[2])
        else:
            # Caso ---> proc_compuesto: inicio set_proc
            p[0] = ProcCompuesto(p[2], p[1])
    
    else:
        # Caso ---> proc_compuesto: inicio
        p[0] = ProcCompuesto(SetProc([]), p[1])

    pass

# Estructura del procedimiento MAIN
def p_inicio(p):
    """inicio : MAIN PARENTESIS_IZQ PARENTESIS_DER PARENTESISC_IZQ expresion PARENTESISC_DER PUNTOCOMA END PUNTOCOMA"""
    
    line = p.lineno(1)
    p[0] = Inicio(p[1],p[5],line)
    
    pass

# Permite colocar cualquier cantidad de funciones o procedimientos que sean necesarios
def p_set_proc(p):
    """set_proc : funcion set_proc
                | funcion"""
    
    # caso para la primera regla
    if len(p) == 3:
        lista_funciones = [p[1]] + p[2].funciones  # se concatenan listas con objetos de procedimientos
        p[0] = SetProc(lista_funciones)
    #caso para la segunda regla
    else:
        p[0] = SetProc([p[1]])

    pass

# Instrucciones o expresiones que se pueden colocar dentro de funciones
def p_expresion(p):
    """expresion : def_variable expresion
                    | put expresion
                    | llamada_funcion expresion
                    | aritmeticas_No_return expresion
                    | movimiento expresion
                    | for expresion
                    | while expresion
                    | repeat expresion
                    | case expresion
                    | empty"""
    if p[1] is None:
        p[0] = Expresion([])

    else:
        lista_expresiones = [p[1]] + p[2].expresiones # se concatenan las listas de expresiones (en las iteraciones)
        p[0] = Expresion(lista_expresiones)

    pass

# Parámetros que se pueden colocar al definir una variable
def p_expresion_var(p):
    """expresion_var : numero
                    | bool
                    | aritmeticas_return"""
    
    p[0] = p[1]

    pass


# Colocación de parámetros en una función
def p_parametros_funcion(p):
    """parametros_funcion: expresion_param_funcion COMA parametros_funcion
                    | expresion_param_funcion"""
    
    # Caso de la primera regla
    if len(p) == 4:
        # se concatena el parámetro actual con los siguientes
        lista_parametros = [p[1]] + p[3].lista_parametros
        p[0] = Parametros_funcion(lista_parametros)

    # Caso de la segunda regla
    else:
        # Caso cuando la función o procedimiento no tiene parámetros
        if (p[1] is None):
            p[0] = Parametros_funcion([])

        # Caso cunado la función o procedimiento tiene un solo parámetro
        else:
            p[0] = Parametros_funcion([p[1]])

    pass

# colocación de parámetros al llamar a una función o procedimiento
def p_parametros_llamada(p):
    """parametros_llamada: expresion_param_llamada COMA parametros_llamada
                    | expresion_param_llamada"""
    
    # Caso de la primera regla
    if len(p) == 4:
        # se concatena el parámetro actual con los siguientes
        lista_parametros = [p[1]] + p[3].lista_parametros
        p[0] = Parametros_llamada(lista_parametros)

    # Caso de la segunda regla
    else:
        # Caso cuando la función o procedimiento no tiene parámetros
        if (p[2] is None):
            p[0] = Parametros_llamada([])

        # Caso cunado la función o procedimiento tiene un solo parámetro
        else:
            p[0] = Parametros_llamada([p[1]])

    pass

# Parámetros que se pueden colocar en los argumentos de una función
def p_expresion_param1(p):
    """expresion_param_funcion : id
                    | numero
                    | bool
                    | empty"""

    p[0] = p[1]

    pass

# Parámetros que se pueden colocar en los argumentos cuando se llama a una función o procedimiento
def p_expresion_param2(p):
    """expresion_param_llamada : id
                                | numero
                                | bool
                                | empty"""

    p[0] = p[1]

    pass

# Parámetros o datos que se pueden colocar como argumentos de una función de operación aritmética
def p_expresion_op(p):
    """expresion_op : id
                    | numero"""

    p[0] = p[1]
    pass

# Parámetros o datos que se pueden colocar como argumentos de una función operación lógica
def p_expresion_log(p):
    """expresion_log : id
                    | bool"""
    p[0] = p[1]
    pass


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# =================================== ESTRUCTURA DE INSTRUCCIONES DE DEFINICION DE FUNCIONES ===================================
#SEMÁNTICO ---> 'procedimientos_declaraciones.py'

def p_funcion(p):
    """funcion : PROC id PARENTESIS_IZQ parametros_funcion PARENTESIS_DER PARENTESISC_IZQ expresion PARENTESISC_DER PUNTOCOMA END PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = Funcion(p[2], p[4], p[7],line)

    pass

# =================================== ESTRUCTURA DE INSTRUCCIONES DE LLAMADA A FUNCIONES O PROCEDIMIENTOS ===================================
#SEMÁNTICO ---> 'procedimientos_declaraciones.py'

def p_llamada_funcion(p):
    """llamada_funcion : id PARENTESIS_IZQ parametros_llamada PARENTESIS_DER PUNTOCOMA"""
    
    line = p.lineno(1)
    p[0] = Llamada_funcion(p[1],p[3],line)
    pass

# =================================== ESTRUCTURA DE INSTRUCCIONES DE DEFINICION DE VARIABLES ===================================
#SEMÁNTICO ---> 'procedimientos_declaraciones.py'

def p_def_variable(p):
    """def_variable : DEF PARENTESIS_IZQ id COMA expresion_var PARENTESIS_DER PUNTOCOMA"""
    
    line = p.lineno(1)
    p[0] = Def_variable(p[3],p[5],line)

    pass

# =================================== ESTRUCTURA DE INSTRUCCIONES DE MODIFICACION DE VARIABLES ===================================
#SEMÁNTICO ---> 'procedimientos_declaraciones.py'

def p_put(p):
    """put : PUT PARENTESIS_IZQ id COMA expresion_var PARENTESIS_DER PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = Put(p[3],p[5],line)

    pass


# =================================== ESTRUCTURA DE INSTRUCCIONES ARITMÉTICAS ===================================
#SEMÁNTICO ---> 'aritmeticas.py'

def p_div(p):
    """aritmeticas_return: DIV PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER"""
    line = p.lineno(1)
    p[0] = Div(p[3], p[5], line);

def p_mult(p):
    """aritmeticas_return: MULT PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER"""
    line = p.lineno(1)
    p[0] = Mult(p[3], p[5], line);

def p_sum(p):
    """aritmeticas_return: SUM PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER"""
    line = p.lineno(1)
    p[0] = Sum(p[3], p[5], line);

def p_substr(p):
    """aritmeticas_return: SUBSTR PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER"""
    line = p.lineno(1)
    p[0] = Substr(p[3], p[5], line);

def p_random(p):
    """aritmeticas_return: RANDOM PARENTESIS_IZQ expresion_op PARENTESIS_DER"""

    line = p.lineno(1)
    p[0] = Random(p[3],line)
    pass

 # operaciones que no retornan valor
def p_add1(p):
    """aritmeticas_No_return: ADD PARENTESIS_IZQ id PARENTESIS_DER PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = AddOne(p[3],line)
    pass

def p_add2(p):
    """aritmeticas_No_return:  ADD PARENTESIS_IZQ id COMA expresion_op PARENTESIS_DER PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = AddVar(p[3],p[5],line)
    pass



# ============================================= ESTRUCTURA DE INSTRUCCIONES LOGICAS ==============================================
#SEMÁNTICO ---> 'condicionales_logicas.py'

def p_and(p):
    """logicas : AND PARENTESIS_IZQ expresion_log COMA expresion_log PARENTESIS_DER"""

    line = p.lineno(1)
    p[0] = And(p[3],p[5],line)
    pass

def p_or(p):
    """logicas : OR PARENTESIS_IZQ expresion_log COMA expresion_log PARENTESIS_DER"""

    line = p.lineno(1)
    p[0] = Or(p[3],p[5],line)
    pass



# ============================================= ESTRUCTURA DE INSTRUCCIONES CONDICIONALES ==============================================
#SEMÁNTICO ---> 'condicionales_logicas.py'

def p_greater(p):
    """condicionales: GREATER PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER"""

    line = p.lineno(1)
    p[0] = Greater(p[3],p[5],line)
    pass

def p_smaller(p):
    """condicionales: SMALLER PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER"""

    line = p.lineno(1)
    p[0] = Smaller(p[3],p[5],line)
    pass

def p_equal(p):
    """condicionales: EQUAL PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER"""

    line = p.lineno(1)
    p[0] = Equal(p[3],p[5],line)

    pass

# =========================================== ESTRUCTURA DE INSTRUCCIONES DE MOVIMIENTO ===================================
#SEMÁNTICO ---> 'movimiento.py'

def p_continueUp(p):
    """movimiento : CONTINUEUP expresion_op PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = ContinueUp(p[2],line)

    pass

def p_continueDown(p):
    """movimiento : CONTINUEDOWN expresion_op PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = ContinueDown(p[2],line)
    
    pass

def p_continueRight(p):
    """movimiento : CONTINUERIGHT expresion_op PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = continueRight(p[2],line)
    
    pass

def p_continueLeft(p):
    """movimiento : CONTINUELEFT expresion_op PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = ContinueLeft(p[2],line)

    pass

def p_pos(p):
    """movimiento : POS PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = Pos(p[3],p[5],line)
    
    pass

def p_posX(p):
    """movimiento: POSX expresion_op PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = PosX(p[2],line)

    pass

def p_posY(p):
    """movimiento: POSY expresion_op PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = PosY(p[2],line)

    pass

def p_useColor(p):
    """movimiento : USECOLOR expresion_op PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = UseColor(p[2],line)

    pass

def p_useColor_noAsig(p):
    """movimiento : USECOLOR PUNTOCOMA"""
    
    line = p.lineno(1)
    p[0] = UseColor(1,line)

    pass

def p_up(p):
    """movimiento: UP PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = Up(p[1], line)
    pass

def p_down(p):
    """movimiento: DOWN PUNTOCOMA"""
    
    line = p.lineno(1)
    p[0] = Down(p[1], line)
    pass

def p_beginning(p):
    """movimiento : BEGINNING PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = Beginnig(p[1], line) 
    pass

# =================================== ESTRUCTURA DE INSTRUCCIONES DE CICLOS ===================================
#SEMÁNTICO ---> 'ciclos.py'

def p_while(p):
    """while : WHILE PARENTESISC_IZQ condicionales PARENTESISC_DER PARENTESISC_IZQ expresion PARENTESISC_DER WHEND PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = While(p[3],p[6],line)

    pass

def p_while2(p):
    """while : WHILE PARENTESISC_IZQ logicas PARENTESISC_DER PARENTESISC_IZQ expresion PARENTESISC_DER WHEND PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = While(p[3],p[6],line)
    pass

def p_for(p):
    """for : FOR id PARENTESIS_IZQ numero TO numero PARENTESIS_DER LOOP PARENTESISC_IZQ expresion PARENTESISC_DER END LOOP PUNTOCOMA"""
    
    line = p.lineno(1)
    p[0] = For(p[2],p[4],p[6],p[10],line)
    
    pass

def p_repeat(p):
    """repeat : REPEAT PARENTESISC_IZQ expresion PARENTESISC_DER UNTIL PARENTESISC_IZQ condicionales PARENTESISC_DER PUNTOCOMA"""
    
    line = p.lineno(1)
    p[0] = Repeat(p[3],p[7],line)

    pass

def p_repeat2(p):
    """repeat : REPEAT PARENTESISC_IZQ expresion PARENTESISC_DER UNTIL PARENTESISC_IZQ logicas PARENTESISC_DER PUNTOCOMA"""

    line = p.lineno(1)
    p[0] = Repeat(p[3],p[7],line)

    pass

def p_case(p):
    """case : CASE id bloq_when END CASE PUNTOCOMA
            | CASE id bloq_when else END CASE PUNTOCOMA"""
    
    line = p.lineno(1)
    if len(p) == 7:
        p[0] = Case(p[2],p[3],None,line)

    else:
        p[0] = Case(p[2],p[3],p[4],line) # con bloque else


def p_bloque_when(p):
    """bloq_when : when bloq_when
                    | when"""
    
    # Caso de la primera regla
    if len(p) == 3:
        # se concatena el la condicion when actual con las siguientes
        lista_when = [p[1]] + p[2].lista_when
        p[0] = Bloque_when(lista_when)

    # Caso de la segunda regla
    else:
        # Solo una condicion when
        p[0] = Bloque_when([p[1]])

    pass


def p_when(p):
    """when : WHEN numero THEN PARENTESISC_IZQ expresion PARENTESISC_DER
            | WHEN bool THEN PARENTESISC_IZQ expresion PARENTESISC_DER"""

    line = p.lineno(1)
    p[0] = When(p[2],p[5],line)

    pass

def p_else(p):
    """else : ELSE PARENTESISC_IZQ expresion PARENTESISC_DER"""

    line = p.lineno(1)
    p[0] = Else(p[3],line)
    
    pass


# =================================== ESTRUCTURA DE ATÓMICOS ===================================

def p_numero(p):
    """numero: NUMERO"""
    p[0] = p[1]  # Nodo para el tipo de dato numero
    pass

def p_bool(p):
    """bool: BOOL"""
    p[0] = p[1]  # Nodo para el tipo de dato booleano
    pass

def p_id(p):
    """id: ID"""
    p[0] = p[1]  # Nodo para el Id
    pass


# ESTRUCTURA CADENA VACIA

def p_empty(p):
    """empty :"""
    p[0] = None
    pass


# =================================== MANEJO DE ERRORES SINTACTICOS ===================================
def p_error(p):
    global errores_sintacticos
    if p:
        error_msg = f"En línea: {p.lineno} --> Error sintáctico en el token {p.value}"
    else:
        error_msg = "Error de sintaxis: EOF no válido. Falta un token al final de un procedimiento"
    
    errores_sintacticos.append(error_msg) 


# PARSER (Analizador Sintáctico)
def analizador_sintactico(cadena):
    global errores_sintacticos
    errores_sintacticos = [] 
    parser = yacc.yacc()
    parser.parse(cadena)
    return errores_sintacticos


# PRUEBAS
# ========================================================================
'''
def leer_y_parsear_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            cadena = archivo.read()  # Leer todo el contenido del archivo
        result = parser.parse(cadena)  # Parsear el contenido del archivo
        return result
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'.")

# Crear el parser
parser = yacc.yacc()

# Nombre del archivo de texto que contiene el código a parsear
nombre_archivo = "codigo.txt"

# Llamar a la función para leer el archivo y parsearlo
resultado = leer_y_parsear_archivo(nombre_archivo)
print(resultado)
'''
# ========================================================================