import unittest
from Exercice1 import f, find

class Test(unittest.TestCase):
    
    def test_find(self)->None:
        y = f(123456789)
        z = y + 1e-9
        result=find(f,y,0,10000000000)
        result2=find(f,z,0,10000000000)
        self.assertEqual(result, 123456789)
        self.assertEqual(result2, -1)
krkr
jjj
    




    

    
    
        

