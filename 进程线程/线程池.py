##################################这种方法没人用了##############################
"""
map只能传1个参数，apply_async可以传多个参数--
from multiprocessing.pool import ThreadPool
import time

def func(p,s):
    print(p,s)
    time.sleep(3)

tic = time.time()
my_task = [1,2,3,4,5,6,7,8,9,10]
pool = ThreadPool(5)
for item in my_task:
    pool.apply_async(func, args=(item,"可以"))  # 把任务放入线程池，进行


在 python 中使用线程池有两种方式，一种是基于第三方库 threadpool，另一种是基于 python3 新引入的库 concurrent.futures.ThreadPoolExecutor，这里我们介绍一下后一种。
concurrent.futures.ThreadPoolExecutor，在提交任务的时候有两种方式，一种是submit（）函数，另一种是map（）函数，两者的主要区别在于：
1）、map可以保证输出的顺序, submit输出的顺序是乱的。

2）、如果你要提交的任务的函数是一样的，就可以简化成map。但是假如提交的任务函数是不一样的，或者执行的过程之可能出现异常（使用map执行过程中发现问题会直接抛出错误）就要用到submit（）。

3）、submit和map的参数是不同的，submit每次都需要提交一个目标函数和对应的参数，map只需要提交一次目标函数，目标函数的参数放在一个迭代器（列表，字典）里就可以。


"""
import time
from multiprocessing.pool import ThreadPool

import pymysql


def task(x):
    time.sleep(2)
    return x*x


# now = time.time()
# pool = ThreadPool(processes=20)  # 测试下1,10,50,100你就知道了，同时你也可以把task函数改成计算型的，你就会处理时间区别不大，所以对比计算型，python多线程确实没啥用
# results = pool.map(task, range(100))
# pool.close()
# pool.join()
# print(results)
# print("耗时：", time.time() - now)


##########################################第二种，常用的是这种################################
from concurrent.futures import ThreadPoolExecutor


# 定义一个任务函数
def task(n):
    print('条数：', n)
    mysql_client_24_50_conn = pymysql.connect(host='172.31.24.50', port=3306, user='couponcenter',
                                              password='couponcenter',
                                              database='couponcenterdb')
    mysql_client_24_50_cursor = mysql_client_24_50_conn.cursor()
    sql = """INSERT INTO `ct_retry_notify_info` (`gmt_modified`, `gmt_create`, `notify_content`, `notify_result`, `notify_count`, `ext0`) VALUES ('2025-07-22 11:40:03.850', '2025-07-22 11:40:03', '[{\"ad_token\":\"c02e57600196100097bf3030c0a80fd464b\",\"fail_code\":1024,\"fail_message\":\"\",\"sent_time\":1753056197822,\"channel\":4,\"callback_type\":2,\"notification_state\":\"null\",\"msg_id\":\"2809c022b_287658956182929431\"}]', '', 0, '11111');
"""
    mysql_client_24_50_cursor.execute(sql)
    mysql_client_24_50_conn.commit()
    # mysql_client_24_50_cursor.close()


# 创建线程池
with ThreadPoolExecutor(max_workers=100) as executor:
    # 提交任务到线程池
    futures = [executor.submit(task, i) for i in range(1000000)]    # 用100个线程跑100万次

    # 获取结果
    for future in futures:
        print(f"结果: {future.result()}")
