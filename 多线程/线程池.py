from multiprocessing.pool import ThreadPool

def f(x):
    print(x+1)

ThreadNum = 1
pool = ThreadPool(ThreadNum)   # 创建线程池，有3个线程
pool.map(f,list(range(1000000)))
pool.close()
pool.join()
print(pool)