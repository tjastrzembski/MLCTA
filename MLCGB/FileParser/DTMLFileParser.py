#!/usr/bin/python3
from MLCGB.FileParser.FileParser import FileParser

import re
from os import path
from antlr4 import *

from MLCGB.FileParser.DTML.DTMLLexer import DTMLLexer
from MLCGB.FileParser.DTML.DTMLParser import DTMLParser
from MLCGB.FileParser.DTML.DTMLParserListener import DTMLParserListener


class FunctionPathListener(DTMLParserListener):
    def __init__(self):
        super().__init__()
        self.parsed_fct = set()

    def enterDtml_tag_expr_val(self, ctx):    
        for t in ctx.getChildren():
            expr_statement = t.getText()
            fct_name = re.findall(r'([^\"\(]+)\(', expr_statement)
            for entry in fct_name:
                fmt_fct_name = entry.replace('.','/')
                self.parsed_fct.add(fmt_fct_name)
    
    def enterDtml_tag_var(self, ctx):    
        for t in ctx.getChildren():
            self.parsed_fct.add(t.getText())
    
    def get_fctname_list(self) -> set:
        return self.parsed_fct

    

class DTMLFileParser(FileParser):

    def parse_file(self) -> None:
        lexer = DTMLLexer(self.file_handle)
        stream = CommonTokenStream(lexer)
        parser = DTMLParser(stream)
        parser.removeErrorListeners()
        
        parse_tree = parser.parse()
        
        function_path_listener = FunctionPathListener()
        walker = ParseTreeWalker()
        walker.walk(function_path_listener, parse_tree)
        
        self.function_name_list = function_path_listener.get_fctname_list()
