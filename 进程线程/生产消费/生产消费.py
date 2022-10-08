import queue
import threading
import time

q = queue.Queue()


# 生产者
def f1():
    for i in range(100):
        time.sleep(0.1)
        q.put(i)

t1 = threading.Thread(target=f1)
# # 生产者
def f1():
    for i in range(100):
        time.sleep(0.5)
        q.put(i)

t3 = threading.Thread(target=f1)
##生产者
def f1():
    for i in range(100):
        time.sleep(0.5)
        q.put(i)

t5 = threading.Thread(target=f1)

# 消费者
def f2():
    for i in range(100):
        time.sleep(0.3)
        v = q.get()
        print(v)
        print(q.queue)
t2 = threading.Thread(target=f2)
def f2():
    for i in range(100):
        time.sleep(0.3)
        v = q.get()
        print(v)
        print(q.queue)
t4 = threading.Thread(target=f2)
def f2():
    for i in range(100):
        time.sleep(0.3)
        v = q.get()
        print(v)
        print(q.queue)
t6 = threading.Thread(target=f2)

print(q.queue)
t1.start()
t3.start()
t2.start()
t4.start()
t6.start()

