lexer grammar Lexer;

// Tokens
COMA:                ',';
PUNTOCOMA:           ';';
PARENTESIS_IZQ:      '(';
PARENTESIS_DER:      ')';
PARENTESISC_IZQ:     '[';
PARENTESISC_DER:     ']';


// Booleano
Bool:                'TRUE' | 'FALSE';

// Palabras reservadas
Def:                 'DEF';
Put:                 'PUT';
Proc:                'PROC';
Add:                 'ADD';
While:               'WHILE';
Repeat:              'REPEAT';
Until:               'UNTIL';
And:                 'AND';
Or:                  'OR';
End:                 'END';
Random:              'RANDOM';
PosX:                'POSX';
PosY:                'POSY';
Pos:                 'POS';
Equal:               'EQUAL';
Greater:             'GREATER';
Smaller:             'SMALLER';
Substr:              'SUBSTR';
Mult:                'MULT';
Div:                 'DIV';
Sum:                 'SUM';
El:                  'ELSE';
For:                 'FOR';
Loop:                'LOOP';
Case:                'CASE';
When:                'WHEN';
Then:                'THEN';
Whend:               'WHEND';
To:                  'TO';

// Movimientos del hardware
ContinueUp:          'CONTINUEUP';
ContinueDown:        'CONTINUEDOWN';
ContinueLeft:        'CONTINUELEFT';
ContinueRight:       'CONTINUERIGHT';
UseColor:            'USECOLOR';
Down:                'DOWN';
Up:                  'UP';
Beginning:           'BEGINNING';

// Identificadores
NUMERO:              [0-9]+ ;
ID:                  [a-zA-Z_]*[a-zA-Z0-9_#&@]{2,9};

// Comentarios
COMMENT:             '//' ~[\r\n]* -> skip ; // Comentarios de una sola línea

// Ignorar espacios en blanco y tabulaciones
WS: [ \t]+ -> skip ;

// Ignorar nuevas líneas, pero incrementar el número de línea
NEWLINE: [\r\n]+ -> skip ;  

// Token para capturar caracteres no reconocidos
ERROR_CHAR:          . -> channel(HIDDEN);