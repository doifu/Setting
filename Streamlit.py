import streamlit as st

st.subheader("①フォントサイズの設定")

code_font = """
st.title("title")
st.subheader("subheader")
st.text("text")
st.caption("caption")
"""
st.code(code_font, language= "python")

st.text("下記が例")

st.title("title")
st.subheader("subheader")
st.text("text")
st.caption("caption")

st.subheader("②画像、動画の取り込み")

st.text("①画像の取り込み")
code_image = """
important PIL import Image

image_1 = Image.open("画像ファイルのpath")
st.image(image_1, width=200) #場合によっては大きさをwidthで設定する
"""
st.code(code_image, language= "python")

st.text("②動画の取り込み")
code_video = """
important PIL import Image

video_file = open("動画ファイルのpath", "rb")
video_bytes = video_file.read()
st. video(video_bytes)
"""
st.code(code_video, language="python")

