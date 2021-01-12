from os import walk, path, listdir
import re

from MLCGB import MODULE_PATH

class GraphNodeClassifier:
    def __init__(
        self,
        repo_path,
        sub_path,
        psql_handle
    ):
        self.psql = psql_handle
        res = self.psql.exec_query(
            MODULE_PATH + '/PSQL/callingtreetype_get_q.sql'
        )
        if len(res) > 0:
            self.supported_types = res[0]['supported_types']

        self.repo_path = repo_path
        self.sub_path = sub_path

    def repo_check(self) -> None:
        used_path = path.join(self.repo_path, self.sub_path)
        self.psql.exec_query(
            MODULE_PATH + '/PSQL/callingtree_scanflag_reset_q.sql'
        )
        
        for root, dirs, files in walk(used_path):
            # functions/queries are actually folders having meta and source file
            for functiondir in dirs:
                # check only folder which might be associated
                # with zope (having metafile)
                fullpathmeta = path.join(root, functiondir, '__meta__')
                if not path.isfile(fullpathmeta):
                    continue
            
                # check, if filetype is supported
                itype = self.get_interpretation_type(fullpathmeta)
                if itype not in self.supported_types:
                    continue

                # if supported, check, if file is already processed
                # otherwise add Node
                self.create_graph_node(
                    function_name=functiondir,
                    interpretation_type=itype,
                    physical_path=root
                )
        self.callingtree_cleanup()       
        self.psql.commit_changes()

    def get_interpretation_type(
        self,
        metafilename
    ) -> str:
        '''
        Checks interpretation type of its associated source file.
        It also checks existence of searched expression inside meta file.

        Input arguments:
        metafilename    - meta file with full path expected <string>

        Return value:
        Interpretationtype of associated source file <string>
        '''
        with open(metafilename, 'r') as f:
            content = f.read()

        # 1. Get interpretation type
        itype = None
        result = re.findall(
            r'\(\s*\'type\'\s*,\s*\'(.+)\'\s*\)',
            content
        )
        if len(result) > 0:
            itype = result[len(result)-1]
            if itype in ['File']:
                result = re.findall(
                    r'\(\s*\'value\'\s*,\s*\'(.+)\'\s*\)',
                    content
                )
                if len(result) > 0:
                    itype = f'{itype}({result[0]})'

        return itype

    def create_graph_node(
        self,
        function_name,
        interpretation_type,
        physical_path
    ) -> None:
        fullpath = path.join(physical_path, function_name)
        # source files contains always one element
        source_file = [f for f in listdir(fullpath) if f != '__meta__']
        for filename in source_file:
            relative_path = physical_path.replace(self.repo_path, '')
            fullpathfile = path.join(fullpath, filename)
            modtime = path.getmtime(fullpathfile)
            self.psql.exec_query(
                MODULE_PATH + '/PSQL/callingtree_set_q.sql',
                path=relative_path,
                filename=function_name,
                itype=interpretation_type,
                file_modded=modtime
            )

    def callingtree_cleanup(self) -> None:
        self.psql.exec_query(
            MODULE_PATH + '/PSQL/callingtree_cleanup_q.sql',
            path=f'^{self.sub_path}'
        )
