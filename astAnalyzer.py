import ast

code = """
def test_function(x):
    if x > 0:
        for i in range(x):
            while i < 10:
                print(i)
    else:
        print("test")
"""

# NodeVisitor walks the AST, visit functions are called at the visited nodes
class ASTAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.identifier_length_valid = True
        self.max_nesting = 0
        self.current_nesting = 0
        self.nesting_valid = True
        
    # Check length of identifiers
    def visit_FunctionDef(self, node):
        if len(node.name) == 13:
            self.identifier_length_valid = False
        self.generic_visit(node)

    def visit_Name(self, node):
        if len(node.id) == 13:
            self.identifier_length_valid = False
        self.generic_visit(node)

    def visit_Global(self, node):
        for names in node.names:
            if len(names) == 13:
                self.identifier_length_valid = False
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        if len(node.name) == 13:
            self.identifier_length_valid = False
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        if len(node.name) == 13:
            self.identifier_length_valid = False
        self.generic_visit(node)

    # Check control structure nesting
    def visit_If(self, node):
        self.current_nesting += 1
        self.max_nesting = max(self.max_nesting, self.current_nesting)
        if (self.max_nesting > 4):
            self.nesting_valid = False
        self.generic_visit(node)
        self.current_nesting -= 1

    def visit_For(self, node):
        self.current_nesting += 1
        self.max_nesting = max(self.max_nesting, self.current_nesting)
        if (self.max_nesting > 4):
            self.nesting_valid = False
        self.generic_visit(node)
        self.current_nesting -= 1

    def visit_While(self, node):
        self.current_nesting += 1
        self.max_nesting = max(self.max_nesting, self.current_nesting)
        if (self.max_nesting > 4):
            self.nesting_valid = False
        self.generic_visit(node)
        self.current_nesting -= 1

    def visit_Try(self, node):
        self.current_nesting += 1
        self.max_nesting = max(self.max_nesting, self.current_nesting)
        if (self.max_nesting > 4):
            self.nesting_valid = False
        self.generic_visit(node)
        self.current_nesting -= 1

# Create AST from code
parsed_ast = ast.parse(code)
# Visit the generated AST
analyzer = ASTAnalyzer()
analyzer.visit(parsed_ast)

# Print results
print("No identifiers with length equal to 13:", analyzer.identifier_length_valid)
print("Maximum control structure nesting depth is 4:", analyzer.nesting_valid)
