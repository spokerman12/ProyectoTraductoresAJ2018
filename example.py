from lexer2 import *

# Test it out
data = ''' with
  var contador : int

begin
  contador <- 35hola .

end'''

filename = "prueba.txt"
file = open(filename,"r")

# Give the lexer some input
lexer.input(data)

# Tokenize
linea = 0
#while True:

for line in file:
    lexer.input(line)
    
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input

        if (tok.type == "TkId"):
            salida = tok.type+"('"+tok.value+"')"+" "+str(tok.lineno)+" "+str(tok.lexpos)

        elif (tok.type == "TkNum"):
            salida = tok.type+"("+str(tok.value)+")"+" "+str(tok.lineno)+" "+str(tok.lexpos)

        else:
            salida = tok.type+" "+str(tok.lineno)+" "+str(tok.lexpos)

        if (linea != tok.lineno):
            linea = tok.lineno
            print (" ")

        print (salida, end = ", ")
