import unittest
import app

class Test_my_program(unittest.TestCase):

    def setup(self):

        self.app = app

    def test_fact(self):

        self.assertEqual(6, app.factor(3))

    def test_inp(self):

        self.assertIsInstance(app.inp(3), int)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()