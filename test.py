#!/usr/bin/python3

# own Files
from PostgreSQLQueryHandle import PostgreSQLQueryHandle
from GraphNodeClassifier import GraphNodeClassifier
from GraphNodeParser import GraphNodeParser
from GraphNodeConnector import GraphNodeConnector

from psycopg2 import OperationalError, errors

# For HTTP Requests regarding physical path
zope_url = 'http://localhost:9081'
global_acquisition = 'PerFact/DB_Utils/zLayout/zDB/zI18N/zMod/'
dbconn_args = "user=postgres dbname=perfactema"
zope_repo_path = '/opt/perfact/dbutils-zoperepo/__root__/'
zope_sub_path  = 'PerFact/WebApp/TestMask'
netrc_file = '/root/.netrc-callingtree'

psql = PostgreSQLQueryHandle(
    dbconn_args=dbconn_args
)

def test_psql_handle():
    try:
        cust_psql = PostgreSQLQueryHandle(
            dbconn_args=dbconn_args
        )
        res = cust_psql.exec_query('./PSQL/tests/check_connection_q.sql')
        assert len(res) > 0
    except OperationalError as err:
        assert False, err

def test_psql_table_callingtree():
    try:
        res = psql.exec_query('./PSQL/tests/callingtree_get_q.sql')
        assert len(res) > 0
    except (errors.UndefinedTable, OperationalError) as err:
        assert False, err

def test_psql_table_callingtreetype():
    try:
        res = psql.exec_query('./PSQL/tests/callingtreetype_get_q.sql')
        assert len(res) > 0
    except (errors.UndefinedTable, OperationalError) as err:
        assert False, err

def test_psql_table_callingtreexcallingtree():
    try:
        res = psql.exec_query('./PSQL/tests/callingtreexcallingtree_get_q.sql')
        assert len(res) > 0
    except (errors.UndefinedTable, OperationalError) as err:
        assert False, err
        
def test_GraphNodeConnector_check_connection():
    gnconnector = GraphNodeConnector(
        zope_url=zope_url,
        netrc_file=netrc_file,
        global_acquisition=global_acquisition,
        psql_handle=psql
    )
    res = gnconnector.get_real_physical_path('')
    assert res == ('', '')


