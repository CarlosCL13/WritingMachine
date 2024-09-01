import ply.lex as lex

# Definicion de Tokens

tokens = [
    'COMA', 'PUNTOCOMA', 'DOSPUNTOS', 'ASIGNACION', 
    'PARENTESIS_IZQ', 'PARENTESIS_DER', 'PARENTESISC_IZQ', 'PARENTESISC_DER',
    'ID', 'NUMERO', 'DIFERENTE',
    'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL',
    'SUMA',  'RESTA', 'MULTIPLICA', 'DIVIDE', 'POTENCIA'    
]

# Definicion de palabras reservadas
                
reservadas = {
    'Def':'DEF', 'Put':'PUT' , 'Start':'START', 
    'Add':'ADD', 'If':'IF', 'while':'WHILE',
    'IfElse':'IFELSE', 'EndIf':'ENDIF', 'Repeat':'REPEAT', 
    'Until':'UNTIL', 'And':'AND','Or':'OR', 
    'Print':'PRINT', 'End':'END', 'Random':'RANDOM',
    'PosX':'POSX', 'PosY':'POSY','Pos':'POS',
    'Equal':'EQUAL', 'Greater':'GREATER', 'Smaller':'SMALLER',
    'Substr':'SUBSTR', 'Mult':'MULT', 'Div':'DIV',
    'Sum':'SUM', 'Else':'ELSE', 'For':'FOR', 
    'Loop':'LOOP', 'Case':'CASE', 'When':'WHEN', 
    'Then':'THEN', 'Whend':'WHEND'
}


# Definicion de movimientos del hardware
                                                                                
movimientos = {'ContinueUp':'CONTINUEUP', 'ContinueDown':'CONTINUEDOWN', 
               'ContinueLeft':'CONTINUELEFT', 'ContinueRight':'CONTINUERIGHT', 
               'UseColor':'USECOLOR', 'Down':'DOWN','Up':'UP',
               'Beginning':'BEGINNING'
}

reservadas.update(movimientos)

tokens = list(reservadas.values()) + tokens

t_ignore = '  \t'

# Asignacion de caracteres

t_COMA = r','
t_PUNTOCOMA = r';'
t_DOSPUNTOS = r':'
t_ASIGNACION = r'='
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_PARENTESISC_IZQ = r'\['
t_PARENTESISC_DER = r'\]'
t_DIFERENTE = r'!='
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICA = r'\*'
t_DIVIDE = r'\/'
t_POTENCIA = r'\^'

# Funciones

def t_START(t):
    r'\--.*'
    t.value = "START"
    t.type = t.value
    return t


def t_FIN(t):
    r'Fin'
    t.value = "FIN"
    t.type = t.value
    return t



def t_ENDIF(t):
    r'EndIf'
    t.value = "ENDIF"
    t.type = t.value
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_#&@]*'
    if t.value.upper() in reservadas.values():
        t.value = t.value.upper()
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
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


def t_COMMENT(t):
    r'\//.*'
    pass
    # No return value. Token discarded

#Construcción del analizador léxico
lexer = lex.lex()

#Ejemplo de uso
data = "Add (4,5) While (3>1) abc = 2 Random()"

lexer.input(data)

#Obtener los tokens reconocidos
while True:
    token = lexer.token()
    if not token:
        break
    print(token)