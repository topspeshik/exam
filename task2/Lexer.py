from Token import Token
from TokenType import TokenType


class LexerException(Exception):
    ...


class Lexer:

    def __init__(self):
        self.pos = 0
        self.text = ""
        self.current_char = ""

    def init_lexer(self, text: str):
        self.pos = 0
        self.text = text
        self.current_char = self.text[self.pos]

    def forward(self):
        self.pos += 1
        if self.pos == len(self.text):
            self.current_char = ""
        else:
            self.current_char = self.text[self.pos]

    def next(self) -> Token:
        while self.current_char != "":
            if self.current_char.isspace():
                self.skip()
                continue
            if self.current_char.isdigit():
                return Token(TokenType.NUMBER, self.number())
            if self.current_char.isalpha():
                ch = ""
                while self.current_char.isalpha():
                    ch += self.current_char
                    self.forward()
                if ch == 'int':
                    return Token(TokenType.TYPE, ch)
                else:
                    return Token(TokenType.VARIABLE, ch)
            if self.current_char == "*":
                ch = self.current_char
                self.forward()
                return Token(TokenType.POINTER, ch)
            if self.current_char == "&":
                ch = self.current_char
                self.forward()
                return Token(TokenType.REFERENCE, ch)

            if self.current_char == '=':
                ch = self.current_char
                self.forward()
                return Token(TokenType.ASSIGN, ch)

            if self.current_char == ';':
                ch = self.current_char
                self.forward()
                return Token(TokenType.SEMI, ch)
            print(self.current_char.isspace())
            raise LexerException("bad token")
        return Token(TokenType.EOL, "")

    def skip(self):
        while self.current_char != "" and self.current_char.isspace():
            self.forward()

    def number(self) -> str:
        result = []
        while self.current_char != "" and \
                (self.current_char.isdigit() or
                 self.current_char == '.'):
            result.append(self.current_char)
            self.forward()
        return "".join(result)


s = "int value = 10; int* ptr = &value;"

lexer = Lexer()

lexer.init_lexer(s)

current_token = lexer.next()

while current_token.type != TokenType.EOL:
    print(current_token)
    current_token = lexer.next()