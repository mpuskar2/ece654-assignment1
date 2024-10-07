import ast
import unittest
import astAnalyzer

code = """
def atest_function(x):
    if x > 0:
        for i in range(x):
            while i < 10:
                print(i)
    else:
        print("test")
"""

class TestASTAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = astAnalyzer.ASTAnalyzer()
        self.parsed_ast = ast.parse(code)

    def test_identifier_length_13(self):
        self.analyzer.visit(self.parsed_ast)
        self.assertTrue(self.analyzer.identifier_length_valid)

    def test_max_nesting_depth(self):
        self.analyzer.visit(self.parsed_ast)
        self.assertEqual(self.analyzer.max_nesting, 4)

if __name__ == "__main__":
    unittest.main()
