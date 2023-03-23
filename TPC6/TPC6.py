import ply.lex as lex

# Lista dos tokens
tokens = [
    'INT',          # Tipo de dados inteiros
    'ID',           # Identificadores (nomes de variáveis, funções, programas e tipos)
    'LPAREN',       # Parêntese esquerdo
    'RPAREN',       # Parêntese direito
    'LBRACE',       # Chave esquerda
    'RBRACE',       # Chave direita
    'COMMA',        # Vírgula
    'PONTOFIN',     # Ponto Final
    'RET',          # Reticencias
    'SEMICOLON',    # Ponto e vírgula
    'ASSIGN',       # Operador de atribuição
    'PLUS',         # Operador de adição
    'MINUS',        # Operador de subtração
    'TIMES',        # Operador de multiplicação
    'DIVIDE',       # Operador de divisão
    'LT',           # Operador "menor que"
    'GT',           # Operador "maior que"
    'EQ',           # Operador de igualdade
    'LE',           # Operador "menor ou igual"
    'GE',           # Operador "maior ou igual"
    'FUNCTION',
    'PROGRAM',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'PRINT',
    'RANGE',
]

# Expressões regulares para os tokens
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_COMMA     = r','
t_SEMICOLON = r';'
t_ASSIGN    = r'='
t_PLUS      = r'\+'
t_MINUS     = r'\-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LT        = r'<'
t_GT        = r'>'
t_EQ        = r'=='
t_LE        = r'<='
t_GE        = r'>='
t_PONTOFIN  = r'\.'
t_RET       = r'\.+'

# Expressão regular para identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    keywords = {'function': 'FUNCTION', 'program': 'PROGRAM', 'if': 'IF',
                'else': 'ELSE', 'while': 'WHILE', 'for': 'FOR', 'print': 'PRINT',
                'range': 'RANGE', 'int': 'INT'}
    t.type = keywords.get(t.value, 'ID')
    return t

# Expressão regular para números inteiros
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Expressão regular para comentários
def t_COMMENT(t):
    r'(\/*([^*]|[\r\n]|(\*+([^*\/]|[\r\n])))*\*+\/)|(\/\/.*)'
    pass

# Ignorar espaços em branco e tabs
t_ignore = ' \t'

# Contador de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Construindo o lexer
lexer = lex.lex()

data ='''
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
'''
data2 = '''
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
'''

lexer.input(data2)

while tok := lexer.token():
        print(tok)