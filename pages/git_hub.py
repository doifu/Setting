import streamlit as st

st.subheader("Git_Hub操作について")
st.text("\n")

st.text("＃ローカルに空のリポジトリを作成。最初だけこれをする")
st.text("目的のフォルダに移動してから")
code_init = """
    git init
"""
st.code(code_init, language= "python")

st.text("①リスト予約")
code_add = """
    git add -A #全リスト予約
"""
st.code(code_add, language= "python")

st.text("②Status確認")
code_status = """
    git status
"""
st.code(code_status, language= "python")

st.text("③Commit")
code_commit = """
    git commit -m "メモ内容"
"""
st.code(code_commit, language= "python")

st.text("④ここは不明")
code_remote = """
    git remote add oridin https://github.com/USER_ID/Ripositori_name
"""
st.code(code_remote, language= "python")

st.text("⑤push")
code_push = """
    git push -u oridin main
"""
st.code(code_push, language= "python")
