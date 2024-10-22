# Entry point of your interpreter

from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    print("Enter your code (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    
    # Join the lines into a single string
    text = "\n".join(lines)
    
    lexer = Lexer(text)
    tokens = lexer.tokenize()
    print("Tokens:", tokens)  # Debugging line
    parser = Parser(tokens)
    ast = parser.parse()
    print("AST:", ast)  # Debugging line
    interpreter = Interpreter(ast)
    result = interpreter.interpret()
    print("Output:", result)  # Print the output from the interpreter

if __name__ == '__main__':
    main()