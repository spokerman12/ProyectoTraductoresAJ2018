# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required

reserved = {
	'if' : 'TkIf',
	'then': 'TkThen',
	'fi' : 'TkFi',
	'while' : 'TkWhile',
	'begin' : 'TkBegin',
	'var' : 'TkVar',
	'with' : 'TkWith',
	'do': 'TkDo',
	'od' : 'TkOd',
	'bool' : 'TkBool',
	'for' : 'TkFor',
	'end' : 'TkEnd',
	'True' : 'TkTrue',
	'False' : 'TkFalse',
	'int' : 'TkInt'
}

tokens = [
   'TkNum',
   'TkCaracter',
   'TkId',
   'TkComa',
   'TkPunto',
   'TkDosPuntos',
   'TkParAbre',
   'TkParCierra',
   'TkCorcheteAbre',
   'TkCorcheteCierra',
   'TkLlaveAbre',
   'TkLlaveCierra',
   'TkHacer',
   'TkAsignacion',
   'TkSuma',
   'TkResta',
   'TkMult',
   'TkDiv',
   'TkMod',
   'TkConjuncion',
   'TkDisyuncion',
   'TkNegacion',
   'TkMenor',
   'TkMenorIgual',
   'TkMayor',
   'TkMayorIgual',
   'TkIgual',
   'TkSiguienteCar',
   'TkAnteriorCar',
   'TkValorAscii',
   'TkConcatenacion',
   'TkShift',
   #'TkTrue',
   #'TkFalse'
] + list(reserved.values())


# Regular expression rules for simple tokens
t_TkComa				= r','
t_TkPunto 				= r'\.'
t_TkDosPuntos 			= r':'
t_TkParAbre 			= r'\('
t_TkParCierra			= r'\)'
t_TkCorcheteAbre		= r'\['
t_TkCorcheteCierra		= r'\]'
t_TkLlaveAbre			= r'\{'
t_TkLlaveCierra			= r'\}'
t_TkHacer				= r'->'
t_TkAsignacion			= r'<-'
t_TkSuma				= r'\+'
t_TkResta				= r'\-'
t_TkMult				= r'\*'
t_TkDiv					= r'\/'
t_TkMod					= r'\%'
t_TkConjuncion			= r'\/\\'
t_TkDisyuncion			= r'\\\/'
t_TkNegacion			= r'not'
t_TkMenor				= r'<'
t_TkMenorIgual			= r'<='
t_TkMayor				= r'>'
t_TkMayorIgual			= r'>='
t_TkIgual 				= r'='
t_TkSiguienteCar		= r'\+\+'
t_TkAnteriorCar			= r'--'
t_TkValorAscii			= r'\#'
t_TkConcatenacion		= r'::'
t_TkShift				= r'\$'

# A regular expression rule with some action code
def t_TkNum(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_TkCaracter(t):
	r'\'[a-zA-Z_][a-zA-Z_0-9]*\''
	#t.value = str(t.value)
	return t

# Define a rule so we can track line numbers
def t_Tknewline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_TkId(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'TkId')    # Check for reserved words
    return t

#def t_TkTrue(t):
#	r'True'
#	t.type = reserved.get(t.value,'True')    # Check for reserved words
#	return t

#def t_TkFalse(t):
#	r'False'
#	t.type = reserved.get(t.value,'False')    # Check for reserved words
#	return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Error: Caracter inesperado "+str(t.value[0])+" en la fila "+str(t.lexer.lineno)+" y columna "+str(t.lexer.lexpos)+"\n")
    t.lexer.skip(1)

def t_error2(t):
	r'[0-9][a-zA-Z_0-9]*'
	print ("ERROR")
	t.lexer.skip(1)

# Build the lexer
lexer = lex.lex() 