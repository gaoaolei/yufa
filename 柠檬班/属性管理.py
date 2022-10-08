"""
第一题、自定义一个类
    1、通过上课的相关知识点对这个类创建的对象，进行属性限制，对象只能设置这个三个属性：  title    money   data
    2、通过相关机制对设置的属性类型进行限制，title只能设置字符串类型数据
    money设置为int类型数据  data可以设置为任意类型
    3、通过相关机制实现，data 属性不能进行删除
    4、类支持 obj[属性名] 这种语法获取属性值。

第二题、基于pymysql实现一个操作数据库的类DBClass，
实现上下文管理器协议，实现退出上下文时，自动关闭游标，断开连接
"""


class Demo:
    __slots__ = ['title', 'money', 'data']

    def __setattr__(self, key, value):
        if key == 'title':
            if isinstance(value, str):
                object.__setattr__(self, key, value)
            else:
                raise TypeError("title类型错误")

        if key == 'money':
            if isinstance(value, int):
                object.__setattr__(self, key, value)
            else:
                raise TypeError("money类型错误")
        if key == 'data':
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'data':
            pass
        else:
            object.__delattr__(self, item)

    def __getitem__(self, item):
        return object.__getattribute__(self, item)


import pymysql


class MyMysql:
    def __init__(self):
        self.cursor = None

    def __enter__(self):
        conn = pymysql.connect(host='47.96.76.135',  # host属性
                               port=3306,  # 端口号
                               user='root',  # 用户名
                               password='D*a93_Q08.z',  # 此处填登录数据库的密码
                               db='gao',  # 数据库名
                               charset="utf8")
        self.cursor = conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()


with MyMysql() as m:
    m.execute('select * from Persons')
    res = m.fetchall()
    print(res)
m.execute('select * from Persons')
