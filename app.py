import streamlit as st
import ast

from visitor import FeatureExtractor
from ir_generator import generate_ir
from analysis import analyze_ir
from nlp_engine import generate_nlp_comment
from integrator import insert_comments_into_code

st.title("Code Comment Generator")

code = st.text_area("Paste your Python code here")

if st.button("Generate Comments"):

    if code.strip() == "":
        st.warning("Please enter code")
    else:
        tree = ast.parse(code)

        extractor = FeatureExtractor()
        extractor.visit(tree)

        ir_list = [generate_ir(f) for f in extractor.functions]
        analysis_results = [analyze_ir(ir) for ir in ir_list]

        comments = []
        for ir, analysis in zip(ir_list, analysis_results):
            comments.append(generate_nlp_comment(ir, analysis))

        final_code = insert_comments_into_code(code, comments)

        st.subheader("Generated Comments")
        for c in comments:
            st.write(c)

        st.subheader("Commented Code")
        st.code(final_code, language='python')