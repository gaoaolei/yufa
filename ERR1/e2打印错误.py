try:
    print(10 / 0)
    print('产生错误了就不会执行')

except Exception as e:
    print(f'产生错误了:{e}')
else:
    print('没有错误就执行这句')
finally:
    print('不论有无错误总是执行')
print('主函数执行')