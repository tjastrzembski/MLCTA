#!/usr/bin/python3
from FileParser.FileParser import FileParser

import re
from os import path
from antlr4 import *

from FileParser.Python.Python3Lexer import Python3Lexer
from FileParser.Python.Python3Parser import Python3Parser
from FileParser.Python.Python3Listener import Python3Listener


class FunctionPathListener(Python3Listener):
    def __init__(self, rule_names):
        super().__init__()
        self.rule_names = rule_names
        self.parsed_fct = set()

    def enterZope_fct_call(self, ctx):    
        path_tokens = [
            t for t in ctx.getChildren() 
            if self.rule_names[t.getRuleIndex()] == 'trailer'
        ]
        fct_path = []
        for token in path_tokens:
            fct_path.extend(token.getChildren())
    
        path_str = ''.join([t.getText() for t in fct_path])
        fct_name = re.findall(r'(?:\.)?([^\"\(]+)(?:\()?', path_str)
        if len(fct_name) > 1:
            fmt_fct_name = fct_name[0].replace('.','/')
            self.parsed_fct.add(fmt_fct_name)
    
    def get_fctname_list(self) -> set:
        return self.parsed_fct

class PythonFileParser(FileParser):

    def parse_file(self) -> None:
        lexer = Python3Lexer(self.file_handle)
        lexer.removeErrorListeners()
        stream = CommonTokenStream(lexer)
        parser = Python3Parser(stream)
        parser.removeErrorListeners()
        
        parse_tree = parser.file_input()
        
        function_path_listener = FunctionPathListener(parser.ruleNames)
        walker = ParseTreeWalker()
        walker.walk(function_path_listener, parse_tree)
        
        self.function_name_list = function_path_listener.get_fctname_list()


class JavaScriptFileParser(FileParser):
    def parse_file(self, file_path) -> None:
        pass





