from MLCGB.FileParser import FileParser
from MLCGB.FileParser.PythonFileParser import PythonFileParser
from MLCGB.FileParser.DTMLFileParser import DTMLFileParser
from MLCGB.FileParser.TALFileParser import TALFileParser

#from JavaScriptFileParser import JavaScriptFileParser

class FileParserFactory:
    type_map = {
        'Script (Python)': PythonFileParser,
        'Z SQL Method': DTMLFileParser,
        'Page Template': TALFileParser,
        'File(text/html)': TALFileParser,
        # 'File(text/javascript)': JavaScriptFileParser,
        'File(text/sql)': DTMLFileParser,
        'DTML Method': DTMLFileParser,
        'DTML Document': DTMLFileParser,
        'Page Template(text/html)': TALFileParser
    }

    @staticmethod
    def get_FileParser(interpretation_type) -> FileParser:
        file_parser = FileParserFactory.type_map.get(interpretation_type)
        return file_parser
