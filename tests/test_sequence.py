from unittest import TestCase
import task_7 as t


class TestSequence(TestCase):

    def test_get(self):
        self.assertEqual(list(t.Sequence(8).get()), list((x for x in [1,2])))

    def test_print_sequence(self):
        self.assertEqual(t.Sequence(8).print_sequence(), None)

    def test_params_assigned_0(self):
        self.assertFalse(t.params_assigned(0))

    def test_params_assigned_negative(self):
        self.assertFalse(t.params_assigned(-5))

    def test_params_assigned_str(self):
        self.assertFalse(t.params_assigned("abc"))

    def test_params_assigned(self):
        self.assertTrue(t.params_assigned(17))

if __name__ == '__main__' :
    unittest.main()