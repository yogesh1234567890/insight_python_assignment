""" 27.​ Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8] """

import unittest
Sample1=[1, 3, 5, 7, 9, 10]
sample2=[2, 4, 6, 8]
def add(val1,val2):
    val1.remove(val1[-1])
    output=val1+val2
    return output

ans=add(Sample1,sample2)
print(ans)

class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add([2,3,4],[6,7]),([2,3,6,7]))

if __name__ =="__main__":
    unittest.main()
