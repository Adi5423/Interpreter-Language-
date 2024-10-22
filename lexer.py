# Lexer implementation  The lexer will convert the input source code into tokens
import re

# Define token types
TOKEN_TYPES = [
    ('NUMBER', r'\d+'),          # Integer
    ('STRING', r'"([^"\\]*(\\.[^"\\]*)*)?"'),  # String literal
    ('PLUS', r'\+'),             # Addition
    ('MINUS', r'-'),             # Subtraction
    ('TIMES', r'\*'),            # Multiplication
    ('DIVIDE', r'/'),            # Division
    ('IF', r'if'),               # If keyword
    ('ELSE', r'else'),           # Else keyword
    ('LPAREN', r'\('),           # Left Parenthesis
    ('RPAREN', r'\)'),           # Right Parenthesis
    ('NEWLINE', r'\n'),          # New line
    ('SKIP', r'[ \t]+'),         # Skip spaces and tabs
]

# Create a regex pattern for all token types
TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES)

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Advance the `pos` pointer and set `current_char`."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def tokenize(self):
        tokens = []
        while self.pos < len(self.text):
            match = re.match(TOKEN_REGEX, self.text[self.pos:])
            if match:
                token_type = match.lastgroup
                token_value = match.group(token_type)
                if token_type == 'NUMBER':
                    tokens.append(('NUMBER', int(token_value)))
                elif token_type == 'STRING':
                    tokens.append(('STRING', token_value[1:-1]))  # Remove quotes
                elif token_type != 'SKIP' and token_type != 'NEWLINE':
                    tokens.append((token_type, token_value))
                self.pos += len(token_value)
            else:
                self.error()
        return tokens

# # Example usage:
# if __name__ == "__main__":
#     lexer = Lexer('2 + 3 * (4 - 5)')
#     tokens = lexer.tokenize()
#     print(tokens)  # Should print a list of tokens