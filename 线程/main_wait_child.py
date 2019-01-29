# _*_coding:utf-8_*_
import threading
from time import sleep, ctime
print('main thread is start at %s' % ctime())
sleep(5)
# 定义线程1函数对象
def thread1_entry(nsec):
    print('thread1 is start at %s' % ctime())
    sleep(nsec)
    print('thread1 is end at %s' % ctime())
# 定义线程1函数对象
def thread2_entry(nsec):
    print('thread2 is start at %s' % ctime())
    sleep(nsec)
    print('thread2 is end at %s' % ctime())
# 创建线程实例对象
t1 = threading.Thread(target=thread1_entry, args=(5,))
t2 = threading.Thread(target=thread2_entry, args=(5,))
t1.start()
sleep(6)
t2.start()
t1.join()      # 等待t1线程结束
t2.join()
print('main thread is end at %s' % ctime())
