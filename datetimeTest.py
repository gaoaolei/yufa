from datetime import datetime          # 前面一个datetime是模块，后面一个是类
print('-----------打印当前日期时间------------------')
print(datetime.now())
print(type(datetime.now()))

# import datetime
# print(datetime.datetime.now())

print('---------------获取指定日期和时间-----------------')
print(datetime(2017, 12, 30, 11, 5, 00))
print('--------------datetime转换成时间戳-----------------')
print(datetime(2017, 12, 30, 11, 5, 00).timestamp())      # 2不能书写02，但可以写00，参数必须为inter
print(datetime(2017, 12, 30, 11, 5, 1).timestamp())
print(datetime.now().timestamp())
print('-------------时间戳转化成datetime(北京时间)----------------')
print(datetime.fromtimestamp(1514603100))
print(datetime.fromtimestamp(datetime.now().timestamp()))
print('----------------时间戳转换成UTC datetime(格林尼治时间)--------------------')
print(datetime.utcfromtimestamp(1514603100))
print(datetime.utcfromtimestamp(datetime.now().timestamp()))
print('----------------datetime转换成str------------------')
print(datetime.now().strftime('%a %b-%d %H:%M'))
# datetime加减
from datetime import timedelta
print(datetime.now()+timedelta(hours=1))
print(datetime.now()+timedelta(days=1))
print(datetime.now()+timedelta(weeks=1))
print(datetime.now()+timedelta(weeks=1, days=1, hours=1))
print('---------------本地时间转换成utc时间-----------------')
print(datetime.tzinfo)            # tzinfo是datetime类的属性,默认为None
print(type(datetime.tzinfo))            # tzinfo是datetime类的属性,默认为None
print(datetime.now().tzinfo)
from datetime import timezone
# print(datetime.now().replace(tzinfo=8))
print(datetime.now().replace(tzinfo=timezone(timedelta(hours=8))))

