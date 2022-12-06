import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import pytz

url = 'https://docs.google.com/spreadsheets/d/18UwwEd1tA7Ww9rzaKn1kLVsBWudRg_qalZwDsPaXM-k/export?format=csv&gid=540793946'
DATE_COLUMN = 'Tanggal Penyerahan'
db_kecamatan = pd.read_csv('db_kecamatan.csv', sep=";")
db_kelurahan = pd.read_csv('db_kelurahan.csv', sep=";")
def load_data(csv):
    data = pd.read_csv(csv).loc[:, ["Kecamatan", "Kelurahan", "SLS", "Nama Lengkap Penunjuk Jalan", "Tanggal Penyerahan"]]
    data["Tanggal Penyerahan"] = pd.to_datetime(data["Tanggal Penyerahan"], format="%m/%d/%Y")
    data["Tanggal Penyerahan"] = data["Tanggal Penyerahan"].dt.strftime("%d-%m-%Y")
    data["Kecamatan"] = data["Kecamatan"].str.upper()
    data["Kelurahan"] = data["Kelurahan"].str.upper()
    data["Nama Lengkap Penunjuk Jalan"] = data["Nama Lengkap Penunjuk Jalan"].str.upper()
    data.index = data.index + 1
    return data


title = st.title('Monitoring Pembayaran Honor Penunjuk Jalan: ...')

data_load_state = st.text('Loading data...')

df = load_data(url)
title.title('Monitoring Pembayaran Honor Penunjuk Jalan: ' + str("%.2f" % (len(df)/478 * 100)) + "% ")

st.write(str(len(df)) + " dari 478 SLS")

data_load_state.text('Last Updated: ' + str(datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%d-%m-%Y %H:%M:%M")) + "WIB")

OPTION = st.selectbox('Pilih Kecamatan', ["SEMUA KECAMATAN", "DEMPO SELATAN", "DEMPO TENGAH", "DEMPO UTARA", "PAGAR ALAM SELATAN", "PAGAR ALAM UTARA"])

st.dataframe(df[df["Kecamatan"] == OPTION] if (OPTION != "SEMUA KECAMATAN") else df.sort_values('Kecamatan'))

df_kecamatan = df
df_kecamatan["Realisasi"] = df.groupby('Kecamatan')["Kecamatan"].transform('count').astype('int64')
df_kecamatan = df_kecamatan.drop_duplicates('Kecamatan')
df_kecamatan = df_kecamatan.loc[:, ["Kecamatan", "Realisasi"]]

df_kecamatan = db_kecamatan.set_index('Kecamatan').join(df_kecamatan.set_index('Kecamatan')).reset_index(names='Kecamatan')
df_kecamatan["Progres"] = df_kecamatan["Realisasi"]/df_kecamatan["Jumlah SLS"] * 100
df_kecamatan = df_kecamatan.fillna(0)
df_kecamatan["Progres"] = df_kecamatan["Progres"].map('{:,.2f}%'.format)
df_kecamatan['Realisasi'] = df_kecamatan['Realisasi'].astype('int64')

st.title('Realisasi Per Kecamatan')
st.dataframe(df_kecamatan)


df_kelurahan = df
df_kelurahan["Realisasi"] = df.groupby(['Kecamatan', 'Kelurahan'])["Kelurahan"].transform('count')
df_kelurahan = df_kelurahan.drop_duplicates('Kelurahan')
df_kelurahan = df_kelurahan.loc[:, ["Kelurahan", "Realisasi"]]

df_kelurahan = db_kelurahan.set_index('Kelurahan').join(df_kelurahan.set_index('Kelurahan')).reset_index(names='Kelurahan')
df_kelurahan = df_kelurahan.fillna(0)
df_kelurahan["Progres"] = df_kelurahan["Realisasi"]/df_kelurahan["Jumlah SLS"] * 100
df_kelurahan["Progres"] = df_kelurahan["Progres"].map('{:,.2f}%'.format)
df_kelurahan['Realisasi'] = df_kelurahan['Realisasi'].astype('int64')
df_kelurahan = df_kelurahan.loc[:, ["Kecamatan", "Kelurahan", "Jumlah SLS", "Realisasi", "Progres"]]

st.title('Realisasi Per Kelurahan')
KECAMATAN_SELECT = st.selectbox('Pilih', ["SEMUA KECAMATAN", "DEMPO SELATAN", "DEMPO TENGAH", "DEMPO UTARA", "PAGAR ALAM SELATAN", "PAGAR ALAM UTARA"])
st.dataframe(df_kelurahan[df_kelurahan["Kecamatan"] == KECAMATAN_SELECT] if (KECAMATAN_SELECT != "SEMUA KECAMATAN") else df_kelurahan.sort_values('Kecamatan'))