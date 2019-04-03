#!/usr/bin/env python3
import unittest
from unittest import TestCase
import task_8 as t


class TestFib(TestCase):
    def test_params_assigned_0(self):
        self.assertFalse(t.params_assigned(0, 0))

    def test_params_assigned_negative(self):
        self.assertFalse(t.params_assigned(-55, -19))

    def test_params_assigned_str(self):
        self.assertFalse(t.params_assigned("abc", "abc"))

    def test_params_assigned(self):
        self.assertTrue(t.params_assigned(17, 60))


if __name__ == '__main__':
    unittest.main()
