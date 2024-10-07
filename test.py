import ast
import unittest
import astAnalyzer

class TestASTAnalyzer(unittest.TestCase):
    # Call this in every test to get the analyzer's results
    def get_results(self, code):
        self.analyzer = astAnalyzer.ASTAnalyzer()
        parsed_ast = ast.parse(code)
        self.analyzer.visit(parsed_ast)
        return self.analyzer.identifier_length_valid, self.analyzer.max_nesting

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
        identifier_length_valid, max_nesting = self.get_results(code)
        self.assertTrue(identifier_length_valid) # test_function
        self.assertEqual(max_nesting, 3) # if, for, while

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
        identifier_length_valid, max_nesting = self.get_results(code)
        self.assertFalse(identifier_length_valid) # qwertyuiopasd
        self.assertEqual(max_nesting, 4) # if, for, while, try

    
if __name__ == "__main__":
    unittest.main()
