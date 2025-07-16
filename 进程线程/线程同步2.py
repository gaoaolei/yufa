import random
import time, threading

# 假定这是你的银行存款: 没有锁之前，最终结果不一定是0，加锁后一定是0
balance = 0

lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        change_it(n)
        lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t3 = threading.Thread(target=run_thread, args=(9,))
t4 = threading.Thread(target=run_thread, args=(11,))
t5 = threading.Thread(target=run_thread, args=(100,))
t6 = threading.Thread(target=run_thread, args=(123,))
t7 = threading.Thread(target=run_thread, args=(5,))
t8 = threading.Thread(target=run_thread, args=(5,))
t9 = threading.Thread(target=run_thread, args=(5,))
t10 = threading.Thread(target=run_thread, args=(5,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t8.join()
t10.join()

print(balance)
