import unittest

class Dollar:
    def __init__(self,amount):
        self.amount = amount
        
    def times(self, multiplyer):
        return Dollar(self.amount * multiplyer)

class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        fiver = Dollar(5)
        tenner = fiver.times(2)
        self.assertEqual(10, tenner.amount)

if __name__ == '__main__':
    unittest.main()