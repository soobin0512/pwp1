# DB_Helper.py

import common.oracle_db as odb

class DBHelper:
    # 멤버변수(field)
    conn = ''

    # 생성자(constructor)
    def __init__(self):
        odb.oracle_init()
        self.conn = odb.connect()

    # 소멸자(destructor)
    def __del__(self):
        if self.conn:
            odb.close(self.conn)

    # 멤버함수(method)
    def db_insertCrawlingData(self, T):
        # cursor = self.conn.cursor()
        with self.conn.cursor() as cursor:  # cursor 자동 close 됨
            query = "insert into tour values (seq_tour.nextval, :1, :2, :3, :4, :5)"
            cursor.execute(query, T)
        odb.commit(self.conn)

