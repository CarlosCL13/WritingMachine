from antlr4 import InputStream, CommonTokenStream
from Lexer import Lexer  # Asegúrate de que `Lexer` es el lexer generado por ANTLR

# Definir una entrada directamente en el código
input_text = "PROC ADD (4,5) WHILE (GREATER(3,1)) DEF(ra,TRUE) RANDOM() END;"

# Crear el InputStream con el texto de entrada
input_stream = InputStream(input_text)

# Crear el lexer
lexer = Lexer(input_stream)

# Crear el token stream
token_stream = CommonTokenStream(lexer)
token_stream.fill()

# Imprimir los tokens reconocidos
for token in token_stream.tokens:
    print(token)
