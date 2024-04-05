import ply.lex as lex
import ply.yacc as yacc
c=0
reserved = {'while':'WHILE', 'and':'AND', 'or':'OR', 'not':'NOT', 'True':
'TRUE', 'for':'FOR', 'in':'IN', 'range':'RANGE',
'if':'IF', 'elif':'ELIF', 'else':'ELSE','statements': 'STAT', 'def':
'DEF'}
tokens = ['LPAREN', 'RPAREN', 'GT', 'LT', 'GTE', 'LTE', 'FLOAT', 'INT', 'ID',
'COM', 'NEQUALS', 'DEQUALS', 'COLON',
'SPACE', 'EQUALS', 'ASTERISK'] + list(reserved.values())
t_GT = r'\>'
t_LT = r'\<'
t_GTE = r'\<\='
t_LTE = r'\>\='
t_DEQUALS = r'\=\='
t_NEQUALS = r'\!\='
t_EQUALS = r'\='
t_COLON = r'\:'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SPACE = r'\ '
t_FLOAT = r'\d+\.\d*'
t_INT = r'\d+'
t_COM = r','
t_ASTERISK = r'\*'
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID') # Check for reserved words
    return t
def t_error(t):
    print("Illegal character inputs!")
    t.lexer.skip(1)
lexer = lex.lex()
data = '''
for i in range(10):
'''
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
def p_loop(p):
    '''
    start : FOR SPACE character SPACE IN SPACE RANGE LPAREN strstpste RPAREN COLON start
        | FOR SPACE character SPACE IN SPACE character COLON start
        | STAT SPACE start
        | STAT
    '''
    p[0] = 1
def p_strstpste(p):
    '''
    strstpste : INT COM INT COM INT
    | INT COM INT
    | INT
    | ID COM ID COM ID
    | ID COM ID
    | ID
    | ID COM INT
    | INT COM ID
    | INT COM ID COM ID
    | ID COM INT COM ID
    | ID COM ID COM INT
    | INT COM INT COM ID
    | INT COM ID COM INT
    | ID COM INT COM INT
    '''
    p[0]=1
def p_character(p):
    'character : ID'
    p[0] = 1
def p_error(p):
    print("Syntax Error!!!")
    global c
    c = 1
parser = yacc.yacc()
while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    result = parser.parse(s)
    if c == 0:
        print("Valid syntax!!")
    print()
    c = 0