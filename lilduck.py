import ply.lex as lex
import ply.yacc as yacc


tokens = (
    #Literals
    'ID', 'INTEGER', 'FLOAT', 'STRING', 

    #Aritmetic operators
     'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
    'OR', 'AND', 'NOT', 'XOR', 'LSHIFT', 'RSHIFT',
    'LOR', 'LAND', 'LNOT',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

     # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=)
    'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
    'LSHIFTEQUAL','RSHIFTEQUAL', 'ANDEQUAL', 'XOREQUAL', 'OREQUAL',

     # Increment/decrement (++,--)
    'INCREMENT', 'DECREMENT',

     # Delimeters ( ) [ ] { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD', 'SEMI', 'COLON',

    # Ellipsis (...)
    'ELLIPSIS',
)

# Operators
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIVIDE           = r'/'
t_OR               = r'\|'
t_AND              = r'&'
t_NOT              = r'~'
t_XOR              = r'\^'
t_LSHIFT           = r'<<'
t_RSHIFT           = r'>>'
t_LOR              = r'\|\|'
t_LAND             = r'&&'
t_LNOT             = r'!'
t_LT               = r'<'
t_GT               = r'>'
t_LE               = r'<='
t_GE               = r'>='
t_EQ               = r'=='
t_NE               = r'!='

# Assignment operators

t_EQUALS           = r'='
t_TIMESEQUAL       = r'\*='
t_DIVEQUAL         = r'/='
t_MODEQUAL         = r'%='
t_PLUSEQUAL        = r'\+='
t_MINUSEQUAL       = r'-='
t_LSHIFTEQUAL      = r'<<='
t_RSHIFTEQUAL      = r'>>='
t_ANDEQUAL         = r'&='
t_OREQUAL          = r'\|='
t_XOREQUAL         = r'\^='

# Delimeters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
t_PERIOD           = r'\.'
t_SEMI             = r';'
t_COLON            = r':'
t_ELLIPSIS         = r'\.\.\.'

# Identifiers
t_ID = r'[A-Za-z_][A-Za-z0-9_]*'

# Integer literal
t_INTEGER = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# String literal
t_STRING = r'\"([^\\\n]|(\\.))*?\"'


def t_error(t): 
    print("Illegal expresion or illegal character '%s'"% t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_expression(p):
    '''
    expression : exp LT exp
               | exp GT exp
               | exp
    '''

def p_exp(p):
    '''
    exp : termino PLUS termino
        | termino MINUS termino
        | termino
    '''

def p_termino(p):
    '''
    termino : factor TIMES factor
            | factor DIVIDE factor
            | factor
    '''

def p_factor(p):
    '''
    factor : LPAREN expression RPAREN
           | PLUS ID
           | MINUS ID
           | ID
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]
    
def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
         | factor
    '''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]


def p_error(p):
    print("Sytax error!")

parser = yacc.yacc()

with open('lilDuck.txt', 'r') as f:
    s = f.read()

try:
    result = parser.parse(s)
    print('Input string is valid')
except Exception as e:
    print('Input string is not valid:', e)


