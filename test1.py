from multiprocessing import Process
import os

def run1():
    print("child process id %s" % os.getpid())
if __name__ == "__main__":

    t = Process(target=run1)
    t.start()
    t.join()


# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc():
#     print('Run child process  (%s)...' % (os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc)
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')