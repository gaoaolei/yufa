import logging
#创建日志log文件，注意是log后缀
log_filename='loggingTest.log'
#设置日志格式
log_format='%(filename)s [%(asctime)s] [%(levelname)s] %(message)s'
#设置时间格式
datetime='%Y-%m-%d %H:%M:%S'

#设置日志输出格式和级别
#filemode:以什么模式操作文件
logging.basicConfig(filename=log_filename,filemode='a',format=log_format,datefmt=datetime,level=logging.DEBUG)
logging.debug('aaaaaaaaa')
logging.info('xiaodeng')
logging.warning('python')



def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    # except和else互斥，finally总是执行
    try:
        bar('0')
    except Exception as e:
        # logging.basicConfig(filename=log_filename, filemode='w', format=log_format, datefmt=datetime,
        #                     level=logging.DEBUG)
        logging.exception(e)

    else:
        print('else')
    finally:
        print('finally')
main()
