# comment_generator
-Python Code Comment Generator

A rule-based Python code comment generation tool built using Python's Abstract Syntax Tree (AST) and Natural Language Processing (NLP) techniques. The application analyzes the structure of Python code, identifies language constructs, and generates meaningful comments based on predefined rules. The generated comments are inserted as function docstrings to improve code readability and documentation.

Features:
->Parse Python source code using the built-in AST module.
->Analyze functions, return statements, arithmetic expressions, conditional statements, and imported modules.
->Generate descriptive comments using a rule-based approach.
->Insert generated comments as Python docstrings.
->Interactive web interface built with Streamlit.
->Copy the commented code directly from the interface.

Tech Stack:
->Python
->AST (Abstract Syntax Tree)
->NLP (Rule-based text generation)
->Streamlit

How It Works:
->Paste Python code into the editor.
->The application parses the code using Python's AST module.
->AST nodes are analyzed to identify programming constructs such as:
->Function definitions
->Return statements
->Arithmetic operations
->Conditional statements
->Import statements
->Rule-based NLP templates generate human-readable descriptions.
->The generated description is inserted as a function docstring and displayed alongside the modified code.
Test case 1:
Input:
def add(a, b):
    return a + b
Generated Comment:
This function computes the sum of the inputs and returns a + b.
Output:
def add(a, b):
    """This function computes the sum of the inputs and returns a + b."""
    return a + b
Test case 2:
Input:
import math

def calc(x):
    return math.sqrt(x)
Generated Comment
This function computes the square root of the input using the math module.
Input:
def complex(a, b):
    result = (a + b) * (a % b)
    if result > 10:
        return result ** 2
    return result
Generated Comment
This function performs arithmetic operations on the inputs, evaluates a condition, and returns the computed result.

Author
Snigdha Parasa
