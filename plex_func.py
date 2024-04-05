import ply.lex as lex
import ply.yacc as yacc
c = 0
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
data = '''def fun(a,b):'''
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break # No more input
    print(tok)
def p_start(p):
    '''
    start : def_statement
          | STAT SPACE start
          | STAT
    '''
    p[0] = 1

def p_def_statement(p):
    '''
    def_statement : DEF SPACE ID LPAREN RPAREN COLON STAT SPACE start
                  | DEF SPACE ID LPAREN RPAREN COLON start
                  | DEF SPACE ID LPAREN arg RPAREN COLON STAT SPACE start
                  | DEF SPACE ID LPAREN arg RPAREN COLON start
    '''
    p[0] = 1

def p_arg(p):
    '''
    arg : non_keyworded COM keyworded
        | keyworded
        | non_keyworded
        | ASTERISK ASTERISK ID
        | ASTERISK ID
        | non_keyworded COM non_keyworded
    '''
    p[0] = 1
def p_keyworded(p):
    '''
    keyworded : keyworded COM keyworded

    | ID EQUALS INT
    | ID EQUALS FLOAT

    '''
    p[0] = 1
def p_non_keyworded(p):
    '''
    non_keyworded : ID COM non_keyworded
    | ID

    '''
    p[0] = 1
def p_error(p):
    print("Syntax error")
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
        print("Valid syntax")
    print()
    c = 0