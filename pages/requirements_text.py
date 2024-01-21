import streamlit as st

st.subheader("Reqirements.txtの使い方")
st.text("\n")


st.text("まとめてインストール")
code_install = """
    pip install -r requirements.txt
"""
st.code(code_install, language= "python")

st.text("ライブラリの書き出し")
code_out = """
    $ pip freeze > requirements.txt
"""
st.code(code_out, language= "python")
