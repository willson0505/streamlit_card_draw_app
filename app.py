
import streamlit as st
import pandas as pd
import random
from PIL import Image

st.set_page_config(layout="wide")
st.title("抽牌工具")

# 載入資料與圖片
df = pd.read_csv("cards/card_data.csv")
bg_image = Image.open("card_layout.jpg")

positions = [
    "事情的成因", "現在的狀況", "當前的功課", "最好的未來", "集體意識的收穫"
]
drawn_cards = []

if "cards" not in st.session_state:
    st.session_state.cards = []

st.image(bg_image, caption="抽牌陣列")

if st.button("抽一張牌", disabled=len(st.session_state.cards) >= 5):
    remaining = df[~df["主題"].isin([card["主題"] for card in st.session_state.cards])]
    if not remaining.empty:
        selected = remaining.sample(1).iloc[0]
        st.session_state.cards.append(selected.to_dict())

st.subheader("抽到的牌：")
for i, card in enumerate(st.session_state.cards):
    st.markdown(f"**{positions[i]}**")
    st.write(f"主題：{card['主題']}")
    st.write(f"大局：{card['大局']}")
    st.write(f"個體：{card['個體']}")
    st.write("---")
