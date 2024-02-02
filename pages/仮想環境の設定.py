import streamlit as st

st.subheader("仮想環境の作り方")
st.text("\n")


st.text("①仮想環境の作り方")
code_venv = """
    cd path(仮想環境を作る場所)
    python -m venv 仮想環境名
"""
st.code(code_venv, language= "python")

st.text("②仮想環境のActivate")
code_activate = """
    .\仮想環境名\Scripts\ activate
"""
st.code(code_activate, language= "python")

from PIL import Image

image_1 = Image.open(".\image\Venv\1.png")
st.image(image_1, width=500) #場合によっては大きさをwidthで設定する


st.text("③仮想環境の無効化")
code_deact = """
    deactivate
"""
st.code(code_deact, language= "python")

st.text("④仮想環境の削除")
code_reset = """
    deactivate
    python -m venv --clear 仮想環境名
"""
st.code(code_reset, language="python")

st.text("④仮想環境の削除_もう一つの方法")
code_reset = """
   Remove-Item 仮想環境名 -Recurse -Force
"""
st.code(code_reset, language="python")