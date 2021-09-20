# 线程同步
# 例子：l的元素0被f1从后往前修改成1，f2从中间某个时刻读取，异步的时候可能读到一半1一半0的情况，数据不一致了，所以要同步
import threading
import time

print("主线程开始")
threadLock = threading.Lock()
l = []
for i in range(100):
    l.append(0)


def f1():
    threadLock.acquire()
    for i in range(100):
        time.sleep(0.1)
        l[99 - i] = 1
    threadLock.release()


def f2():
    threadLock.acquire()
    time.sleep(5)
    print(l)
    threadLock.release()


t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)

t = [t1, t2]
for i in t:
    i.start()
    # i.join()

print("主线程结束")
