#!/usr/bin/env python3
import unittest

if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('../tests', pattern='*.py')
    unittest.TextTestRunner().run(all_tests)