"""
1、用一个队列来存储数据

2、创建一个专门生产数据的任务函数，循环生产5次数据，每轮循环，往队列中添加20条数据，每循环一轮暂停1秒

3、创建一个专门处理数据的任务函数 循环获取队列中的数据处理，每秒处理4条数据。

4、创建一个线程生产数据 ，3个线程处理数据
5、统计数据生产并获取完  程序运行的总时长
"""

from queue import Queue
import time

a = Queue()
a.put(111)
print(a)

def work():
    for i in range(5):
        for j in range(20):
            a.put(j)
        time.sleep(1)

def custom():
    pass