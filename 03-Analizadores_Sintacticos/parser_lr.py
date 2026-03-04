import ply.lex as lex
import ply.yacc as yacc

# LEXER

tokens = (
    'NUM',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'LPAREN',
    'RPAREN',
)

t_ignore = ' \t'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    print(f"Leyendo NUM: {t.value}")
    return t

def t_PLUS(t):
    r'\+'
    print("Leyendo PLUS: +")
    return t

def t_MINUS(t):
    r'-'
    print("Leyendo MINUS: -")
    return t

def t_TIMES(t):
    r'\*'
    print("Leyendo TIMES: *")
    return t

def t_DIV(t):
    r'/'
    print("Leyendo DIV: /")
    return t

def t_LPAREN(t):
    r'\('
    print("Leyendo LPAREN: (")
    return t

def t_RPAREN(t):
    r'\)'
    print("Leyendo RPAREN: )")
    return t

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# PARSER LR (LALR)

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
)

def p_expression_plus(p):
    'E : E PLUS T'
    print("Reduce: E → E + T")

def p_expression_minus(p):
    'E : E MINUS T'
    print("Reduce: E → E - T")

def p_expression_term(p):
    'E : T'
    print("Reduce: E → T")

def p_term_times(p):
    'T : T TIMES F'
    print("Reduce: T → T * F")

def p_term_div(p):
    'T : T DIV F'
    print("Reduce: T → T / F")

def p_term_factor(p):
    'T : F'
    print("Reduce: T → F")

def p_factor_num(p):
    'F : NUM'
    print(f"Reduce: F → num ({p[1]})")

def p_factor_group(p):
    'F : LPAREN E RPAREN'
    print("Reduce: F → (E)")

def p_error(p):
    if p:
        print(f"✘ Error sintáctico en '{p.value}'")
    else:
        print("✘ Error sintáctico al final de la entrada")

parser = yacc.yacc()

# PROGRAMA INTERACTIVO

if __name__ == "__main__":
    print("=== Analizador Sintáctico LR (LALR(1) con PLY) ===")

    while True:
        try:
            expr = input("\nIngrese una expresión aritmética (o Ctrl+C para salir): ")
            if not expr: continue
            
            parser.parse(expr)
            print("✔ Análisis finalizado")

            opcion = input("\n¿Desea analizar otra expresión? (s/n): ").lower()
            if opcion != 's':
                print("Saliendo del analizador LR...")
                break
        except EOFError:
            break