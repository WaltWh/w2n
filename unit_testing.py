import unittest

from w2n import w2n

general_test_data = [("two million three thousand nine hundred and eighty four", 2003984),
                     ("nineteen", 19),
                     ("two thousand and nineteen", 2019),
                     ("two million three thousand and nineteen", 2003019),
                     ('three billion', 3000000000),
                     ('three million', 3000000),
                     ('one hundred twenty three million four hundred fifty six thousand seven hundred and eighty nine',
                      123456789),
                     ('eleven', 11),
                     ('nineteen billion and nineteen', 19000000019), ('one hundred and forty two', 142),
                     ('112', 112),
                     ('11211234', 11211234),
                     ('five', 5),
                     ('two million twenty three thousand and forty nine', 2023049),
                     ('two point three', 2.3),
                     ('two million twenty three thousand and forty nine point two three six nine', 2023049.2369),
                     ('one billion two million twenty three thousand and forty nine point two three six nine',
                      1002023049.2369),
                     ('point one', 0.1),
                     ('point', 0),
                     ('point nineteen', 0),
                     ('one hundred thirty-five', 135),
                     ('hundred', 100),
                     ('thousand', 1000),
                     ('million', 10 ** 6),
                     ('billion', 10 ** 9),
                     ('trillion', 10 ** 12),
                     ('quadrillion', 10 ** 15),
                     ('quintillion', 10 ** 18),
                     ('sextillion', 10 ** 21),
                     ('septillion', 10 ** 24),
                     ('octillion', 10 ** 27),
                     ('nonillion', 10 ** 30),
                     ('decillion', 10 ** 33),
                     ('undecillion', 10 ** 36),
                     ('duodecillion', 10 ** 39),
                     ('tredecillion', 10 ** 42),
                     ('quattordecillion', 10 ** 45),
                     ('quindecillion', 10 ** 48),
                     ('sexdecillion', 10 ** 51),
                     ('septemdecillion', 10 ** 54),
                     ('octodecillion', 10 ** 57),
                     ('novemdecillion', 10 ** 60),
                     ('vigintillion', 10 ** 63),
                     ('unvigintillion', 10 ** 66),
                     ('duovigintillion', 10 ** 69),
                     ('trevigintillion', 10 ** 72),
                     ('quattorvigintillion', 10 ** 75),
                     ('quinvigintillion', 10 ** 78),
                     ('a quinvigintillion and forty-seven', 10 ** 78 + 47),
                     ('nine point nine nine nine', 9.999),
                     ('a hundred and fourteen', 114),
                     ('three thousand, one hundred and forty-seven', 3147),
                     ('forty-five hundred', 4500)]

sentence_test_data = [(
    'A hundred and twelve years, two hundred and twenty-one days, thirteen hours, and twenty-two minutes',
    '112 years, 221 days, 13 hours, and 22 minutes'),
    ('4 hours, ten days, 7 minutes, 6 seconds', '4 hours, 10 days, 7 minutes, 6 seconds')]


class TestW2N(unittest.TestCase):
    def test_word_to_num_positives(self):
        for datapoint in general_test_data:
            self.assertEqual(datapoint[1], w2n.word_to_num(datapoint[0]))

    def test_word_to_num_negatives(self):
        self.assertRaises(ValueError, w2n.word_to_num, '112-')
        self.assertRaises(ValueError, w2n.word_to_num, '-')
        self.assertRaises(ValueError, w2n.word_to_num, 'on')
        self.assertRaises(ValueError, w2n.word_to_num, 'million million')
        self.assertRaises(ValueError, w2n.word_to_num, 'three million million')
        self.assertRaises(ValueError, w2n.word_to_num, 'million four million')
        self.assertRaises(ValueError, w2n.word_to_num, 'thousand million')
        self.assertRaises(ValueError, w2n.word_to_num,
                          'one billion point two million twenty three thousand and forty nine point two three six nine')
        self.assertRaises(ValueError, w2n.word_to_num, 112)

    def test_numwords_in_sentence(self):
        for datapoint in general_test_data:
            self.assertEqual(str(datapoint[1]), w2n.numwords_in_sentence(datapoint[0]))
        for datapoint in sentence_test_data:
            self.assertEqual(datapoint[1], w2n.numwords_in_sentence(datapoint[0]))


if __name__ == '__main__':
    unittest.main()
