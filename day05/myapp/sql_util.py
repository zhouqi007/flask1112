import pymysql

class SQLTool:

    def __init__(self,user,pwd,host,port,db):
        self.client = pymysql.connect(
            user=user,
            password=pwd,
            host=host,
            port=port,
            database=db

        )
        self.cursor = self.client.cursor()

    def query(self,sql):
        self.cursor.execute(sql)

        return self.cursor.fetchall()