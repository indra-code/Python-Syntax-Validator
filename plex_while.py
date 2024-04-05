import ply.lex as lex
import ply.yacc as yacc
flag = 0
reserved = {
    'while' : 'WHILE',
    'True' : 'TRUE',
    'False' : 'FALSE',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'statements' : 'STAT'
}
tokens =['LPAREN','RPAREN','COLON','NUMBER','TAB','ID','EQUAL','EXCLAMATION','LT','GT'
,'PLUS','MINUS', 'NEQUALS', 'DEQUALS','DIVIDE','MOD','MULTIPLY', "SPACE"] + list(reserved.values())
t_TAB = r'\t'
t_COLON= r'\:'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DEQUALS = r'\=\='
t_NEQUALS = r'\!\='
t_EQUAL = r'\='
t_EXCLAMATION=r'\!'
t_LT=r'\<'
t_GT=r'\>'
t_PLUS=r'\+'
t_MINUS=r'\-'
t_MOD=r'\%'
t_MULTIPLY=r'\*'
t_DIVIDE=r'\/'
t_SPACE = r'\ '
t_ignore = r'\t'
t_NUMBER = r'\d'
# while a==2: break
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_error(t):
    if(t):
        print(f"\n-> Invalid character`{t.value}`\n-> Error: {t}\n")
    t.lexer.skip(1)
    
lexer = lex.lex()
data = """\
while a>2: break"""
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
    
def p_EQUAL(p):
    "S : WHILE SPACE ID DEQUALS ID COLON TAB STAT"
    p[0] = 1
    print("Inside equal:", p)

def p_EQUAL1(p):
    "S : WHILE SPACE ID DEQUALS NUMBER COLON TAB STAT"
    p[0] = 1

def p_exclamation(p):
    "S : WHILE SPACE ID NEQUALS ID COLON TAB STAT"
    p[0] = 1

def p_exclamation1(p):
    "S : WHILE SPACE ID NEQUALS NUMBER COLON TAB STAT"
    p[0] = 1

def p_lt(p):
    "S : WHILE SPACE ID LT ID COLON TAB STAT"
    p[0] = 1

def p_lt1(p):
    "S : WHILE SPACE ID LT NUMBER COLON TAB STAT"
    p[0] = 1

def p_gt(p):
    "S : WHILE SPACE ID GT ID COLON TAB STAT" 
    p[0] = 1
    
def p_gt1(p):
    "S : WHILE SPACE ID GT NUMBER COLON TAB STAT"
    p[0] = 1

def p_plus(p):
    "S : WHILE SPACE ID PLUS ID EQUAL ID COLON TAB STAT"
    p[0] = 1

def p_plus1(p):
    "S : WHILE NUMBER PLUS NUMBER EQUAL ID COLON TAB STAT"
    p[0] = 1

def p_minus(p):
    "S : WHILE SPACE ID MINUS ID EQUAL ID COLON TAB STAT"
    p[0] = 1

def p_minus1(p):
    "S : WHILE NUMBER MINUS NUMBER EQUAL ID COLON TAB STAT"
    p[0] = 1

def p_mod(p):
    "S : WHILE SPACE ID MOD ID EQUAL ID COLON TAB STAT"
    p[0] = 1

def p_mod1(p):
    "S : WHILE NUMBER MOD NUMBER EQUAL ID COLON TAB STAT"
    p[0] = 1

def p_mul(p):
    "S : WHILE SPACE ID MULTIPLY ID EQUAL ID COLON TAB STAT"
    p[0] = 1

def p_mul1(p):
    "S : WHILE NUMBER MULTIPLY NUMBER EQUAL ID COLON TAB STAT"
    p[0] = 1

def p_div(p):
    "S : WHILE SPACE ID DIVIDE ID EQUAL ID COLON TAB STAT"
    p[0] = 1

def p_div1(p):
    "S : WHILE NUMBER DIVIDE NUMBER EQUAL ID COLON TAB STAT"
    p[0] = 1

def p_error(p):
    print("Syntax error:", p)
    global flag
    flag = 1

parser = yacc.yacc()
while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    
    lexer.input(s)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print("\t",tok)

    result = parser.parse(s)
    print("Result:", result)
    if flag == 0:
        print("Valid Syntax")

    print()
    flag = 0