import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 Borsa İstanbul Prim Adayları")

tickers = ['GARAN.IS', 'KCHOL.IS', 'ASELS.IS', 'SASA.IS', 'BIMAS.IS']
selected = st.selectbox("Hisse Seçin:", tickers)

data = yf.download(selected, period="7d", interval="1h")

st.write(f"**{selected} Son 7 Günlük Saatlik Kapanış Fiyatları**")
st.line_chart(data['Close'])
