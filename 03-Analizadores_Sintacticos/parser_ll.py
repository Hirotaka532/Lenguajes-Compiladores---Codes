import re

class ParserLL:
    def __init__(self, text):
        self.tokens = self.tokenize(text)
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    # TOKENIZADOR
    def tokenize(self, text):
        token_specification = [
            ('NUM',   r'\d+'),
            ('PLUS',  r'\+'),
            ('MINUS', r'-'),
            ('TIMES', r'\*'),
            ('DIV',   r'/'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('SKIP',  r'[ \t]'),
        ]

        tok_regex = '|'.join(f'(?P<{name}>{pattern})'
                             for name, pattern in token_specification)

        tokens = []
        for mo in re.finditer(tok_regex, text):
            kind = mo.lastgroup
            value = mo.group()
            if kind != 'SKIP':
                tokens.append((kind, value))

        tokens.append(('EOF', None))
        return tokens

    # UTILIDAD
    def match(self, token_type):
        if self.current_token[0] == token_type:
            print(f"Coincide {token_type}: {self.current_token[1]}")
            self.pos += 1
            self.current_token = self.tokens[self.pos]
        else:
            self.error(f"Se esperaba {token_type}")

    def error(self, message):
        raise Exception(f"Error sintáctico: {message}. Token actual: {self.current_token}")

    # GRAMÁTICA LL(1)
    def E(self):
        print("E → T E'")
        self.T()
        self.E_prime()

    def E_prime(self):
        if self.current_token[0] in ('PLUS', 'MINUS'):
            print("E' → + T E'" if self.current_token[0] == 'PLUS'
                  else "E' → - T E'")
            if self.current_token[0] == 'PLUS':
                self.match('PLUS')
            else:
                self.match('MINUS')
            self.T()
            self.E_prime()
        else:
            print("E' → ε")

    def T(self):
        print("T → F T'")
        self.F()
        self.T_prime()

    def T_prime(self):
        if self.current_token[0] in ('TIMES', 'DIV'):
            print("T' → * F T'" if self.current_token[0] == 'TIMES'
                  else "T' → / F T'")
            if self.current_token[0] == 'TIMES':
                self.match('TIMES')
            else:
                self.match('DIV')
            self.F()
            self.T_prime()
        else:
            print("T' → ε")

    def F(self):
        if self.current_token[0] == 'NUM':
            print("F → num")
            self.match('NUM')
        elif self.current_token[0] == 'LPAREN':
            print("F → (E)")
            self.match('LPAREN')
            self.E()
            self.match('RPAREN')
        else:
            self.error("Factor inválido")

    # FUNCIÓN PRINCIPAL
    def parse(self):
        self.E()
        if self.current_token[0] != 'EOF':
            self.error("Entrada inválida")
        print("✔ Expresión válida")

# PROGRAMA INTERACTIVO
if __name__ == "__main__":
    print("=== Analizador Sintáctico LL(1) ===")

    while True:
        expr = input("\nIngrese una expresión aritmética: ")

        try:
            parser = ParserLL(expr)
            parser.parse()
        except Exception as e:
            print("✘", e)

        opcion = input("\n¿Desea analizar otra expresión? (s/n): ").lower()
        if opcion != 's':
            print("Saliendo del analizador LL...")
            break