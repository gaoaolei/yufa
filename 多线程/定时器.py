import os
import re
import threading
import time

def getTotalPss():
    lines = os.popen("adb shell dumpsys meminfo com.kmxs.reader ").readlines()  # 逐行读取
    Native = "Native Heap "
    Dalvik = "Dalvik Heap "
    for line in lines:
        # 获取Native内存
        if re.findall(Native, line):  # 找到Native 这一行
            lis1 = line.split(" ")  # 将这一行，按空格分割成一个list
            while '' in lis1:  # 将list中的空元素删除
                lis1.remove('')
        # 获取Dalvik内
        if re.findall(Dalvik, line):
            lis2 = line.split(" ")
            while '' in lis2:
                lis2.remove('')
            # print("Dalvik Heap:" + lis2[2])  # Dalvik内存
            nativePss = int(lis1[2]) / 1024
            dalvikPss = int(lis2[2]) / 1024
            totalPss = '%.2f' % (nativePss + dalvikPss)  # 总内存
            print(time.strftime('%H:%M:%S', time.localtime(time.time())) + " " +
                  str(totalPss) + 'MB')  # 调用定时器

            """调用定时器"""
            createTimer()

# 创建定时器
def createTimer():
    t = threading.Timer(1, getTotalPss)  # 定时器是子线程，隔1s执行getTotalPss
    t.start()


createTimer()
