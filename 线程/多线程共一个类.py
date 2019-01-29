'''多个线程公用一个函数对象时，会创建多套局部变量，变量在各自的线程中使用，不会产生干扰'''
# _*_coding:utf-8_*_
import threading
from time import sleep
def thread_entry():
    var = 1
    for i in range(10):
        # print('th#{}:{}'.format(threading.currentThread().ident, var))
        print(f'th#{threading.currentThread().ident}:{var}')
        sleep(1)
        var += 1
        sleep(1)
if __name__ == '__main__':
    print('main thread is start')
    t1 = threading.Thread(target=thread_entry)
    t2 = threading.Thread(target=thread_entry)
    t1.start()
    sleep(1)
    t2.start()
