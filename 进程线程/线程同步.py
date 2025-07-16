# 线程同步
# 例子：l的元素0被f1从后往前修改成1，f2从中间某个时刻读取，异步的时候可能读到一半1一半0的情况，数据不一致了，所以要同步，线程同步会阻塞线程
#和join有点像，
"""
关键差异
join()的特点：
一次性阻塞：只在调用时阻塞，直到目标线程结束

不保护数据：只是等待线程结束，不解决资源共享问题

线程生命周期控制：用于确保线程执行顺序

同步机制的特点：
可重复使用：锁可以多次获取释放

保护共享数据：确保临界区代码的原子性执行

更细粒度控制：可以只保护必要的代码段
"""
import threading
import time
start=time.time()
print("主线程开始")
lock = threading.Lock()
l = []
for i in range(100):
    l.append(0)


def f1():
    lock.acquire()
    for i in range(100):
        time.sleep(0.1)
        l[99 - i] = 1
    lock.release()

def f3():
    with lock:   # 写法同acquire，release，现代简写
        for i in range(100):
            time.sleep(0.1)
            l[99 - i] = 1

def f2():
    lock.acquire()
    time.sleep(5)
    print(l)
    lock.release()


t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)

t = [t1, t2]
for i in t:
    i.start()
    # i.join()

print("主线程结束")
print(time.time()-start)