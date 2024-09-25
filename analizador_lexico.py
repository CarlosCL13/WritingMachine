import ply.lex as lex

# Definicion de Tokens

tokens = [
    'COMA', 'PUNTOCOMA', 'PARENTESIS_IZQ', 'PARENTESIS_DER', 
    'PARENTESISC_IZQ', 'PARENTESISC_DER', 'ID', 'NUMERO', 'BOOL'    
]

# Definicion de palabras reservadas
                
reservadas = {
    'Def':'DEF', 'Put':'PUT' , 'Proc':'PROC', 'Main':'MAIN',
    'Add':'ADD','while':'WHILE','Repeat':'REPEAT',
    'Until':'UNTIL', 'And':'AND','Or':'OR',
    'End':'END', 'Random':'RANDOM','PosX':'POSX',
    'PosY':'POSY','Pos':'POS','Equal':'EQUAL', 'Greater':'GREATER',
    'Smaller':'SMALLER','Substr':'SUBSTR', 'Mult':'MULT', 'Div':'DIV',
    'Sum':'SUM', 'Else':'ELSE', 'For':'FOR', 'Loop':'LOOP',
    'Case':'CASE', 'When':'WHEN', 'Then':'THEN', 'Whend':'WHEND', 'To':'TO'
}


# Definicion de movimientos del hardware
                                                                                
movimientos = {'ContinueUp':'CONTINUEUP', 'ContinueDown':'CONTINUEDOWN', 
                'ContinueLeft':'CONTINUELEFT', 'ContinueRight':'CONTINUERIGHT', 
                'UseColor':'USECOLOR', 'Down':'DOWN','Up':'UP',
                'Beginning':'BEGINNING'
}

reservadas.update(movimientos)

tokens = list(reservadas.values()) + tokens

t_ignore = ' \t'

# Asignacion de caracteres

t_COMA = r','
t_PUNTOCOMA = r';'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_PARENTESISC_IZQ = r'\['
t_PARENTESISC_DER = r'\]'

# Funciones

def t_BOOL(t):
    r'TRUE|FALSE'
    try:
        t.value = t.value
        """  if t.value == "TRUE":
            t.value = t.value
        else:
            t.value = t.value """
    except ValueError:
        print("No es tipo booleano")
    return t


def t_ID(t):
    r'CONTINUELEFT|CONTINUERIGHT|CONTINUEDOWN|TO|OR|UP|[a-zA-Z_][a-zA-Z0-9_@]*'

    if t.value in reservadas.values():
        t.value = t.value
        t.type = t.value 

    else:

        if (t.value[0]>="A" and t.value[0]<="Z"):
                print(f"Error: La variable '{t.value}' no inicia con minuscula.")
                t_error(t)
                return None

        elif (3 <= len(t.value) <= 10):
            t.value = t.value
        
        else:
            
            print(f"Error: The token '{t.value}' is of invalid length ({len(t.value)} characters).")
            t_error(t) 
            return None 
    
    return t


def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("Expresion regular invalida '%s'" % t.value[0])
    t.lexer.skip(1)


def t_COMMENT(t):
    r'\//.*'
    pass
    # No return value. Token discarded

def analizador_lexico(cadena):
    lexer = lex.lex()
    lexer.input(cadena)
    prints = []  # Lista para tokens y errores
    while True:
        tokens = lexer.token()
        if not tokens:
            break
        print(tokens)
        prints.append(tokens)  # Añadir token o error a la lista
    return prints


'''lexer = lex.lex()

cadena = "PROC ADD (4,5) WHILE (GREATER(3,1)) DEF(var1,TRUE) RANDOM() END;"

lexer.input(cadena)

while True:
    tokens = lexer.token()
    if not tokens:
        break
    print(tokens)'''