from django.test import TestCase

class BasicMathTest(TestCase):
    def test_basic_math(self):
        self.assertEqual(1 + 1, 2, "1 + 1 should equal 2")