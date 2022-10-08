# 1、通过列表推导式完成下面数据类型转换，现在有以下数据， li1 = ["{'a':11,'b':2}", "[11,22,33,44]"]，需要转换为
# 以下格式： li1 = [{'a': 11, 'b': 2}, [11, 22, 33, 44]]
li1 = ["{'a':11,'b':2}", "[11,22,33,44]"]
res1 = [eval(i) for i in li1]
print(res1)


# 2、 Names = ['python', 'java', 'php', 'c', 'c++', 'django', 'unittest', 'pytest','pymysql'], 请通过列表推导式，
# 获取names中字符串长度大于4的元素
Names = ['python', 'java', 'php', 'c', 'c++', 'django', 'unittest', 'pytest', 'pymysql']
res2 = [i for i in Names if len(i) > 4]
print(res2)


# 3、通过字典推导式，颠倒字典的键名和值: 将{'py': "python09", 'java': "java09"}转换为： {'python09': "py", 'java09': "java"}
dic = {'py': "python09", 'java': "java09"}
res3 = {item[1]: item[0] for item in dic.items()}
res3_1 = {v: k for k, v in dic.items()}
print(res3)
print(res3_1)


# 4、将字典{'x': 'A', 'y': 'B', 'z': 'C'}通过推导式转换为：['x=A', 'y=B', 'z=C']
dic = {'x': 'A', 'y': 'B', 'z': 'C'}
res4 = ["{}={}".format(k, v) for k, v in dic.items()]
print(res4)
