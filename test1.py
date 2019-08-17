from enum import Enum,unique
@unique
class E(Enum):
    Yellow = 1
    Red = 2
    Green = 3

if __name__ == '__main__':
    print(E.Yellow)
    print(E['Yellow'])
    print(E.Yellow.name)
    print(E.Yellow.value)
    print(E(3))

    for i in E:
        print(i.value)

