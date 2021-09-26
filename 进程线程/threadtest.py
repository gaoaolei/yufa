'''python里面有两个管理线程的库：thread，threading'''

import threading
from time import sleep

print('main thread start')


def thread1_entry():
    print('child thread start')
    sleep(15)
    print('child thread end')


t1 = threading.Thread(target=thread1_entry)  # buid and initial a thread instance

t1.start()
sleep(10)
print(threading.current_thread())
print('main thread end')
