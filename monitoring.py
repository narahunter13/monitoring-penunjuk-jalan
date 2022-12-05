import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

url = 'https://docs.google.com/spreadsheets/d/18UwwEd1tA7Ww9rzaKn1kLVsBWudRg_qalZwDsPaXM-k/export?format=csv&gid=540793946'
DATE_COLUMN = 'Tanggal Penyerahan'
def load_data(csv):
    data = pd.read_csv(csv).loc[:, ["Kecamatan", "Kelurahan", "SLS", "Nama Lengkap Penunjuk Jalan", "Tanggal Penyerahan"]]
    data["Tanggal Penyerahan"] = pd.to_datetime(data["Tanggal Penyerahan"], format="%m/%d/%Y")
    data["Tanggal Penyerahan"] = data["Tanggal Penyerahan"].dt.strftime("%d-%m-%Y")
    data["Kecamatan"] = data["Kecamatan"].str.upper()
    data.index = data.index + 1
    return data


title = st.title('Monitoring Pembayaran Honor Penunjuk Jalan: ...')

data_load_state = st.text('Loading data...')

df = load_data(url)
title.title('Monitoring Pembayaran Honor Penunjuk Jalan: ' + str("%.2f" % (len(df)/478 * 100)) + "% ")

st.write(str(len(df)) + " dari 478 SLS")

data_load_state.text('Last Updated: ' + str(datetime.now().strftime("%d-%m-%Y %H:%M:%M")))

OPTION = st.selectbox('Pilih Kecamatan', ["SEMUA KECAMATAN", "DEMPO SELATAN", "DEMPO TENGAH", "DEMPO UTARA", "PAGAR ALAM SELATAN", "PAGAR ALAM UTARA"])

st.dataframe(df[df["Kecamatan"] == OPTION] if (OPTION != "SEMUA KECAMATAN") else df.sort_values('Kecamatan'))