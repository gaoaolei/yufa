"""
1、编程题）、一个列表中有100个url地址,每个地址请求一次，请设计程序一个程序，
使用4个线程去发送这 100个请求（假设请求每个地址需要0.5秒，请求的代码用time.sleep(0.5)代替）,
计算一共需要多长时间计算出总耗时！（注意点：是4个线程一共发送100个请求，不是每个线程发送100个，不要理解错了
"""
from threading import Thread
import time

a = list(range(20))
def run():
    for i in a:
        a.remove(i)
        time.sleep(0.5)
        print(i)


if __name__ == '__main__':
    start_time = time.time()
    for i in range(4):
        t = Thread(target=run, name="thread-" + str(i))
        t.start()
    t.join()
    end_time = time.time()
    print(end_time-start_time)