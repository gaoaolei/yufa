import logging
from datetime import datetime
import os


class LogUtil():
    def __init__(self, logname=None):
        # 日志名称
        self.logger = logging.getLogger(logname)
        # 日志级别
        self.logger.setLevel(logging.DEBUG)
        # 日志输出到控制台
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        # 输出到文件
        # self.date = datetime.now().strftime("%Y-%m-%d") + '.log'
        import time
        self.date = str(time.time()) + '.log'
        self.filename = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log', self.date)
        self.file = logging.FileHandler(self.filename, encoding='utf-8')
        self.file.setLevel(logging.DEBUG)
        # 日志显示内容
        self.formatstr = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
        self.format = logging.Formatter(self.formatstr)
        self.console.setFormatter(self.format)
        self.file.setFormatter(self.format)
        # 加入到hander
        self.logger.addHandler(self.console)
        self.logger.addHandler(self.file)

    def get_logger(self):
        return self.logger

