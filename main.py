#!/usr/bin/python3
from time import time

# own Files
from PostgreSQLQueryHandle import PostgreSQLQueryHandle
from GraphNodeClassifier import GraphNodeClassifier
from GraphNodeParser import GraphNodeParser
from GraphNodeConnector import GraphNodeConnector

# For HTTP Requests regarding physical path
zope_url = 'http://localhost:9081'
global_acquisition = 'PerFact/DB_Utils/zLayout/zDB/zI18N/zMod/'
dbconn_args = "user=postgres dbname=perfactema"
zope_repo_path = '/opt/perfact/dbutils-zoperepo/__root__/'
zope_sub_path  = 'PerFact/WebApp/TestMask'
netrc_file = '/root/.netrc-callingtree'

if __name__ == '__main__':

    psql = PostgreSQLQueryHandle(
        dbconn_args=dbconn_args
    )

    start_time = time()
    print(f'Process repo_check...')
    gnclassifier = GraphNodeClassifier(
        zope_repo_path, 
        zope_sub_path,
        psql_handle=psql
    )
    gnclassifier.repo_check()
    end_time = time() - start_time
    hours = int(end_time / 3600)
    mins = int(end_time % 3600 / 60)
    secs = end_time % 60
    print(f'repo_check: Elapsed Time for:  {hours} hours {mins} mins {secs} sec')
    
    start_time = time()
    print(f'Process parse_Nodes...')
    parser = GraphNodeParser(
        repo_path=zope_repo_path,
        psql_handle=psql
    )
    parser.parse_Nodes()
    end_time = time() - start_time
    hours = int(end_time / 3600)
    mins = int(end_time % 3600 / 60)
    secs = end_time % 60
    print(f'parse_nodes: Elapsed Time for: {hours} hours {mins} mins {secs} sec')
    
    start_time = time()
    print(f'Process connect_nodes...')
    gnconnector = GraphNodeConnector(
        zope_url=zope_url,
        netrc_file=netrc_file,
        global_acquisition=global_acquisition,
        psql_handle=psql
    )
    gnconnector.process_queue()
    end_time = time() - start_time
    hours = int(end_time / 3600)
    mins = int(end_time % 3600 / 60)
    secs = end_time % 60
    print(f'connect_nodes: Elapsed Time for: {hours} hours {mins} mins {secs} sec')

    