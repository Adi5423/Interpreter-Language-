# parser.py
# Parser implementation
# The parser will take the tokens produced by the lexer and build an Abstract Syntax Tree (AST).

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = self.tokens[0] if tokens else None
        self.position = 0

    def error(self, message='Invalid syntax'):
        raise Exception(message)

    def advance(self):
        """Advance the `position` pointer and set `current_token`."""
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None  # Set to None when out of tokens

    def parse(self):
        """Parse the tokens into an AST."""
        if not self.tokens:
            return None  # No tokens to parse
        result = self.expr()  # Start parsing with an expression
        self.check_for_unexpected_tokens()  # Check for any unexpected tokens
        return result

    def check_for_unexpected_tokens(self):
        """Raise an error if there are unexpected tokens left."""
        if self.current_token is not None:
            self.error(f"Unexpected token: {self.current_token}")

    def expr(self):
        """Parse expressions (numbers, strings, and binary operations)."""
        # print("Entering expr() with current_token:", self.current_token)  # Debugging line
        left = self.term()

        while self.current_token is not None and self.current_token[0] in ('PLUS', 'MINUS'):
            op = self.current_token
            self.advance()  # Move past operator
            right = self.term()
            left = ('BINOP', op[0], left, right)  # Create binary operation node

        return left

    def term(self):
        """Parse terms (numbers, strings, and binary operations)."""
        # print("Entering term() with current_token:", self.current_token)  # Debugging line
        left = self.factor()

        while self.current_token is not None and self.current_token[0] in ('TIMES', 'DIVIDE'):
            op = self.current_token
            self.advance()  # Move past operator
            right = self.factor()
            left = ('BINOP', op[0], left, right)  # Create binary operation node

        return left

    def factor(self):
        """Parse factors (numbers, strings, and parentheses)."""
        # print("Entering factor() with current_token:", self.current_token)  # Debugging line
        if self.current_token is None:
            return None  # Return None if there are no tokens

        token_type, value = self.current_token
        if token_type == 'NUMBER':
            self.advance()  # Move past the number
            return ('NUMBER', value)
        elif token_type == 'STRING':
            self.advance()  # Move past the string
            return ('STRING', value)  # Return the string node
        elif token_type == 'LPAREN':
            self.advance()  # Skip '('
            node = self.expr()
            if self.current_token is None or self.current_token[0] != 'RPAREN':
                self.error("Missing closing parenthesis")  # Missing closing parenthesis
            self.advance()  # Skip ')'
            return node
        self.error(f"Unexpected token in factor: {self.current_token}")  # Raise an error for unexpected token