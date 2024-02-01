import tabula
import streamlit as st

with st.form(key = "file_form"):
    upload_file = st.file_uploader("ファイルアップロード", type='pdf')
    submit_btn = st.form_submit_button("OK")
    cancel_btn = st.form_submit_button("キャンセル")


if submit_btn:
    st.text("元の画像")

    # PDFファイル
    pdf_file = upload_file 
# テキストテーブル取得
    df = tabula.read_pdf(pdf_file,       # PDFファイル
                        pages='1',    # 抽出ページ
                        guess=True,     # 分析部分の変更有無
                        area="entire",  # ページの部分指定
                        lattice=True,  # 格子区切りがPDF内にある場合の対応
                        stream=False,   # ストリームモード
                        password=None,  # パスワード
                        )
    
    print(df)
    
    st.text(" \n\n読み込んだ結果")
    st.text(df)
    