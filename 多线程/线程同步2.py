import time, threading

# 假定这是你的银行存款: 没有锁之前，最终结果不一定是0，加锁后一定是0
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n
lock = threading.Lock()
def run_thread(n):
    for i in range(2000000):
        # lock.acquire()
        change_it(n)
        # lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)