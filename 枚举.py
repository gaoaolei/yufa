from enum import Enum
a = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(a)
print(a['Jan'])                #通过name获取member
print(a.Jan.name)              #通过属性name获取name
print(a.Jan.value)             #通过属性value获取value
print(list(a))
for i in a:
    print(i)




'''1. 枚举的定义

首先，定义枚举要导入enum模块。
枚举定义用class关键字，继承Enum类。
用于定义枚举的class和定义类的class是有区别【下一篇博文继续分享】。
　　示例代码:

复制代码
from enum import Enum

class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7
复制代码
代码分析：                    ******   成员      = 名称 + 值    *****************************************
                            ******   Color.red = red  + 1     *****************************************

上面的代码，我们定义了颜色的枚举Color.
颜色枚举有7个成员，分别是Color.red、Color.orange、Color.yellow等。
每一个成员都有它们各自名称和值，Color.red成员的名称是：red，值是：1。
每个成员的数据类型就是它所属的枚举。【*注：用class定义的类，实际上就是一种类型】
1.1 定义枚举时，成员名称不允许重复　　　
from enum import Enum

class Color(Enum):
    red = 1
    red = 2
　　上面的代码，就无法执行。提示错误：TypeError: Attempted to reuse key: 'red'

　1.2 默认情况下，不同的成员值允许相同。但是两个相同值的成员，第二个成员的名称被视作第一个成员的别名　　

from enum import Enum

class Color(Enum):
    red = 1
    red_alias = 1
　　成员Color.red和Color.red_alias具有相同的值，那么成员Color.red_alias的名称red_alias就被视作成员Color.red名称red的别名。

   1.3 如果枚举中存在相同值的成员，在通过值获取枚举成员时，只能获取到第一个成员

复制代码
from enum import Enum

class Color(Enum):
    red = 1
    red_alias = 1

print(Color(1))
复制代码
　　输出结果为：Color.red

　1.4 如果要限制定义枚举时，不能定义相同值的成员。可以使用装饰器@unique【要导入unique模块】

复制代码
from enum import Enum, unique


@unique
class Color(Enum):
    red = 1
    red_alias = 1
复制代码
　　再执行就会提示错误：ValueError: duplicate values found in <enum 'Color'>: red_alias -> red

 

2. 枚举取值 

　2.1 通过成员的名称来获取成员

Color['red']
　2.2 通过成员值来获取成员

Color(2)
　2.3 通过成员，来获取它的名称和值

red_member = Color.red
red_member.name
red_member.value
 

3. 迭代器

　3.1 枚举支持迭代器，可以遍历枚举成员

for color in Color:
    print(color)
　　输出结果是，枚举的所有成员。Color.red、Color.orange、Color.yellow、Color.green、Color.blue、Color.indigo、Color.purple。

　3.2 如果枚举有值重复的成员，循环遍历枚举时只获取值重复成员的第一个成员

复制代码
from enum import Enum


class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7
    red_alias = 1


for color in Color:
    print(color)
复制代码
　　输出结果是：Color.red、Color.orange、Color.yellow、Color.green、Color.blue、Color.indigo、Color.purple。但是Color.red_alias并没有出现在输出结果中。

　3.3 如果想把值重复的成员也遍历出来，要用枚举的一个特殊属性__members__

复制代码
from enum import Enum


class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7
    red_alias = 1


for color in Color.__members__.items():
    print(color)
复制代码
　　输出结果：('red', <Color.red: 1>)、('orange', <Color.orange: 2>)、('yellow', <Color.yellow: 3>)、('green', <Color.green: 4>)、('blue', <Color.blue: 5>)、

　　　　　　　('indigo', <Color.indigo: 6>)、('purple', <Color.purple: 7>)、('red_alias', <Color.red: 1>)

 

4. 枚举比较

　4.1 枚举成员可进行同一性比较

Color.red is Color.red
　　输出结果是：True

Color.red is not Color.blue
　　输出结果是：True

　4.2 枚举成员可进等值比较

Color.blue == Color.red
　　输出结果是：False

Color.blue != Color.red
　　输出结果是：True

　4.3 枚举成员不能进行大小比较

Color.red < Color.blue
　　输出结果出错：TypeError: unorderable types: Color() < Color()'''