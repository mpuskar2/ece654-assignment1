import ast
import unittest
import astAnalyzer

class TestASTAnalyzer(unittest.TestCase):
    # Call this in every test to get the analyzer's results
    def get_results(self, code):
        self.analyzer = astAnalyzer.ASTAnalyzer()
        parsed_ast = ast.parse(code)
        self.analyzer.visit(parsed_ast)
        return self.analyzer.identifier_length_valid, self.analyzer.max_nesting, self.analyzer.nesting_valid

    # Expected: True, True
    def test_1(self):
        code = """
def atest_function(x):
    if x > 0:
        for i in range(x):
            while i < 10:
                print(i)
    else:
        print("test")
"""
        identifier_length_valid, max_nesting, nesting_valid = self.get_results(code)
        self.assertTrue(identifier_length_valid) # test_function
        self.assertEqual(max_nesting, 3) # if, for, while
        self.assertTrue(nesting_valid)

    # Expected: False, True
    def test_2(self):
        code = """
def other_function(x):
    global qwertyuiopasd
    asd
    if x > 0:
        for i in range(x):
            while i < 10:
                try:
                    print(i)
                except Exception:
                    print("hello")
    else:
        print("hi")
"""
        identifier_length_valid, max_nesting, nesting_valid = self.get_results(code)
        self.assertFalse(identifier_length_valid) # qwertyuiopasd
        self.assertEqual(max_nesting, 4) # if, for, while, try
        self.assertTrue(nesting_valid)

    # Expected: False, True
    def test_3(self):
        code = """
async def test_function(x):
    asd
    if x > 0:
        print(x)
    else:
        print("hi")
"""
        identifier_length_valid, max_nesting, nesting_valid = self.get_results(code)
        self.assertFalse(identifier_length_valid) # test_function
        self.assertEqual(max_nesting, 1) # if
        self.assertTrue(nesting_valid)

    # Expected: False, True
    def test_4(self):
        code = """
class newClass12345(abc):
    def function(x):
        print("hello")
"""
        identifier_length_valid, max_nesting, nesting_valid = self.get_results(code)
        self.assertFalse(identifier_length_valid) # newClass12345
        self.assertEqual(max_nesting, 0)
        self.assertTrue(nesting_valid)

    # Expected: True, False
    def test_5(self):
        code = """
def other_function(x):
    global qwerty
    asd
    if x > 0:
        for i in range(x):
            while i < 10:
                for k in range(10):
                    try:
                        print(i)
                    except Exception:
                        print("hello")
    else:
        print("hi")
"""
        identifier_length_valid, max_nesting, nesting_valid = self.get_results(code)
        self.assertFalse(identifier_length_valid)
        self.assertEqual(max_nesting, 5) # if, for, while, for, try
        self.assertFalse(nesting_valid)

    # Expected: False, False
    def test_5(self):
        code = """
def other_function(xxxxxxxxxxxxx):
    global qwerty
    asd
    if xxxxxxxxxxxxx > 0:
        for i in range(xxxxxxxxxxxxx):
            while i < 10:
                for k in range(10):
                    try:
                        print(i)
                    except Exception:
                        print("hello")
    else:
        print("hi")
"""
        identifier_length_valid, max_nesting, nesting_valid = self.get_results(code)
        self.assertFalse(identifier_length_valid) # xxxxxxxxxxxxx
        self.assertEqual(max_nesting, 5) # if, for, while, for, try
        self.assertFalse(nesting_valid)
    
if __name__ == "__main__":
    unittest.main()
