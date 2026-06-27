
def add(a, b):
    return a + bcode = open("test.py").read()
tree = ast.parse(code)

extractor = FeatureExtractor()
extractor.visit(tree)

print(extractor.features)