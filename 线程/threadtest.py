'''python里面有两个管理线程的库：thread，threading'''

print('main thread start')

import threading
from time import sleep
def thread1_entry():
    print('child thread start')
    sleep(15)
    print('child thread end')
t1 = threading.Thread(target=thread1_entry, name='a')    # buid and initial a thread instance

t1.start()
sleep(10)
print(threading.current_thread())
print('main thread end')

