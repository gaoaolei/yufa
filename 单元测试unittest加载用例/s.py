import para
import test
import unittest
#方式一
suite = unittest.TestSuite()
suite.addTest(para.testMethod('test001'))
suite.addTest(para.testMethod('test002'))
suite.addTest(test.Test('test_001'))
suite.addTest(test.Test('test_002'))
suite.addTest(test.Test('test_003'))

#方式二
# suite1 = unittest.TestLoader().loadTestsFromTestCase(para.testMethod)
# suite2 = unittest.TestLoader().loadTestsFromTestCase(test.Test)
# suite = unittest.TestSuite([suite1, suite2])


runner = unittest.TextTestRunner()
runner.run(suite)
