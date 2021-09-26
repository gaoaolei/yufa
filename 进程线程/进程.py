# 子进程的创建
from multiprocessing import Process
import os

def run1():    # 注意不要写run，run是Process的方法，会有冲突
    print("Child Precess ID is %s And My Parent is %s" % (os.getpid(), os.getppid()))


# if __name__ == "__main__":              #  必须要这行，不知道为什么
#     p = Process(target=run1)
#     p1 = Process(target=run1)
#     p.start()
#     p1.start()
#     p.join()
#     p1.join()


# 进程池
if __name__ == "__main__":
    from multiprocessing import Pool
    po = Pool(50)
    for i in range(50):
        po.apply_async(run1)
    po.close()
    po.join()