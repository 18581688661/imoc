import pymysql
from common.yamlconfig import GetConf


class Mysql_operate:
    def __init__(self):
        mysql_conf = GetConf().get_mysql_conf()
        self.host = mysql_conf["host"]
        self.db = mysql_conf["db"]
        self.port = mysql_conf["port"]
        self.user = mysql_conf["user"]
        self.password = mysql_conf["password"]
        self.conn = None
        self.cur = None

    def __conn_db(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                port=self.port,
                charset="utf-8"
            )
        except Exception as e:
            print(e)
            return False

        self.cur = self.conn.cursor()
        return True

    def __close_conn(self):
        self.cur.close()
        self.conn.close()
        return True

    def query(self, sql):
        self.__conn_db()
        self.cur.execute(sql)
        query_data = self.cur.fetchall()
        if query_data == ():
            query_data = None
            print("没有数据")
        else:
            pass
        self.__close_conn()
        return query_data

    def __commit(self):
        self.conn.commit()
        return True

    def insert(self,sql):
        self.__conn_db()
        self.cur.execute(sql)
        self.__commit()
        self.__close_conn()


if __name__ == '__main__':
    print(Mysql_operate().query("select * from user;"))