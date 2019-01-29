# i=0
def f(x):
    i=0
    if x>=25:
          i=i+x/25
          if x%25!=0:
                f(x%25)
    if 10<=x<25:
          i=i+x/10
          if x%10!=0:
                f(x%10)
    if 5<=x<10:
          i=i+x/5
          if x%5!=0:
                f(x%5)
    if x<5:
          i=i+x/1
    print i        # 试试改成return
print(f(9))