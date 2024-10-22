# interpreter.py
# Interpreter implementation. The interpreter will execute the AST produced by the parser.

class Interpreter:
    def __init__(self, ast, debug=False):
        self.ast = ast  # Store the AST directly
        self.debug = debug  # Debug mode toggle

    def interpret(self):
        """Interpret the parsed AST."""
        if self.ast is None:
            self.error("No AST produced from parsing")  # Handle empty AST case
        result = self._interpret(self.ast)
        return result  # Return the result instead of printing it
    
    def _interpret(self, node):
        """Evaluate the AST node."""
        if node is None:
            self.error("Attempted to interpret a None node")  # Handle None node
        return self.eval(node)  # Call eval to interpret the AST

    def eval(self, node):
        """Evaluate an expression or statement."""
        if self.debug:
            print("Evaluating:", node)  # Debugging line

        if node[0] == 'NUMBER':
            return node[1]
        elif node[0] == 'STRING':
            return node[1]  # Return the string value directly
        elif node[0] == 'BINOP':
            op = node[1]
            left = self.eval(node[2])
            right = self.eval(node[3])
            return self.apply_operator(op, left, right)
        else:
            self.error(f"Unexpected node type: {node[0]}")

    def apply_operator(self, op, left, right):
        """Apply the operator to the left and right operands."""
        if op == 'PLUS':
            return left + right
        elif op == 'MINUS':
            return left - right
        elif op == 'TIMES':
            return left * right
        elif op == 'DIVIDE':
            if right == 0:
                self.error("Division by zero")
            return left / right
        elif op == 'POWER':
            return left ** right  # Support for exponentiation
        elif op == 'MOD':
            return left % right  # Support for modulus
        else:
            self.error(f"Invalid operation: {op}")

    def error(self, message):
        """Raise an error with a specific message."""
        raise Exception(f'Runtime error: {message}')