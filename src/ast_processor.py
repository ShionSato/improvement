from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from Java8Lexer import Java8Lexer
from Java8Parser import Java8Parser
from pprint import pformat


class AstProcessor:

    def __init__(self, logging, listener):
        self.logging = logging
        self.logger = logging.getLogger(self.__class__.__name__)
        self.listener = listener

    def execute(self, input_source):
        parser = Java8Parser(CommonTokenStream(Java8Lexer(FileStream(input_source, encoding="utf-8"))))
        walker = ParseTreeWalker()
        walker.walk(self.listener, parser.compilationUnit())
        self.logger.debug('Display all data extracted by AST. \n' + pformat(self.listener.ast_info, width=160))
        return self.listener.ast_info
