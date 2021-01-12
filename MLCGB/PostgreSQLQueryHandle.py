from perfact import dbconn

class PostgreSQLQueryHandle:
    def __init__(
        self, 
        dbconn_args
        ):
        self.dbconn = dbconn.DBConn(dbconn_args)

    def exec_query(
        self, 
        queryfile, 
        **kwargs
        ):
        with open(queryfile, 'r') as file:
            query = file.read()
        self.dbconn.execute(
            query,
            **kwargs
        )
        return self.dbconn.dictionaries()

    def commit_changes(self):
        self.dbconn.commit()
