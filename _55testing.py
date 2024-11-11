import unittest
import _56testcontent as main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, test_param + 5)


unittest.main()
