from unittest import TestCase
import task_7 as t


class TestSequence(TestCase):

    def test_get(self):
        self.assertEqual(list(t.Sequence(8).get()), list((x for x in [1,2])))

    def test_print_sequence(self):
        self.assertEqual(t.Sequence(8).print_sequence(), None)

    def test_params_are_valid_0(self):
        self.assertFalse(t.params_are_valid(0))

    def test_params_are_valid_negative(self):
        self.assertFalse(t.params_are_valid(-5))

    def test_params_are_valid_str(self):
        self.assertFalse(t.params_are_valid("abc"))

    def test_params_are_valid(self):
        self.assertTrue(t.params_are_valid(17))


if __name__ == '__main__':
    unittest.main()