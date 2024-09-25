import ply.yacc as yacc
from analizador_lexico import tokens

precedence = (
	('right','PROC'),
    ('left','MAIN'),
	)

def p_programa(p):
        """programa : proc_compuesto"""
        pass

def p_proc_compuesto(p):
    """proc_compuesto : set_proc inicio set_proc
                    | set_proc inicio
                    | inicio set_proc
                    | inicio"""
    pass

def p_inicio(p):
    """inicio : MAIN PARENTESIS_IZQ PARENTESIS_DER PARENTESISC_IZQ expresion PARENTESISC_DER PUNTOCOMA END PUNTOCOMA"""
    pass

def p_set_proc(p):
    """set_proc : funcion set_proc
                | funcion"""
    pass

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
    pass


def p_expresion_var(p):
    """expresion_var : ID
                    | NUMERO
                    | BOOL
                    | empty"""
    pass

def p_expresion_param(p):
    """expresion_param : ID
                    | NUMERO
                    | BOOL
                    | aritmeticas_return
                    | logicas
                    | empty"""
    pass

def p_expresion_op(p):
    """expresion_op : ID
                    | NUMERO
                    | aritmeticas_return
                    | empty"""
    pass

def p_expresion_log(p):
    """expresion_log : ID
                    | condicionales
                    | empty"""
    pass

def expresion_cond(p):
    """expresion_cond: """

def p_def_variable(p):
    """def_variable : DEF PARENTESIS_IZQ ID COMA expresion_var PARENTESIS_DER PUNTOCOMA"""
    pass

def p_llamada_funcion(p):
    """llamada_funcion : ID PARENTESIS_IZQ parametros PARENTESIS_DER PUNTOCOMA"""
    pass

def p_parametros(p):
    """parametros : expresion_param COMA parametros
                    | expresion_param"""


def p_funcion(p):
    """funcion : PROC ID PARENTESIS_IZQ parametros PARENTESIS_DER PARENTESISC_IZQ expresion PARENTESISC_DER PUNTOCOMA END PUNTOCOMA"""
    pass

#| ADD PARENTESIS_IZQ ID PARENTESIS_DER PUNTOCOMA
def p_aritmeticas1(p):
    """aritmeticas_return : DIV PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER
                    | MULT PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER
                    | SUM PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER
                    | SUBSTR PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER
                    | random """
    pass

def p_aritmeticas2(p):
    """aritmeticas_No_return : ADD PARENTESIS_IZQ ID PARENTESIS_DER PUNTOCOMA
                    | ADD PARENTESIS_IZQ ID COMA expresion_op PARENTESIS_DER PUNTOCOMA"""
    pass



def p_logicas(p):
    """logicas : AND PARENTESIS_IZQ expresion_log COMA expresion_log PARENTESIS_DER
                | OR PARENTESIS_IZQ expresion_log COMA expresion_log PARENTESIS_DER"""
    pass

def p_condicionales(p):
    """condicionales : GREATER PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER
                | SMALLER PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER
                | EQUAL PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER"""

    pass

def p_movimiento(p):
    """movimiento : continueUp 
        | continueDown
        | continueRight
        | continueLeft
        | pos
        | posAxis
        | useColor
        | elevation
        | beginning"""
    pass

def p_continueUp(p):
    """continueUp : CONTINUEUP expresion_op PUNTOCOMA"""
    pass

def p_continueDown( p):
    """continueDown : CONTINUEDOWN expresion_op PUNTOCOMA"""
    pass

def p_continueRight( p):
    """continueRight : CONTINUERIGHT expresion_op PUNTOCOMA"""
    pass

def p_continueLeft( p):
    """continueLeft : CONTINUELEFT expresion_op PUNTOCOMA"""
    pass

def p_pos( p):
    """pos : POS PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER PUNTOCOMA"""
    pass

def p_posAxis(p):
    """posAxis : POSX expresion_op PUNTOCOMA
            | POSY expresion_op PUNTOCOMA"""
    pass

def p_useColor(p):
    """useColor : USECOLOR expresion_op PUNTOCOMA"""
    pass

def p_elevation(p):
    """elevation : UP PUNTOCOMA
                    | DOWN PUNTOCOMA"""
    pass

def p_beginning(p):
    """beginning : BEGINNING PUNTOCOMA"""
    pass

def p_put(p):
    """put : PUT PARENTESIS_IZQ ID COMA expresion_param PARENTESIS_DER PUNTOCOMA"""
    pass

def p_random(p):
    """random : RANDOM PARENTESIS_IZQ expresion_op PARENTESIS_DER"""
    pass


# Intrucciones de ciclos o bloques de instrucciones

def p_while(p):
    """while : WHILE PARENTESISC_IZQ condicionales PARENTESISC_DER PARENTESISC_IZQ expresion PARENTESISC_DER WHEND PUNTOCOMA
            | WHILE PARENTESISC_IZQ logicas PARENTESISC_DER PARENTESISC_IZQ expresion PARENTESISC_DER WHEND PUNTOCOMA"""
    pass

def p_for(p):
    """for : FOR ID PARENTESIS_IZQ NUMERO TO NUMERO PARENTESIS_DER LOOP PARENTESISC_IZQ expresion PARENTESISC_DER END LOOP PUNTOCOMA"""
    pass

def p_repeat(p):
    """repeat : REPEAT PARENTESISC_IZQ expresion PARENTESISC_DER UNTIL PARENTESISC_IZQ condicionales PARENTESISC_DER PUNTOCOMA
            | REPEAT PARENTESISC_IZQ expresion PARENTESISC_DER UNTIL PARENTESISC_IZQ logicas PARENTESISC_DER PUNTOCOMA"""
    pass

def p_case(p):
    """case : CASE ID when END CASE PUNTOCOMA
            | CASE ID when else END CASE PUNTOCOMA"""

def p_when(p):
    """when : WHEN NUMERO THEN PARENTESISC_IZQ expresion PARENTESISC_DER 
            | WHEN BOOL THEN PARENTESISC_IZQ expresion PARENTESISC_DER"""
    pass

def p_else(p):
    """else : ELSE PARENTESISC_IZQ expresion PARENTESISC_DER"""
    
    pass

def p_empty(p):
    """empty :"""
    pass

def p_error( p):
    if p:
        print(f'Syntax error in line {p.lineno} in {p.value} token')
    else:
        print("Syntax error: Invalid EOF\nMissing token at the end of a procedure")


def analizador_sintactico(cadena):
    parser = yacc.yacc()
    parser.parse(cadena)


# Función para leer el contenido de un archivo de texto y parsearlo
'''def leer_y_parsear_archivo(nombre_archivo):
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
resultado = leer_y_parsear_archivo(nombre_archivo)'''

#print(resultado)