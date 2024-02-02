import streamlit as st

st.subheader("Git_Hub操作について")
st.text("\n")

st.text("必要最小限の設定を行う。必要最小限の設定とは、「ユーザ名」と「メール・アドレス」である。")
st.text("①ユーザ名の設定")
code_id = """
    git config --global user.name “名前”
"""
st.code(code_id, language= "python")

st.text("ユーザ名が正しく設定されたかを確かめる")
code_idck = """
    git config --global user.name
"""
st.code(code_idck, language= "python")

st.text("②メール・アドレスを設定")
code_mail = """
    git config --global user.email “メール・アドレス”
"""
st.code(code_mail, language= "python")

st.text("メール・アドレスが正しく設定されたかを確かめる")
code_mailck = """
    git config --global user.email
"""
st.code(code_mailck, language= "python")

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
    git push -u origin main
"""
st.code(code_push, language= "python")


st.text(".gitignoreの設定")
code_ignore = """
    .envなど、公開してはいけないファイルを.gitignoreに記述
"""
st.code(code_ignore, language= "python")

