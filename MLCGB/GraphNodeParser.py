from os import path
from MLCGB import MODULE_PATH
from MLCGB.FileParser.FileParserFactory import FileParserFactory

class GraphNodeParser:
    def __init__(
        self,
        repo_path,
        psql_handle
        ):
        self.repo_path = repo_path 
        self.psql = psql_handle
        self.unparsed_nodes = self.psql.exec_query(
            MODULE_PATH + '/PSQL/callingtree_unparsed_get_q.sql'
            )
        
    def parse_Nodes(self) -> None:
        for entry in self.unparsed_nodes:
            file_path = path.join(
                self.repo_path,
                entry['path'], 
                entry['filename']
            )
            # Add Multiprocessing here
            response, function_list = self.parse_file(
                file_path=file_path,
                interpretation_type= entry['itype'] 
            )
            if response == 1:
                self.psql.exec_query(
                    MODULE_PATH + '/PSQL/callingtree_parsedfile_set_q.sql',
                    modtime=entry['modtime'],
                    functionlist=list(function_list),
                    path=entry['path'],
                    filename= entry['filename'] 
                )
        self.psql.commit_changes()

    def parse_file(
        self,
        file_path, 
        interpretation_type
        ) -> list:
        file_parser_class = FileParserFactory.get_FileParser(
            interpretation_type=interpretation_type
        )
        if not file_parser_class:
            return 0 , set()
        file_parser = file_parser_class(
            file_path=file_path
        )
        return 1, file_parser.get_function_name_list()
