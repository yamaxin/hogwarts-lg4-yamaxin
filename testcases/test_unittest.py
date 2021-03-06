import unittest

class Testupper(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(Testupper('test_isupper'))
    # unittest.TextTestRunner().run(suite)


    suite=unittest.TestLoader().loadTestsFromTestCase(Testupper)
    st=unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=2).run(st)