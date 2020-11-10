#!/usr/bin/python3

# to establish connection to zope instance
# and get physical path for acquisition
# from http.client import HTTPResponse
# from urllib.parse import urlencode
# from urllib.error import HTTPError, URLError
# from urllib.request import Request, urlopen

from io import BytesIO  # for fast response storage
import pycurl


from os import walk, path, listdir
import re
from time import time
from perfact import dbconn

# own Files
from FileParser.FileParserFactory import FileParserFactory 


# For HTTP Requests regarding physical path
zope_url = 'http://localhost:9081'
global_acquisition = 'PerFact/DB_Utils/zLayout/zDB/zI18N/zMod/'
cust_dbconn =  dbconn.DBConn("user=postgres dbname=perfactema")
zope_repo_path = '/opt/perfact/dbutils-zoperepo/__root__/'
netrc_file = '/root/.netrc-callingtree'

supported_types = [
    'Script (Python)',
    'Z SQL Method',
    'Page Template',
    'File(text/css)',
    'File(text/html)',
    'File(text/javascript)',
    'File(text/sql)',
    'DTML Method',
    'DTML Document',
    'Page Template(text/html)',
    'Page Template(text/xml)'

    # If new types are acquired: here is the list
    # To clarify, which of those are required
    # 'Virtual Host Monster'
    # 'Simple User Folder',
    # 'Site Error Log',
    # 'Browser Id Manager',
    # 'Session Data Manager',
    # 'User Folder',
    # 'External Method',
    # 'Temporary Folder',
    # 'RAM Cache Manager',
    # 'ZSyncer',
    # 'Folder (Ordered)',
    # 'WebExtFile',
    # 'Accelerated HTTP Cache Manager',
    # 'Image',
    # 'Folder',
    # 'Control Panel',
    # 'Mail Host',
    # 'Z Psycopg 2 Database Connection',
    # 'File(application/font-woff)',
    # 'File(application/javascript)',
    # 'File(application/json)',
    # 'File(application/octet-stream)',
    # 'File(application/pdf)',
    # 'File(application/sql)',
    # 'File(application/vnd.ms-excel)',
    # 'File(application/vnd.ms-fontobject)',
    # 'File(application/vnd.oasis.opendocument.text)',
    # 'File(application/x-compressed-tar)',
    # 'File(application/x-dia-diagram)',
    # 'File(application/x-executable)',
    # 'File(application/x-font-ttf)',
    # 'File(application/x-font-woff)',
    # 'File(application/x-httpd-php)',
    # 'File(application/x-javascript)',
    # 'File(application/x-ms-dos-executable)',
    # 'File(application/x-msdos-program)',
    # 'File(application/x-msi)',
    # 'File(application/x-shockwave-flash)',
    # 'File(application/x-x509-ca-cert)',
    # 'File(application/xml)',
    # 'File(audio/mp4)',
    # 'File(audio/x-wav)',
    # 'File(font/opentype)',
    # 'File(font/truetype)',
    # 'File(font/ttf)',
    # 'File(image/bmp)',
    # 'File(image/gif)',
    # 'File(image/jpeg)',
    # 'File(image/png)',
    # 'File(image/svg+xml)',
    # 'File(text)',
    # 'File(text/markdown)',
    # 'File(text/plain)',
    # 'File(text/x-ms-regedit)',
    # 'File(text/x-python)',
    # 'File(text/x-sh)',
    # 'File(text/x-unknown-content-type)',
    # 'File(text/xml)',
    # 'File(video/mp4)',
    # 'Image(image/bmp)',
    # 'Image(image/gif)',
    # 'Image(image/jpeg)',
    # 'Image(image/png)',
    # 'Image(image/svg+xml)',
    # 'Image(image/x-icon)',
]
# extract class from perfact-assignd
class ResponseWriter:
    '''We need to wrap pycurl's writer callbacks for headers and body,
    so we can store each response (headers and body) separately.

    This class has functions to be used as callbacks, "headerfunc" and
    "bodyfunc", and pushes all responses into a list of tuples called
    "responses".
    If an error occurred, the flag "error" is set to True.
    '''

    def __init__(self):
        '''Initialize the list of responses and the error flag.'''
        self.responses = []
        self.error = False
        self.reset()

    def reset(self):
        '''Reset header and body storages, and the flag "body_called",
        which indicates that the next call to "headerfunc" belongs to
        the next response.
        '''
        self.headers = BytesIO()
        self.body = BytesIO()
        self.body_called = False

    def flush(self):
        '''If a new response begins, store the previous one.'''
        if self.body_called:
            headers_val = self.headers.getvalue()
            body_val = self.body.getvalue()
            self.responses.append(
                (headers_val, body_val)
            )
            if headers_val.find(b'\nBobo-Exception-Type:') != -1:
                self.error = True
            self.reset()

    def headerfunc(self, header_line):
        '''A header line comes in. First, flush if the previous
        response was finished. Check also for an empty header, which
        also triggers a new response on the subsequent call.'''
        self.flush()
        self.headers.write(header_line)
        if header_line.strip() == '':
            self.body_called = True

    def bodyfunc(self, bytes):
        '''Write a part of the response body, and set the signal that
        the next header will belong to the next response.
        '''
        self.body.write(bytes)
        self.body_called = True


def parse_file(
    file_path, 
    interpretation_type
    ) -> list:
    file_parser_class = FileParserFactory.get_FileParser(
        interpretation_type=interpretation_type
    )
    if not file_parser_class:
        #print(f'Skip this shit. {file_path} as {interpretation_type} is a lie.')
        return 0 , set()
    file_parser = file_parser_class(
        file_path=file_path
    )
    return 1, file_parser.get_function_name_list()

def parse_Nodes(
    repo_path
    ) -> None:
    res = exec_query('./PSQL/callingtree_unparsed_get_q.sql')
    for entry in res:
        file_path = path.join(
            repo_path,
            entry['path'], 
            entry['filename']
        )
        # Add Multiprocessing here
        #print(file_path)
        response, function_list = parse_file(
            file_path=file_path,
            interpretation_type= entry['itype'] 
        )
        if response == 1:
            exec_query(
                './PSQL/callingtree_parsedfile_set_q.sql',
                modtime=entry['modtime'],
                functionlist=list(function_list),
                path=entry['path'],
                filename= entry['filename'] 
            )
    cust_dbconn.commit()

# dict< file_path:str,graph_node:Node>
graph_dict = {}

class ConnectQueue:
    def __init__(
        self
    ):
        # List containing tuples<Node,str>
        # the str object contains acquisition path
        self.queue = []
        res = exec_query('./PSQL/callingtree_functionlist_get_q.sql')
        
        for entry in res:
            self.queue.append((entry, None))


    def connect_node(self)-> None:
        node, acquisition_path = self.queue.pop()

        #print(f'Node {node["callingtree_path"]}/{node["callingtree_filename"]}')
        # exit function, if no children nodes are given
        if not node['callingtree_functionlist']:
            return
        
        if acquisition_path is None:
            acquisition_path =  path.join( 
                global_acquisition,
                node['callingtree_path']
            )
        # check, if acquisition already processed
        # TODO: will this be efficient enough? Or do we need ident to stop?
        acquisition_check_res = exec_query(
                './PSQL/callingtree_acquisition_check_q.sql',
                caller_id=node['callingtree_id'],
                acquisition_path=acquisition_path
        )
        if acquisition_check_res[0]['already_checked']: 
           return

        # parts missing from function callstring
        acquisition_part_list = acquisition_path.split('/')

        for entry in node['callingtree_functionlist']:
            full_acquisition = path.join(
                acquisition_path, 
                entry
            )
            real_physical_path, filename = get_real_physical_path(full_acquisition)
            child_node_res = exec_query(
                    './PSQL/callingtree_get_q2.sql',
                    path=real_physical_path,
                    filename=filename
            )
            if len(child_node_res) == 0:
                continue
            
            child_node = child_node_res[0]
            
            function_path_parts = entry.split('/')
            function_path = '/'.join(function_path_parts[:-1])
            full_acquisition_path = path.join(
                acquisition_path, 
                function_path
            )

            # check if edge is already existent
            edge_res = exec_query(
                './PSQL/callingtreexcallingtree_get_q.sql',
                caller_id=node['callingtree_id'],
                called_id=child_node['callingtree_id'],
            )

            if len(edge_res) == 1:
                acquisition_list = edge_res[0]['cxc_acquisition']
                if full_acquisition_path in acquisition_list:
                    continue
                
                acquisition_list.append(full_acquisition_path)
            else:
                acquisition_list = [full_acquisition_path]

            # check child nodes on changes 
            self.queue.append((child_node, full_acquisition_path))

            exec_query(
                './PSQL/callingtreexcallingtree_ins_q.sql',
                caller_id=node['callingtree_id'],
                called_id=child_node['callingtree_id'],
                acquisition_path=acquisition_list
            )
    
    def process_queue(self) -> None:
        while len(self.queue) > 0:
            self.connect_node()
        cust_dbconn.commit()

def get_interpretation_type(
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
    repo_path,
    function_name,
    interpretation_type,
    physical_path
    ) -> None:

    fullpath = path.join(physical_path, function_name)
    # source files contains always one element
    source_file = [f for f in listdir(fullpath) if f != '__meta__']
    for filename in source_file:
        relative_path = physical_path.replace(repo_path, '')
        fullpathfile = path.join(fullpath, filename)
        modtime = path.getmtime(fullpathfile)
        res = exec_query(
            './PSQL/callingtree_set_q.sql',
            path=relative_path,
            filename=function_name,
            itype=interpretation_type,
            file_modded=modtime
        )

def callingtree_cleanup() -> None:
    exec_query('./PSQL/callingtree_cleanup_q.sql')

def repo_check(
    repo_path
    ) -> None:
    exec_query('./PSQL/callingtree_scanflag_reset_q.sql')
    for root, dirs, files in walk(repo_path):
        # functions/queries are actually folders having meta and source file
        for functiondir in dirs:
            # check only folder which might be associated
            # with zope (having metafile)
            
            fullpathmeta = path.join(root, functiondir, '__meta__')
            if not path.isfile(fullpathmeta):
                continue
        
            # check, if filetype is supported
            itype = get_interpretation_type(fullpathmeta)
            if itype not in supported_types:
                continue

            # if supported, check, if file is already processed
            # otherwise add Node
            create_graph_node(
                repo_path=repo_path,
                function_name=functiondir,
                interpretation_type=itype,
                physical_path=root
            )
    callingtree_cleanup()       
    cust_dbconn.commit()

# def check_zope_connection() -> HTTPResponse:
#     result = None
#     try:
#         response = urlopen(zope_url)
#         result = {
#             'status': response.status,
#             'msg': response.reason
#         }
#         response.read()

#     except HTTPError as err:
#         result = {
#             'status': err.code,
#             'msg': err.reason
#         }

#     return result

def  get_real_physical_path(acquisition_path) -> tuple:
        '''
        Gets physical path in Zope environment using libcurl.
        '''
        url = f'{zope_url}/{acquisition_path}/absolute_url_path'
        respwriter = ResponseWriter()

        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.CONNECTTIMEOUT, 20)
        curl.setopt(curl.FOLLOWLOCATION, True)
        curl.setopt(curl.HEADERFUNCTION, respwriter.headerfunc)
        curl.setopt(curl.NOSIGNAL, True)
        curl.setopt(curl.NOPROGRESS, True)
        curl.setopt(curl.SERVICE_NAME, 'callingtree')
        curl.setopt(curl.NETRC, 1)
        curl.setopt(curl.NETRC_FILE, netrc_file)
        curl.setopt(curl.HTTPAUTH, curl.HTTPAUTH_BASIC)
        curl.setopt(curl.UNRESTRICTED_AUTH, True)
        #curl.setopt(curl.COOKIEFILE, self.cookies)
        #curl.setopt(curl.COOKIEJAR, self.cookies)
        curl.setopt(curl.WRITEFUNCTION, respwriter.bodyfunc)
        curl.setopt(curl.SSL_VERIFYPEER, False)
        curl.setopt(curl.SSL_VERIFYHOST, False)

        curl.perform()
        curl.close()
        respwriter.flush()
        error = respwriter.error
       
        response = respwriter.responses[0]
        if error or b'200 OK\r\n' not in response[0]:
            return None, None
        
        #print(response[1])
        context = response[1].decode('utf-8').split('/')
        file_name = context[-1]
        path = '/'.join(context[1:-1])

        result = path, file_name
        return result


def main() -> None:
    # Make GraphDict
    # Make ParseQueue
    # Initialize minimal Zope instance or use existing one using web service
    
    #repo_check('./TestMask') #  input graphdict, ParseQueue
    
    # First check connection
    connection_res = check_zope_connection()
    if connection_res['status'] > 400:
        print('{} {}'.format(
            connection_res['status'],
            connection_res['msg']
        ))
    
        exit()
    
    #acquisition_path = 'PerFact/DB_Utils/zLayout/zDB/zI18N/zMod/WebApp/index_html'
    #response = get_real_physical_path(acquisition_path)
    #print(response)

    start_time = time()
    repo_check()
    end_time = time() - start_time
    print(f'Elapsed Time: {end_time} sec')
    while len(connect_queue.queue) > 0:
        connect_queue.connect_node()

    for key, node in graph_dict.items():
        print('Path: {}; Connect To: ({})'.format(
            key,
            ', '.join([f'{n.phyiscal_path}/{n.function_name}' for n in node.children])
        ))


def exec_query(queryfile, **kwargs):
    with open(queryfile, 'r') as file:
        query = file.read()
    cust_dbconn.execute(
        query,
        **kwargs
    )
    return cust_dbconn.dictionaries()

if __name__ == '__main__':

    start_time = time()
    print(f'Process repo_check...')
    repo_check(zope_repo_path)
    end_time = time() - start_time
    hours = int(end_time / 3600)
    mins = int(end_time % 3600 / 60)
    secs = end_time % 60
    print(f'repo_check: Elapsed Time for:  {hours} hours {mins} mins {secs} sec')
    
    start_time = time()
    print(f'Process parse_Nodes...')
    parse_Nodes(zope_repo_path)
    end_time = time() - start_time
    hours = int(end_time / 3600)
    mins = int(end_time % 3600 / 60)
    secs = end_time % 60
    print(f'parse_nodes: Elapsed Time for: {hours} hours {mins} mins {secs} sec')
    
    start_time = time()
    print(f'Process connect_nodes...')
    connect_queue = ConnectQueue()
    connect_queue.process_queue()
    end_time = time() - start_time
    hours = int(end_time / 3600)
    mins = int(end_time % 3600 / 60)
    secs = end_time % 60
    print(f'connect_nodes: Elapsed Time for: {hours} hours {mins} mins {secs} sec')

    