# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required

reserved = {
	'if' : 'IF',
	'then': 'THEN',
	'fi' : 'FI',
	'while' : 'WHILE',
	'begin' : 'BEGIN',
	'var' : 'VAR',
	'with' : 'WITH',
	'do': 'DO',
	'od' : 'OD',
	'bool' : 'BOOL',
	'for' : 'FOR',
	'end' : 'END',
	'True' : 'TRUE',
	'False' : 'FALSE'
}

tokens = [
   'Numero',
   'Caracter',
   'Id',
   'Coma',
   'Punto',
   'DosPuntos',
   'ParAbre',
   'ParCierra',
   'CorcheteAbre',
   'CorcheteCierra',
   'LlaveAbre',
   'LlaveCierra',
   'Hacer',
   'Asignacion',
   'Suma',
   'Resta',
   'Mult',
   'Div',
   'Mod',
   'Conjuncion',
   'Disyuncion',
   'Negacion',
   'Menor',
   'MenorIgual',
   'Mayor',
   'MayorIgual',
   'Igual',
   'SiguienteCar',
   'AnteriorCar',
   'ValorAscii',
   'Concatenacion',
   'Shift',
   'True',
   'False'
] + list(reserved.values())


# Regular expression rules for simple tokens
t_Coma				= r','
t_Punto 			= r'\.'
t_DosPuntos 		= r':'
t_ParAbre 			= r'\('
t_ParCierra			= r'\)'
t_CorcheteAbre		= r'\['
t_CorcheteCierra	= r'\]'
t_LlaveAbre			= r'\{'
t_LlaveCierra		= r'\}'
t_Hacer				= r'->'
t_Asignacion		= r'<-'
t_Suma				= r'\+'
t_Resta				= r'\-'
t_Mult				= r'\*'
t_Div				= r'\/'
t_Mod				= r'\%'
t_Conjuncion		= r'\/\\'
t_Disyuncion		= r'\/'
t_Negacion			= r'not'
t_Menor				= r'<'
t_MenorIgual		= r'<='
t_Mayor				= r'>'
t_MayorIgual		= r'>='
t_Igual 			= r'='
t_SiguienteCar		= r'\+\+'
t_AnteriorCar		= r'--'
t_ValorAscii		= r'\#'
t_Concatenacion		= r'::'
t_Shift				= r'\$'

# A regular expression rule with some action code
def t_Numero(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_Caracter(t):
	r'"[a-zA-Z_][a-zA-Z_0-9]*"'
	#t.value = str(t.value)
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_Id(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'Id')    # Check for reserved words
    return t

def t_True(t):
	r'True'
	t.type = reserved.get(t.value,'True')    # Check for reserved words
	return t

def t_False(t):
	r'False'
	t.type = reserved.get(t.value,'False')    # Check for reserved words
	return t



# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Error: Caracter inesperado "+str(t.value[0])+" en la fila "+str(t.lexer.lineno)+" y columna "+str(t.lexer.lexpos)+"\n")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()