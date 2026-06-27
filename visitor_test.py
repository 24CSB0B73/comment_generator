#import ast

#code = '''
#def add(a, b):
 #   return a + b

#def multiply(x, y):
 #   return x * y
#'''


#tree = ast.parse(code)   #week 5 and 6

#class MyVisitor(ast.NodeVisitor):
 #   def visit_FunctionDef(self, node):
  #      print("Function found:", node.name)
   #     self.generic_visit(node)

#visitor = MyVisitor()
#visitor.visit(tree)
#updated for week 7
def add(a, b):
    return a + b


def process_numbers(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total
