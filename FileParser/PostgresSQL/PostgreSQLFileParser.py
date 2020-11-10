#!/usr/bin/PostgreSQL
from os import path
from antlr4 import *

from FileParser.FileParser import FileParser
from FileParser.Python.PostgreSQLLexer import PostgreSQLLexer
from FileParser.Python.PostgreSQLParser import PostgreSQLParser
from FileParser.Python.PostgreSQLListener import PostgreSQLListener

class FunctionPathListener(PostgreSQLListener):
    

class PostgreFileParser(FileParser):
    def parse_file(self, file_path) -> None:
        pass



#     Traceback (most recent call last):
#   File "main.py", line 346, in <module>
#     connect_queue.connect_node()
#   File "main.py", line 156, in connect_node
#     if acquisition_path in node.acquisition:
# AttributeError: 'tuple' object has no attribute 'acquisition'