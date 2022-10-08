import unittest
from concurrent.futures.thread import ThreadPoolExecutor
import time

class TestAdd(unittest.TestCase):
    def test_001(self):
        time.sleep(1)
        print('111111')

    def test_002(self):
        time.sleep(1)
        print('2222')

class TestSub(unittest.TestCase):
    def test_001(self):
        time.sleep(1)
        print('3333')

    def test_002(self):
        time.sleep(1)
        print('4444')

class TestDiv(unittest.TestCase):
    def test_001(self):
        time.sleep(1)
        print('5555')

    def test_002(self):
        time.sleep(1)
        print('6666')

suite = unittest.defaultTestLoader.discover(r'D:\yufa')

mod_suite = []
for i in suite:
    for j in i:
        for k in j:
            mod_suite.append(k)
print(mod_suite)
result = unittest.TestResult()
if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=6) as tp:
        for i in mod_suite:
            tp.submit(i.run, result)


