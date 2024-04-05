import ply.lex as lex
import ply.yacc as yacc
flag = 0
reserved = {'while':'WHILE', 'and':'AND', 'or':'OR', 'not':'NOT', 'True':
'TRUE', 'for':'FOR', 'in':'IN', 'range':'RANGE',
'if':'IF', 'elif':'ELIF', 'else':'ELSE','statements': 'STAT', 'def':
'DEF'}
tokens = ['LPAREN', 'RPAREN', 'GT', 'LT', 'GTE', 'LTE','ID',
'COM', 'NEQUALS', 'DEQUALS', 'COLON',
'SPACE', 'EQUALS','NUMBER'] + list(reserved.values())
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
t_NUMBER = r'-?\d+(\.\d+)?'
t_COM = r','
t_ignore = r'\t'
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t
def t_error(t):
    print("Invalid character '%s'" %t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()
data = '''if i==5: statements elif i==3: tatements else:statements'''
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
def p_command(p):
    '''
    start : IF SPACE condition COLON start
            | IF SPACE condition COLON STAT SPACE body
            | IF SPACE condition COLON start SPACE body
            | IF SPACE condition COLON STAT
    '''
    p[0] = 1
def p_condition(p):
    '''
    condition : condition SPACE AND SPACE condition
             | condition SPACE OR SPACE condition
             | LPAREN condition RPAREN
             | TRUE
             | NOT LPAREN condition RPAREN
    '''
    p[0] = 1
def p_exp(p):
    '''
    exp : NUMBER
        | ID
    '''
    p[0] = 1
def p_cond_logic(p):
    '''
    condition : exp LT exp
             | exp LTE exp
             | exp DEQUALS exp
             | exp NEQUALS exp
             | exp GT exp
             | exp GTE exp
    '''
    p[0] = 1
def p_body(p):
    '''
    body : ELIF SPACE condition COLON start
        | ELIF SPACE condition COLON STAT SPACE body
        | ELIF SPACE condition COLON start SPACE body
        | ELSE COLON start
        | ELSE COLON STAT
    '''
    p[0] = 1
def p_error(p):
    print("Syntax error")
    global flag
    flag = 1
parser = yacc.yacc()
while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    result = parser.parse(s)
    if flag == 0:
        print("Valid syntax")
    print()
    flag = 0
