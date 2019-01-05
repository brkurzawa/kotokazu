import src.parse
import tinysegmenter as ts
import unittest


class TestFrequencyParser(unittest.TestCase):

    def test_sentence(self):
        correct = [('私', 1), ('の', 1), ('名前', 1), ('は', 1), ('中野', 1), ('です', 1)]
        self.assertCountEqual(correct, src.parse.get_frequency(ts.tokenize("私の名前は中野です")))


if __name__ == "__main__":
    unittest.main()
