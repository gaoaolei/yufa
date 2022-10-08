import unittest
from concurrent.futures.thread import ThreadPoolExecutor
import time


def execute1(suite, mode):
    test_suite = []
    try:
        if mode == 'module':
            for m in suite:
                test_suite.append(m)
        if mode == 'cls':
            for m in suite:
                for c in m:
                    test_suite.append(c)
        if mode == 'case':
            for m in suite:
                for c in m:
                    for ca in c:
                        test_suite.append(ca)
        print(test_suite)
        with ThreadPoolExecutor(max_workers=len(test_suite)) as tp:
            result = unittest.TestResult()
            for i in test_suite:
                tp.submit(i.run, result)

        # print(test_suite)
    except Exception as e:
        print(e)


class TestAdd(unittest.TestCase):
    def test_001(self):
        time.sleep(1)

    def test_002(self):
        time.sleep(1)


class TestSub(unittest.TestCase):
    def test_001(self):
        time.sleep(1)

    def test_002(self):
        time.sleep(1)


class TestDiv(unittest.TestCase):
    def test_001(self):
        time.sleep(1)

    def test_002(self):
        time.sleep(1)


suite = unittest.defaultTestLoader.discover(r'D:\yufa')
execute1(suite, mode='mini')
