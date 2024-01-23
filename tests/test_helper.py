import unittest

from core.helper import AssetLoader


class TestImportLayout(unittest.TestCase):
    def test_raises_error_on_csv_empy(self):
        with self.assertRaisesRegex(FileNotFoundError, 'No such file or directory:'):
            next(AssetLoader.import_layout(''))
    
    def test_raises_error_no_args(self):
        with self.assertRaises(TypeError):
            next(AssetLoader.import_layout())

    def test_return_generator_with_values(self):
        gen = AssetLoader.import_layout('./tests/test.csv')

        self.assertTrue(hasattr(gen, '__next__'))

        val = next(gen)

        self.assertEqual(val[0], 'test')

if __name__ == '__main__':
    unittest.main()