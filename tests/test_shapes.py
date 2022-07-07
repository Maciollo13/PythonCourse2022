import unittest
from shapes import triangle, rectangle, trapezoid

class ShapesTestCase(unittest.TestCase):
    def setUp(self):
        self.sideA = 5
        self.sideB = 6

    def test_rectangle_with_correct_value(self):
        result = rectangle(5,6)
        self.assertEqual(result,30)

    def tearDown(self):
        del self.sideA
        del self.sideB

class Triangle_test(unittest.TestCase):
    def setUp(self):
        self.sideA = 5
        self.sideB = 6

    def test_triangle_with_correct_values(self):
        self.assertEqual(triangle(self.sideA,self.sideB),15)

    def tearDown(self):
        del self.sideB
        del self.sideA

class Trapez_test(unittest.TestCase):
    def setUp(self):
        self.sideA = 5
        self.sideB = 6
        self.heigth = 2

    def test_trapezoid_with_correct_values(self):
        self.assertEqual(trapezoid(self.sideA,self.sideB,self.heigth),11)

    def tearDown(self):
        del self.sideA
        del self.sideB
        del self.heigth

if __name__ == "__main__":
    unittest.main()