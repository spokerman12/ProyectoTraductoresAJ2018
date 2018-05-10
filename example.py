from lexer2 import *

# Test it out
data = '''¡
3 4 * 10 + ++ if True ! False
   -20 *2 "dasd" var kak::
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:

    linea = 1

    tok = lexer.token()

    if not tok: 
        break      # No more input
    if (tok.lineno != linea):
        salida = tok.type+" "+str(tok.value)+" "+str(tok.lineno)+" "+str(tok.lexpos)
        linea = tok.lineno
        print (str(linea)+salida, end = " ")
