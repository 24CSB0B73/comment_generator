#import ast

#class FeatureExtractor(ast.NodeVisitor):
 #   def __init__(self):
  #      self.features = {
   #         "function_name": None,
    #        "parameters": [],
     #       "has_loop": False,
      #      "has_condition": False,
       #     "operations": [],
        #    "returns": None
        #}

#    def visit_FunctionDef(self, node):
 #       self.features["function_name"] = node.name
  #      self.features["parameters"] = [arg.arg for arg in node.args.args]
   #     self.generic_visit(node)

    #def visit_For(self, node):
     #   self.features["has_loop"] = True
      #  self.generic_visit(node)

#    def visit_While(self, node):
 #       self.features["has_loop"] = True
  #      self.generic_visit(node)

#    def visit_If(self, node):
 #       self.features["has_condition"] = True
  #      self.generic_visit(node)

   # def visit_Return(self, node):
    #    self.features["returns"] = ast.dump(node.value)
#        self.generic_visit(node)
#
 #   def visit_BinOp(self, node):
  #      if isinstance(node.op, ast.Add):
   #         self.features["operations"].append("addition")
    #    elif isinstance(node.op, ast.Sub):
     #       self.features["operations"].append("subtraction")
      #  elif isinstance(node.op, ast.Mult):
       #     self.features["operations"].append("multiplication")
        #elif isinstance(node.op, ast.Div):
         #   self.features["operations"].append("division")
        #self.generic_visit(node)


#def generate_comment(features):
 #   name = features["function_name"]
  #  params = features["parameters"]

#   comment = f"This function '{name}' "
#
#   if features["operations"]:
 #       op = features["operations"][0]
  #      comment += f"performs {op} "

   # if features["has_loop"]:
    #    comment += "using iteration "

    #if features["has_condition"]:
     #   comment += "with conditional logic "

    #if params:
     #   comment += f"on parameters {', '.join(params)}."

    #return comment


#if __name__ == "__main__":
 #   code = open("visitor_test.py").read()
  #  tree = ast.parse(code)

   # extractor = FeatureExtractor()
    #extractor.visit(tree)

    #print("Extracted Features:")
    #print(extractor.features)

    #print("\nGenerated Comment:")
    #print(generate_comment(extractor.features)) # week 7  is updated again

#import ast

#class FeatureExtractor(ast.NodeVisitor):

 #   def __init__(self):
  #      self.functions = [] # this is new to implement ruke based approach in week 7

   # def visit_FunctionDef(self, node):

    #    feature = {
     #       "name": node.name,
      #      "parameters": [arg.arg for arg in node.args.args],
       #     "has_loop": False,
        #    "has_condition": False,
         #   "operations": [],
          #  "return_value": None
        #}

        #for child in ast.walk(node):

         #   if isinstance(child, ast.For) or isinstance(child, ast.While):
          #      feature["has_loop"] = True

            #if isinstance(child, ast.If):
             #   feature["has_condition"] = True

            #if isinstance(child, ast.BinOp):

             #   if isinstance(child.op, ast.Add):
              #      feature["operations"].append("addition")

               # if isinstance(child.op, ast.Mult):
                #    feature["operations"].append("multiplication")

                #if isinstance(child.op, ast.Sub):
                 #  feature["operations"].append("subtraction")

                #if isinstance(child.op, ast.Div):
                 #   feature["operations"].append("division")

            #if isinstance(child, ast.Return):
             #   feature["return_value"] = ast.unparse(child.value)

        #self.functions.append(feature)

        #self.generic_visit(node)
#import ast

#class FeatureExtractor(ast.NodeVisitor):

    #def __init__(self):
     #   self.functions = []

    #def visit_FunctionDef(self, node):

        #feature = {
       #     "name": node.name,
      #      "parameters": [arg.arg for arg in node.args.args],
     #       "has_loop": False,
    #        "has_condition": False,
   #         "operations": set(),   # using set to avoid duplicates
  #          "return_value": None
 #       }

#        for child in ast.walk(node):

            # Loop detection
   #         if isinstance(child, (ast.For, ast.While)):
  #              feature["has_loop"] = True

            # Condition detection
 #           if isinstance(child, (ast.If, ast.Compare)):
#                feature["has_condition"] = True

            # Operation detection
         #   if isinstance(child, ast.BinOp):

        #        if isinstance(child.op, ast.Add):
       #             feature["operations"].add("addition")

      #          elif isinstance(child.op, ast.Sub):
     #               feature["operations"].add("subtraction")

    #            elif isinstance(child.op, ast.Mult):
   #                 feature["operations"].add("multiplication")

  #              elif isinstance(child.op, ast.Div):
 #                   feature["operations"].add("division")
#
  #              elif isinstance(child.op, ast.Mod):
 #                   feature["operations"].add("modulus")
#
 #               elif isinstance(child.op, ast.Pow):
#                    feature["operations"].add("exponentiation")

              #  elif isinstance(child.op, ast.FloorDiv):
             #       feature["operations"].add("floor division")

            # Function call detection
            #if isinstance(child, ast.Call):
           #     feature["operations"].add("function call")

            # Return detection
          #  if isinstance(child, ast.Return):
         #       feature["return_value"] = ast.unparse(child.value) if child.value else None

        # Convert set → list
        #feature["operations"] = list(feature["operations"])

        #self.functions.append(feature)

        #self.generic_visit(node)

#week 10 deliverables
import ast

class FeatureExtractor(ast.NodeVisitor):

    def __init__(self):
        self.functions = []

    def visit_FunctionDef(self, node):

        feature = {
            "name": node.name,
            "parameters": [arg.arg for arg in node.args.args],
            "has_loop": False,
            "has_condition": False,
            "operations": set(),
            "return_value": None
        }

        for child in ast.walk(node):

            # 🔹 Loop detection
            if isinstance(child, (ast.For, ast.While)):
                feature["has_loop"] = True

            # 🔹 Condition detection
            if isinstance(child, (ast.If, ast.Compare)):
                feature["has_condition"] = True

            # 🔹 Operations
            if isinstance(child, ast.BinOp):

                if isinstance(child.op, ast.Add):
                    feature["operations"].add("addition")

                elif isinstance(child.op, ast.Sub):
                    feature["operations"].add("subtraction")

                elif isinstance(child.op, ast.Mult):
                    feature["operations"].add("multiplication")

                elif isinstance(child.op, ast.Div):
                    feature["operations"].add("division")

                elif isinstance(child.op, ast.Mod):
                    feature["operations"].add("modulus")

                elif isinstance(child.op, ast.Pow):
                    feature["operations"].add("exponentiation")

                elif isinstance(child.op, ast.FloorDiv):
                    feature["operations"].add("floor division")

            # 🔹 Function calls
            if isinstance(child, ast.Call):
                feature["operations"].add("function call")

            # 🔹 Return detection
            if isinstance(child, ast.Return):
                feature["return_value"] = ast.unparse(child.value) if child.value else None

        # 🔹 Convert set → list
        feature["operations"] = list(feature["operations"])

        self.functions.append(feature)

        self.generic_visit(node)

    # 🔥 NEW: GLOBAL IMPORT DETECTION
    def visit_Import(self, node):
        for name in node.names:
            self._add_import_usage(f"uses {name.name} module")

    def visit_ImportFrom(self, node):
        for name in node.names:
            self._add_import_usage(f"uses {name.name} from {node.module}")

    # 🔹 Helper to attach import info to ALL functions
    def _add_import_usage(self, text):
        for func in self.functions:
            func["operations"].append(text)
        