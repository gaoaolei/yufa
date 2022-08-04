import threading
import time

#
# def f():
#     time.sleep(1)
#     print("主线程开始", threading.current_thread().name)
#
#
# print(threading.current_thread().name)
#
# th_list = []
# for i in range(5):
#     th_list.append(threading.Thread(target=f))
#
# for i in th_list:
#     # i.setDaemon(True)     # setDaemon为True则主线程结束，子线程也结束
#     i.start()
#     # i.join()           # join是阻塞主线程，timeout为空则一直阻塞直到子线程全部结束，有timeout则主线程等待timeout*线程个数的时间后结束
#
# print("主进程结束")

# join是阻塞主线程调用子线程，必须前一个子线程执行完后才能执行下一个子线程，这就是同步，那有人问，那这样和单线程有什么区别呢？答案是多线程效率高，
# 但是多个线程可能会操作同一个数据，这就导致数据不一致的问题，此时必须join同步，当然还有别的方法加锁Lock。
def f():
    print('aaa')
threading.Thread(target=f).start()