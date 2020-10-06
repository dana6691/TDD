import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,6),16)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)
        
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,6),4)
        self.assertEqual(calc.subtract(-1,1),-2)
        self.assertEqual(calc.subtract(-1,-1),0)
        
    def test_multiply(self):
        self.assertEqual(calc.multiply(10,6),60)
        self.assertEqual(calc.multiply(-1,1),-1)
        self.assertEqual(calc.multiply(-1,-1),1)
        
    def test_divide(self):
        #result = calc.divide(10,6)
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertEqual(calc.divide(-1,-1),1)
        # when it's in error
        with self.assertRaises(ValueError):
            calc.divide(10,0)

 #run all of them       
if __name__ == '__main__':
    unittest.main()