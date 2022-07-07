import unittest
from student import Student


class StudentTestCase(unittest.TestCase):
    def fullname_test(self):
        ex_student = Student("Jon", "Snow", 4.5, None)
        self.assertEqual(ex_student.fullname, "Jon Snow")

