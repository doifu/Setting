import streamlit as st
from pytesseract import pytesseract
from PIL import Image


with st.form(key = "file_form"):
    upload_file = st.file_uploader("ファイルアップロード", type='png')
    submit_btn = st.form_submit_button("OK")
    cancel_btn = st.form_submit_button("キャンセル")

def read_picture(file):
    img = Image.open(file, "r")
    
    # tesseractコマンドのインストールパス
    pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    
    # 文字列として出力できる。
    ocr_result = pytesseract.image_to_string(img, lang="eng+jpn")

    return ocr_result
    
if submit_btn:
    st.text("元の画像")
    image_1 = Image.open(upload_file)
    st.image(image_1, width=600) #場合によっては大きさをwidthで設定する
    
    st.text(" \n\n読み込んだ結果")
    amino_acid = read_picture(upload_file)
    st.text(amino_acid)
    
    #アミノ酸の分析をする。
    #1 アミノ酸数をカウント
    num = len(amino_acid)
    st.text(f"カウント数{num}")
    
    #2 システイン数をカウント
    cys_num =amino_acid.count("C")
    st.text(cys_num)
    