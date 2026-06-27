#import ast
#from visitor import FeatureExtractor
#from comment_engine import generate_comment

# Read input code
#code = open("visitor_test.py").read()

# Parse AST
#tree = ast.parse(code)

# Extract features
#extractor = FeatureExtractor()
#extractor.visit(tree)

#print("===== Extracted AST Features =====")

#for feature in extractor.functions:
 #   print(feature)

#print("\n===== Generated Comments =====")

#for feature in extractor.functions:
 #   comment = generate_comment(feature)
  #  print(comment)

    #week 7 deliverables
#import ast
#from visitor import FeatureExtractor
#from ir_generator import generate_ir
#from analysis import analyze_ir
#from comment_engine import generate_comment
#from nlp_engine import generate_nlp_comment

#code = open("input_code.py").read()

#tree = ast.parse(code)

#extractor = FeatureExtractor()
#extractor.visit(tree)

#print("===== Extracted AST Features =====")

#for feature in extractor.functions:
 #   print(feature)

#print("\n===== Intermediate Representation =====")

#ir_list = []

#for feature in extractor.functions:
 #   ir = generate_ir(feature)
  #  ir_list.append(ir)
   # print(ir)

#print("\n===== Analysis Results =====")

#analysis_results = []

#for ir in ir_list:
 #   result = analyze_ir(ir)
  #  analysis_results.append(result)
   # print(result)

#print("\n===== Generated Comments =====")

#for ir, analysis in zip(ir_list, analysis_results):
 #   print(generate_comment(ir, analysis))

#print("\n===== NLP Enhanced Comments =====")

#for ir, analysis in zip(ir_list, analysis_results):
 #   print(generate_nlp_comment(ir, analysis))
 # week10 deliverables
import ast
import sys

from visitor import FeatureExtractor
from ir_generator import generate_ir
from analysis import analyze_ir
from nlp_engine import generate_nlp_comment
from integrator import insert_comments_into_code


# 🔹 Step 1: Take input file
file = sys.argv[1] if len(sys.argv) > 1 else "input_code.py"

with open(file, "r") as f:
    code = f.read()


# 🔹 Step 2: Parse AST
tree = ast.parse(code)


# 🔹 Step 3: Extract features
extractor = FeatureExtractor()
extractor.visit(tree)

print("===== Extracted AST Features =====")
for feature in extractor.functions:
    print(feature)


# 🔹 Step 4: Generate IR
ir_list = []
for feature in extractor.functions:
    ir = generate_ir(feature)
    ir_list.append(ir)

print("\n===== Intermediate Representation =====")
for ir in ir_list:
    print(ir)


# 🔹 Step 5: Analyze IR
analysis_results = []
for ir in ir_list:
    result = analyze_ir(ir)
    analysis_results.append(result)

print("\n===== Analysis Results =====")
for res in analysis_results:
    print(res)


# 🔹 Step 6: Generate basic comments
print("\n===== Generated Comments =====")
for ir, analysis in zip(ir_list, analysis_results):
    print(f"The function '{ir['name']}' {', '.join(analysis)} and returns {ir['return']}.")


# 🔹 Step 7: Generate NLP comments
comments = []

print("\n===== NLP Enhanced Comments =====")
for ir, analysis in zip(ir_list, analysis_results):
    comment = generate_nlp_comment(ir, analysis)
    comments.append(comment)
    print(comment)


# 🔹 Step 8: Insert comments into code
final_code = insert_comments_into_code(code, comments)

print("\n===== FINAL COMMENTED CODE =====\n")
print(final_code)


# 🔹 Step 9: Save output to file
with open("output.py", "w") as f:
    f.write(final_code)

print("\n✅ Commented code saved to output.py")