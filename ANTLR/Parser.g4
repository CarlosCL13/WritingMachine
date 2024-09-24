// Parser.g4
parser grammar Parser;

options {
  tokenVocab=Lexer;
}

programa:              proc_compuesto;

proc_compuesto:        set_proc;

set_proc:              procedimiento set_proc
                      | procedimiento;

procedimiento:        funcion;

funcion:              PROC ID '(' parametros ')' '[' expresion ']' END ';';

parametros:           expresion_param (',' expresion_param)*;

expresion:            def_variable
                    | put
                    | llamada_funcion
                    | aritmeticas
                    | logicas
                    | movimiento
                    | condicionales
                    | for
                    | while
                    | empty;

def_variable:         DEF '(' ID ',' expresion_var ')' ';';

put:                  PUT '(' ID ',' expresion_param ')' ';';

llamada_funcion:      ID '(' parametros ')' ';';

aritmeticas:         ADD '(' ID ',' expresion_op ')' ';'
                    | DIV '(' expresion_op ',' expresion_op ')' ';'
                    | MULT '(' expresion_op ',' expresion_op ')' ';'
                    | SUM '(' expresion_op ',' expresion ')' ';'
                    | SUBSTR '(' expresion_op ',' expresion_op ')' ';'
                    | RANDOM '(' expresion_op ')' ';';

logicas:             AND '(' expresion_log ',' expresion_log ')' ';'
                    | OR '(' expresion_log ',' expresion_log ')' ';';

condicionales:        GREATER '(' expresion_op ',' expresion_op ')' ';'
                    | SMALLER '(' expresion_op ',' expresion_op ')' ';'
                    | EQUAL '(' expresion_op ',' expresion_op ')' ';';

movimiento:           CONTINUEUP expresion_op ';'
                    | CONTINUEDOWN expresion_op ';'
                    | CONTINUERIGHT expresion_op ';'
                    | CONTINUELEFT expresion_op ';'
                    | POS '(' expresion_op ',' expresion_op ')' ';'
                    | POSX expresion_op ';'
                    | POSY expresion_op ';'
                    | USECOLOR expresion_op ';'
                    | UP ';'
                    | DOWN ';'
                    | BEGINNING ';';

for:                  FOR ID '(' NUMERO TO NUMERO ')' LOOP '[' expresion ']' END LOOP ';';

while:                WHILE '[' condicionales ']' '[' expresion ']' WHEND ';';

repeat:               REPEAT '[' expresion ']' UNTIL '[' condicionales ']';

case:                 CASE ID when END CASE ';'
                    | CASE ID when else END CASE ';';

when:                 WHEN NUMERO THEN '[' expresion ']'
                    | WHEN BOOL THEN '[' expresion ']';

else:                 ELSE '[' expresion ']';

empty:                ;

expresion_var:         ID
                    | NUMERO
                    | BOOL
                    | empty;

expresion_param:       ID
                    | NUMERO
                    | BOOL
                    | aritmeticas
                    | logicas
                    | empty;

expresion_op:         ID
                    | NUMERO
                    | aritmeticas
                    | empty;

expresion_log:        ID
                    | NUMERO
                    | condicionales
                    | empty;
