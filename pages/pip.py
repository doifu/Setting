import streamlit as st

st.subheader("pipコマンド")
st.text("\n")

st.text("①バージョンを確認")
code_ver = """
    pip -V
"""
st.code(code_ver, language= "python")

st.text("②インストール済みのパッケージを一覧で確認する")
code_mv = """
    python -m pip list
"""
st.code(code_mv, language= "python")

st.text("③pipのグレードアップ")
code_gu = """
    pip install --upgrade pip
"""
st.code(code_gu, language= "python")

st.text("④アンインストール")
code_ui = """
    pip uninstall numpy
"""
st.code(code_ui, language= "python")