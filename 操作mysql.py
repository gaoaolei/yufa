'''
本电脑上安装的是mysql-connector-2.1.4 + mysql-5.5.56
还有比较常见的库有MySQLdb
笔者在用python的MysqlDB包对Mysql进行insert操作时出现了问题，程序运行不报错，insert语句也没有问题，但是新的数据一直没有插入到数据库中。在查阅了资料之后，发现是未提交的原因。
数据库语言可分为四种，
数据操作语言（Date Manipulation Language）DML语言，实现对数据的基本操作，”增删改”。
UPDATE DELETE INSERT
数据定义语言（Data Definition Language ）DDL语言，可以实现对数据库结构、操作方法等的定义：
create table 创建表
alter table 修改表
drop table 删除表
truncate table 删除表中所有行
create index 创建索引
drop index 删除索引**
数据库控制语言（Data Control Language）DCL授权，角色控制
GRANT 授权
REVOKE 取消授权
事务控制语言（Transaction Control Language）事务控制语言
SAVEPOINT 设置保存点
ROLLBACK 回滚
SET TRANSACTION
在这之中，DDL语句是自带commit的，而执行DML命令如果没有提交，将不会被其他会话看到。除非在DML命令之后执行了DDL命令或DCL命令，或用户退出会话，或终止实例，此时系统会自动发出commit命令，使未提交的DML命令提交。

建议每次 对MYSQL中的表修改或插入数据后 都提交一下(commit) ！

付费的商用数据库：

Oracle，典型的高富帅；

SQL Server，微软自家产品，Windows定制专款；

DB2，IBM的产品，听起来挺高端；

Sybase，曾经跟微软是好基友，后来关系破裂，现在家境惨淡。

这些数据库都是不开源而且付费的，最大的好处是花了钱出了问题可以找厂家解决，不过在Web的世界里，常常需要部署成千上万的
数据库服务器，当然不能把大把大把的银子扔给厂家，所以，无论是Google、Facebook，还是国内的BAT，无一例外都选择了免费的
开源数据库：

MySQL，大家都在用，一般错不了；

PostgreSQL，学术气息有点重，其实挺不错，但知名度没有MySQL高；

sqlite，嵌入式数据库，适合桌面和移动应用，python内置了SQLite3，所以连接sqlite数据库时直接连，import sqlite3即可。

MySQLdb is a C module that links against the MySQL protocol implementation in the libmysqlclient library. It is
faster, but requires the library in order to work.

mysql-connector is a Python module that reimplements the MySQL protocol in Python. It is slower, but does not
require the C library and so is more portable.

'''
# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='4209841413pl', host='localhost', database='a', port='3307')
cursor = conn.cursor()
try:
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
except Exception:
    cursor.execute('drop table user')
# 创建user表:
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Kobe'])
cursor.executemany('insert into user (id, name) values (%s, %s)', [('3', 'gaorui'), ('4', 'gaorong')])

print(cursor.rowcount)       # 上一条语句影响的数据库行数
conn.commit()
print(cursor.rowcount)
# 查询
cursor.execute('select * from user where id = 2')

values = cursor.fetchall()        # 接收全部的返回结果行 ，返回结果为tuple
print(values)

# 关闭Cursor和Connection:
cursor.close()
conn.close()


# MySQLdb--返回数据但没有字段
import MySQLdb.cursors
host = '172.16.100.80'
port = 3306
user = 'qimao_free_test'
password = 'd3R6d190ZXN0Cg=='
database = 'qimao_free'
conn = MySQLdb.connect(host=host,port=port,user=user,password=password,database=database,charset = 'utf8',cursorclass = MySQLdb.cursors.DictCursor)
cursor = conn.cursor()
cursor.execute("SELECT * FROM adv WHERE area_config_id=11 AND platform=1 AND STATUS=1 AND min_app_version=40060 AND ab_group_id='' AND adv_code !='' ")
a = cursor.fetchone()       #返回的是()
a = cursor.fetchall()       #返回的是((),(),())
print(type(a))

# # MySQLdb--返回数据且有字段
import MySQLdb.cursors
host = '172.16.100.80'
port = 3306
user = 'qimao_free_test'
password = 'd3R6d190ZXN0Cg=='
database = 'qimao_free'
conn = MySQLdb.connect(host=host,port=port,user=user,password=password,database=database,charset = 'utf8',cursorclass = MySQLdb.cursors.DictCursor)
cursor = conn.cursor()
cursor.execute("SELECT * FROM adv WHERE area_config_id=11 AND platform=1 AND STATUS=1 AND min_app_version=40060 AND ab_group_id='' AND adv_code !='' ")
a = cursor.fetchone()       #返回的是{}
a = cursor.fetchall()       #返回的是({},{},{})
print(type(a))

# mysql.connector--返回数据但没字段
import mysql.connector
host = '172.16.100.80'
port = 3306
user = 'qimao_free_test'
password = 'd3R6d190ZXN0Cg=='
database = 'qimao_free'
conn = mysql.connector.connect(host=host,port=port,user=user,password=password,database=database,charset = 'utf8')
cursor = conn.cursor()
cursor.execute("SELECT * FROM adv WHERE area_config_id=11 AND platform=1 AND STATUS=1 AND min_app_version=40060 AND ab_group_id='' AND adv_code !='' ")
a = cursor.fetchone()       #返回的是()
a = cursor.fetchall()       #返回的是[(),(),()]
print(a)

# mysql.connector--返回数据且有字段
import mysql.connector
host = '172.16.100.80'
port = 3306
user = 'qimao_free_test'
password = 'd3R6d190ZXN0Cg=='
database = 'qimao_free'
conn = mysql.connector.connect(host=host,port=port,user=user,password=password,database=database,charset = 'utf8')
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM adv WHERE area_config_id=11 AND platform=1 AND STATUS=1 AND min_app_version=40060 AND ab_group_id='' AND adv_code !='' ")
a = cursor.fetchone()       #返回的是{}
a = cursor.fetchall()       #返回的是[{},{},{}]
print(a)