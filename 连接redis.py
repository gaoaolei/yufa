import pymysql

class MysqlEngine(object):
    def __init__(self, host=None, port=None, user=None, password=None, database=None, conn=None, auto_commit=True):
        """
        :param host: 数据库ip
        :param port: 端口
        :param user: 用户名
        :param password: 密码
        :param database: 数据库连接db
        :param conn: pymysql链接
        :param auto_commit: 执行sql后是否自动提交
        """
        self.host = '172.31.28.13'
        self.port = '3306'
        self.user = 'jira_readonly'
        self.password = 'jira_readonly'
        self.database = 'jiradb'
        self.conn = conn
        self.auto_commit = auto_commit
        self.connect()

    def connect(self) -> pymysql.Connection:
        """
        获取pymysql连接conn
        @return:
        """
        if not (self.conn and self.conn.open):
            self.conn = pymysql.connect(
                host=self.host,
                port=self.port if isinstance(self.port, int) else int(self.port),
                user=self.user,
                password=self.password,
                database=self.database,
                charset="utf8"
            )
        return self.conn

    # def table(self, table_name):
    #     """
    #     @param table_name: 表名
    #     @return:数据库表对象
    #     """
    #     return Table(table_name, **self.attributes())

    def call(self, sql, params=None, many=False) -> (int, int):
        """
        @param sql:可执行事务sql
        @param params: 参数list
        @param many: 是否批量插入
        @return: 返回插入数据主键id 和 数据变更的条数
        """
        # logger.debug('{}  {}'.format(sql, params))
        conn = self.connect()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        if many:
            rowcount = cursor.executemany(sql, params)
        else:
            rowcount = cursor.execute(sql, params if params else None)
        if self.auto_commit:
            conn.commit()
        insert_id = cursor.lastrowid  # 插入数据的自增id
        return insert_id, rowcount

    def commit(self):
        """提交事务"""
        if self.conn and self.conn.open:
            self.conn.commit()

    def call_search(self, sql, params=None) -> (list, int):
        """
        @param sql:查询sql
        @param params: 参数list
        @param search_one: 是否查询单条数据
        @return: 返回数据list，和数据总条数（忽略分页）
        """
        if not params:
            params = None
        # logger.debug('{}  {}'.format(sql, params))
        conn = self.connect()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql, params if params else None)
        result = cursor.fetchall()
        cursor.execute('select FOUND_ROWS() as count')
        count = cursor.fetchone()['count']
        return result, count

    def show_tables(self) -> list:
        """
        @return:返回库中所有表名
        """
        table_list = []
        data_list, _ = self.call_search(
            "select table_name as table_name from information_schema.tables where table_schema='{}'".format(
                self.database))
        for data in data_list:
            table_list.append(data['table_name'])
        return table_list

    def attributes(self) -> dict:
        """获取对象自定义的属性"""
        attributes = self.__dict__
        kwargs = dict()
        for k, v in attributes.items():
            if not k.startswith('_'):
                kwargs[k] = v
        return kwargs

print(MysqlEngine(port=1234).attributes())
print(MysqlEngine(port=1234).__dict__)