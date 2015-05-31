import nose
import unittest


class MyTestCase(unittest.TestCase):

    def test_with_docstring(self):
        """
        Test that something does something i can fly
        """
        pass

    def test_without_docstring(self):
        pass


if __name__ == '__main__':
    nose.run(argv=["nosetests" "forsevascript.py", "--verbosity=2"])