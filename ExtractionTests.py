import unittest

from pathlib import Path


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.sample_one_liners = Path('one_liners.docx')
        self.sample_paras_type1 = Path('type1_paras.docx')

    def tearDown(self):
        pass

    def test_samples_exist(self):
        for sample in [self.sample_paras_type1, self.sample_one_liners]:
            with self.subTest(msg="Sample Missing", sample=sample):
                note = 'Expected `{file}` to be available'.format(file=sample.resolve())
                self.assertTrue(sample.exists(), msg=note)



if __name__ == '__main__':
    unittest.main()
