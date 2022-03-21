# Python 單元測試官網文件
# https://docs.python.org/zh-tw/3/library/unittest.html


def calculate(w, h):
    return round(w/h**2,2)

def cmToM(cm):
    return cm/100


if __name__ == '__main__':
    import unittest
    class BmiTestCase(unittest.TestCase):

        def test_calculate(self):
            result = calculate(65, 1.75)
            self.assertEqual(21.22, result)

        def test_cmToM(self):
            result = cmToM(175)
            self.assertEqual(1.75, result)

    tests = [
        BmiTestCase('test_calculate'),
        BmiTestCase('test_cmToM')
    ]
    suite = unittest.TestSuite()
    suite.addTests(tests)

    runner = unittest.TextTestRunner()
    runner.run(suite)
