#!/usr/bin/python3
from MLCGB.FileParser.FileParser import FileParser

import re
from os import path
from antlr4 import *

from MLCGB.FileParser.TAL.TALLexer import TALLexer
from MLCGB.FileParser.TAL.TALParser import TALParser
from MLCGB.FileParser.TAL.TALParserListener import TALParserListener


class FunctionPathListener(TALParserListener):
    def __init__(self):
        super().__init__()
        self.parsed_fct = set()

    def enterFunction_ref(self, ctx):
        path_str = ''.join([
            t.getText() for t in ctx.getChildren()
           ]) 
        fct_name = re.findall(r'(?:[\.\/])?([^\"\(]+)(?:\()?', path_str)
        for entry in fct_name:
            fmt_fct_name = entry.replace('.','/')
            self.parsed_fct.add(fmt_fct_name)
    
    def get_fctname_list(self) -> set:
        return self.parsed_fct

class TALFileParser(FileParser):

    def parse_file(self) -> None:
        lexer = TALLexer(self.file_handle)
        stream = CommonTokenStream(lexer)
        parser = TALParser(stream)
        parser.removeErrorListeners()
        
        parse_tree = parser.parse()
        
        function_path_listener = FunctionPathListener()
        walker = ParseTreeWalker()
        walker.walk(function_path_listener, parse_tree)
        
        self.function_name_list = function_path_listener.get_fctname_list()
