import psycopg2

class Database():
    def __init__(self, table):
        self._table = table
        self._connection = None
        self._setConnection()
    
    def _setConnection(self):
        #abrindo conexão
        try:
            connection = psycopg2.connect(host="engine-bd", port="5432", user="postgres",password="postgres")
            self._connection = connection.cursor()
        except:        
            raise ValueError("Não foi possivel abrir a conexão com o banco de dados",500)
    
    def execute(self):
        pass
        