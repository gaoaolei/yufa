from multiprocessing import Pool
import time


def task(n):
    time.sleep(1)  # 模拟耗时操作
    return n * n


# 创建一个有最大4个进程的进程池
with Pool(4) as pool:
    # 映射任务到进程池中的进程
    results = pool.map(task, range(10))
    for result in results:
        print(f'Result: {result}')