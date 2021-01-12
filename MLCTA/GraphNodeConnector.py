from io import BytesIO  # for fast response storage
from os import path
import pycurl
from MLCTA import MODULE_PATH

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

class GraphNodeConnector:
    def __init__(
        self,
        zope_url,
        netrc_file,
        global_acquisition,
        psql_handle
    ):
        # List containing tuples<Node,str>
        # the str object contains acquisition path
        self.psql = psql_handle
        self.zope_url = zope_url
        self.netrc_file = netrc_file
        self.global_acquisition = global_acquisition
        self.queue = []
        
        res = self.psql.exec_query(
            MODULE_PATH + '/PSQL/callingtree_functionlist_get_q.sql'
            )
        
        for entry in res:
            self.queue.append((entry, None))

    def connect_node(self)-> None:
        node, acquisition_path = self.queue.pop()

        # exit function, if no children nodes are given
        if not node['callingtree_functionlist']:
            return
        
        if acquisition_path is None:
            acquisition_path =  path.join( 
                self.global_acquisition,
                node['callingtree_path']
            )
        # check, if acquisition already processed
        acquisition_check_res = self.psql.exec_query(
                MODULE_PATH + '/PSQL/callingtree_acquisition_check_q.sql',
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
            real_physical_path, filename = self.get_real_physical_path(
                full_acquisition
            )
            child_node_res = self.psql.exec_query(
                    MODULE_PATH + '/PSQL/callingtree_get_q2.sql',
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
            edge_res = self.psql.exec_query(
                MODULE_PATH + '/PSQL/callingtreexcallingtree_get_q.sql',
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

            self.psql.exec_query(
                MODULE_PATH + '/PSQL/callingtreexcallingtree_ins_q.sql',
                caller_id=node['callingtree_id'],
                called_id=child_node['callingtree_id'],
                acquisition_path=acquisition_list
            )
    
    def process_queue(self) -> None:
        while len(self.queue) > 0:
            self.connect_node()
        self.psql.commit_changes()

    def  get_real_physical_path(
        self,
        acquisition_path
    ) -> tuple:
        '''
        Gets physical path in Zope environment using libcurl.
        '''
        url = f'{self.zope_url}/{acquisition_path}/absolute_url_path'

        #replace hashtags which leads to crash 
        url = url.replace('#','')
        respwriter = ResponseWriter()

        try:
            curl = pycurl.Curl()
            curl.setopt(curl.URL, url)
            curl.setopt(curl.CONNECTTIMEOUT, 5)
            curl.setopt(curl.TIMEOUT, 5)
            curl.setopt(curl.FOLLOWLOCATION, True)
            curl.setopt(curl.HEADERFUNCTION, respwriter.headerfunc)
            curl.setopt(curl.NOSIGNAL, True)
            curl.setopt(curl.NOPROGRESS, True)
            curl.setopt(curl.SERVICE_NAME, 'callingtree')
            curl.setopt(curl.NETRC, 1)
            curl.setopt(curl.NETRC_FILE, self.netrc_file)
            curl.setopt(curl.HTTPAUTH, curl.HTTPAUTH_BASIC)
            curl.setopt(curl.UNRESTRICTED_AUTH, True)
            curl.setopt(curl.WRITEFUNCTION, respwriter.bodyfunc)
            curl.setopt(curl.SSL_VERIFYPEER, False)
            curl.setopt(curl.SSL_VERIFYHOST, False)
        except UnicodeEncodeError:
            return None, None

        try:
            curl.perform()
            curl.close()
            respwriter.flush()
            error = respwriter.error
        except pycurl.error:
            return None, None
        
        response = respwriter.responses[0]
        if error or b'200 OK\r\n' not in response[0]:
            return None, None
        
        context = response[1].decode('utf-8').split('/')
        file_name = context[-1]
        path = '/'.join(context[1:-1])

        result = path, file_name
        return result
