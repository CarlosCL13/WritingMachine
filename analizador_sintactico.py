import ply.yacc as yacc
from analizador_lexico import tokens

precedence = (
	('right','PROC'),
	)

# Ejemplo que no sabemos como funca: DEF(rata, MULT(MULT(9,1), MULT(8,9)))

def p_programa(p):
        """programa : proc_compuesto"""
        #p[0] = programa(p[1])
        pass

def p_proc_compuesto(p):
    """proc_compuesto : set_proc"""
    #p[0] = p[1]
    pass

def p_set_proc(p):
    """set_proc : procedimiento set_proc
                | procedimiento"""
    #try:
        #p[0] = [p[1]] + p[2]
    #except IndexError:
        #p[0] = [p[1]]
    pass

def p_procedimiento(p):
    """procedimiento : funcion"""
    #p[0] = p[1]
    pass


def p_bloq_ejecucion(p):
    """bloq_ejecucion : while"""
    pass


def p_expresion(p):
    """expresion : def_variable expresion
                    | put expresion
                    | llamada_funcion expresion
                    | aritmeticas expresion
                    | logicas expresion
                    | movimiento expresion
                    | condicionales expresion
                    | empty"""
    #p[0] = p[1]
    pass


def p_expresion_var(p):
    """expresion_var : ID
                    | NUMERO
                    | BOOL
                    | empty"""
    #p[0] = p[1]
    pass

def p_expresion_param(p):
    """expresion_param : ID
                    | NUMERO
                    | BOOL
                    | aritmeticas
                    | logicas
                    | empty"""
    #p[0] = p[1]
    pass

def p_expresion_op(p):
    """expresion_op : ID
                    | NUMERO
                    | aritmeticas
                    | empty"""
    #p[0] = p[1]
    pass

def p_expresion_log(p):
    """expresion_log : ID
                    | NUMERO
                    | condicionales
                    | empty"""
    #p[0] = p[1]
    pass

def expresion_cond(p):
    """expresion_cond: """

def p_def_variable(p):
    """def_variable : DEF PARENTESIS_IZQ ID COMA expresion_var PARENTESIS_DER PUNTOCOMA"""
    #p[0] = VariableDef(p[2], p[4])
    pass

def p_llamada_funcion(p):
    """llamada_funcion : ID PARENTESIS_IZQ parametros PARENTESIS_DER PUNTOCOMA"""
    #p[0] = FunctionCall(p[1], p[3])
    pass

def p_parametros(p):
    """parametros : expresion_param COMA parametros
                    | expresion_param"""
    #try:
        #p[0] = [p[1]] + p[3]
    #except IndexError:
        #p[0] = [p[1]]
    pass

def p_funcion(p):
    """funcion : PROC ID PARENTESIS_IZQ parametros PARENTESIS_DER PARENTESISC_IZQ expresion PARENTESISC_DER PUNTOCOMA END PUNTOCOMA"""
    #p[0] = Function(p[2], p[4], p[6])
    pass

def p_aritmeticas(p):
    """aritmeticas : ADD PARENTESIS_IZQ ID COMA expresion_op PARENTESIS_DER PUNTOCOMA
                    | ADD PARENTESIS_IZQ ID PARENTESIS_DER PUNTOCOMA
                    | DIV PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER PUNTOCOMA
                    | MULT PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER PUNTOCOMA
                    | SUM PARENTESIS_IZQ expresion_op COMA expresion PARENTESIS_DER PUNTOCOMA
                    | SUBSTR PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER PUNTOCOMA
                    | random """
    # if p[1] == "Multiply":
    #     p[0] = Multiply(p[3], p[5])
    # elif p[1] == "Divide":
    #     p[0] = Divide(p[3], p[5])
    # elif p[1] == "Power":
    #     p[0] = Power(p[3], p[5])
    # elif p[1] == "Addition":
    #     p[0] = Addition(p[3], p[5])
    # elif p[1] == "Subtract":
    #     p[0] = Subtract(p[3], p[5])
    pass

def p_logicas(p):
    """logicas : AND PARENTESIS_IZQ expresion_log COMA expresion_log PARENTESIS_DER PUNTOCOMA
                | OR PARENTESIS_IZQ expresion_log COMA expresion_log PARENTESIS_DER PUNTOCOMA"""
    # if p[1] == "And":
    #     p[0] = And(p[3], p[5])
    # elif p[1] == "Or":
    #     p[0] = Or(p[3], p[5])
    pass

def p_condicionales(p):
    """condicionales : GREATER PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER PUNTOCOMA
                | SMALLER PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER PUNTOCOMA
                | EQUAL PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER PUNTOCOMA"""
    # if p[1] == "Greater":
    #     p[0] = Greater(p[3], p[5])
    # elif p[1] == "Smaller":
    #     p[0] = Smaller(p[3], p[5])
    # elif p[1] == "Equal":
    #     p[0] = Equal(p[3], p[5])
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
    #p[0] = Continue(p[1], p[2])
    pass

def p_continueDown( p):
    """continueDown : CONTINUEDOWN expresion_op PUNTOCOMA"""
    #p[0] = Continue(p[1], p[2])
    pass

def p_continueRight( p):
    """continueRight : CONTINUERIGHT expresion_op PUNTOCOMA"""
    #p[0] = Continue(p[1], p[2])
    pass

def p_continueLeft( p):
    """continueLeft : CONTINUELEFT expresion_op PUNTOCOMA"""
    #p[0] = Continue(p[1], p[2])
    pass

def p_pos( p):
    """pos : POS PARENTESIS_IZQ expresion_op COMA expresion_op PARENTESIS_DER PUNTOCOMA"""
    #p[0] = Pos(p[3], p[5])
    pass

def p_posAxis( p):
    """posAxis : POSX expresion_op PUNTOCOMA
            | POSY expresion_op PUNTOCOMA"""
    #p[0] = PosAxis(p[1], p[2])
    pass

def p_useColor( p):
    """useColor : USECOLOR expresion_op PUNTOCOMA"""
    #p[0] = UseColor(p[2])
    pass

def p_elevation( p):
    """elevation : UP PUNTOCOMA
                    | DOWN PUNTOCOMA"""
    #p[0] = Elevation(p[1])
    pass

def p_beginning( p):
    """beginning : BEGINNING PUNTOCOMA"""
    #p[0] = Begin()
    pass

def p_put(p):
    """put : PUT PARENTESIS_IZQ ID COMA expresion_param PARENTESIS_DER PUNTOCOMA"""
    #p[0] = Put(p[2], p[4])
    pass

def p_random(p):
    """random : RANDOM PARENTESIS_IZQ expresion_op PARENTESIS_DER PUNTOCOMA"""
    #"p[0] = Random(p[3])
    pass


# Intrucciones de ciclos o bloques de instrucciones

def p_while(p):
    """while : WHILE PARENTESISC_IZQ condicionales PARENTESISC_DER PARENTESISC_IZQ expresion PARENTESISC_DER WHEND PUNTOCOMA"""
    #p[0] = While(p[3], p[6])
    pass

def p_for(p):
    """for : FOR ID PARENTESIS_IZQ NUMERO to NUMERO PARENTESIS_DER LOOP PARENTESISC_IZQ expresion PARENTESISC_DER END LOOP PUNTOCOMA"""
    #p[0] = While(p[3], p[6])
    pass

def p_repeat(p):
    """repeat : REPEAT PARENTESISC_IZQ expresion PARENTESISC_DER UNTIL PARENTESISC_IZQ condicionales PARENTESISC_DER"""
    #p[0] = Repeat(p[2], p[4])
    pass

def p_case(p):
    """case : CASE ID when END CASE PUNTOCOMA
            | CASE ID when else END CASE PUNTOCOMA"""

def p_when(p):
    """when : WHEN NUMERO THEN PARENTESISC_IZQ expresion PARENTESISC_DER 
            | WHEN BOOL THEN PARENTESISC_IZQ expresion PARENTESISC_DER"""
    #p[0] = If(p[2], p[4])
    pass

def p_else(p):
    """else : ELSE PARENTESISC_IZQ expresion PARENTESISC_DER"""
    #p[0] = Else(p[2], p[4], p[7])
    pass

def p_empty(p):
    """empty :"""
    pass

def p_error( p):
    if p:
        print(f'Syntax error in line {p.lineno} in {p.value} token')
    else:
        print("Syntax error: Invalid EOF\nMissing token at the end of a procedure")

parser = yacc.yacc()
cadena = "PROC linea1() \n [Def(varLocal1, 1); \n POSY varLocal1;]; \n END;"
result = parser.parse(cadena)