print('主函数开始')
try:
    print(10 / 0)
    print('产生错误了就不会执行')
except:
    print('产生错误了')
else:
    print('没有错误就执行这句')
finally:
    print('不论有无错误总是执行')
print('主函数执行')

