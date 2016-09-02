import unittest

from main import Interpreter


class TokenTestCase(unittest.TestCase):

    def test_lexer_integer(self):
        interpreter = Interpreter('2')
        token = interpreter.get_next_token()

        self.assertEqual(token.type, 'INTEGER')
        self.assertEqual(token.value, 2)

    def test_lexer_whitespace(self):
        interpreter = Interpreter('2')
        token = interpreter.get_next_token()

        self.assertEqual(token.type, 'INTEGER')
        self.assertEqual(token.value, 2)


if __name__ == '__main__':
    unittest.main()
