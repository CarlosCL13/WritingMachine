import ply.lex as lex

# Definicion de Tokens

tokens = [
    'COMA', 'PUNTOCOMA', 'PARENTESIS_IZQ', 'PARENTESIS_DER', 
    'PARENTESISC_IZQ', 'PARENTESISC_DER', 'ID', 'NUMERO', 'BOOL'    
]

# Definicion de palabras reservadas
                
reservadas = {
    'Def':'DEF', 'Put':'PUT' , 'Proc':'PROC', 
    'Add':'ADD','while':'WHILE','Repeat':'REPEAT', 
    'Until':'UNTIL', 'And':'AND','Or':'OR',
    'End':'END', 'Random':'RANDOM','PosX':'POSX',
    'PosY':'POSY','Pos':'POS','Equal':'EQUAL', 'Greater':'GREATER', 
    'Smaller':'SMALLER','Substr':'SUBSTR', 'Mult':'MULT', 'Div':'DIV',
    'Sum':'SUM', 'Else':'ELSE', 'For':'FOR', 'Loop':'LOOP', 
    'Case':'CASE', 'When':'WHEN', 'Then':'THEN', 'Whend':'WHEND', 'To':'to'
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
    r'[a-zA-Z_][a-zA-Z0-9_#&@]{2,9}|to'
    if t.value in reservadas.values():
        t.value = t.value
        t.type = t.value
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

#Construcción del analizador léxico
lexer = lex.lex()

#Ejemplo de uso
data = "PROC ADD (4,5) WHILE (GREATER(3,1)) DEF(rata,TRUE) RANDOM() END; to"

lexer.input(data)

#Obtener los tokens reconocidos
while True:
    token = lexer.token()
    if not token:
        break
    print(token)