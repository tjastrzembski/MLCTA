#!/usr/bin/python3

from abc import ABC, abstractmethod
from os import path, listdir
from antlr4 import FileStream

class FileParser(ABC):
    def __init__(
        self,
        file_path
        ):
        self.function_name_list = []
        self.file_handle = None

        # NOTE: I assume that every method folder contains 2 files
        # one of those files ends always with __meta__ 
        source_file = [f for f in listdir(file_path) if f != '__meta__']
        if len(source_file) == 0:
            return

        full_path = path.join(file_path, source_file[0])
        try:
            self.file_handle = FileStream(full_path, encoding='utf-8')
            self.parse_file()
        except UnicodeDecodeError:
            # Mark as not readable
            print(f'UnicodeDecodeError on {full_path}. Skip file.')
            return
        
    
    @abstractmethod
    def parse_file(self) -> None:
        print('should not be executed')
        pass

    def get_function_name_list(self) -> set:
        return self.function_name_list


