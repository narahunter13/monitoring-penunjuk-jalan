import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import pytz
import matplotlib.pyplot as plt


title = st.title('Monitoring Perbaikan Anomali Regsosek')

data_load_state = st.text('Loading data...')

anomali_1 = pd.read_csv("https://docs.google.com/spreadsheets/d/1JmDNVhlWL_Coj9hdKEzskY2Kz4wh_H5S5fmcZV4VVls/export?format=csv&gid=1210863346", sep=",")
anomali_2 = pd.read_csv("https://docs.google.com/spreadsheets/d/1YDZllbeRAA3cwQ_qHUMqFAdZOsnHqO4Bhjq5aZtb9A0/export?format=csv&gid=314362263", sep=",")
anomali_3 = pd.read_csv("https://docs.google.com/spreadsheets/d/1gWCbq2ruMLHKYZIfO8-x_19AJRqa-os5WgTmDFd3A0Q/export?format=csv&gid=568120335", sep=",")
anomali_4 = pd.read_csv("https://docs.google.com/spreadsheets/d/1ceai_7M5czkm2M8VouniZBaOBraHHj0pOVugm-NSwYs/export?format=csv&gid=1148218461", sep=",")
anomali_5 = pd.read_csv("https://docs.google.com/spreadsheets/d/11vl7VUScgiPO5vuFh4PcdPaRDy3LlKuT8b7e-1WpvHE/export?format=csv&gid=1353683748", sep=",")
anomali_6 = pd.read_csv("https://docs.google.com/spreadsheets/d/1E0y6-XYDA2DF7JHjKqc3Mk4VMO56ezQf0WYXyO2AU0s/export?format=csv&gid=1267789551", sep=",")
anomali_7 = pd.read_csv("https://docs.google.com/spreadsheets/d/1VzVhxv_jISRWTl9s-Qc6pfacE8NBwIJlHTD6U5EZKFQ/export?format=csv&gid=190110879", sep=",")
anomali_8 = pd.read_csv("https://docs.google.com/spreadsheets/d/1csZ6099a2Pmrjm95JCV35lEbkgl0vwvkq4ViURs9Rs8/export?format=csv&gid=88446257", sep=",")
anomali_9 = pd.read_csv("https://docs.google.com/spreadsheets/d/1Gbiuj2k_g5629CSlNPjNje3EqbcyXM67E9y1i2mQgLY/export?format=csv&gid=1850787277", sep=",")

data_load_state.text("Data pada " + str(datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%d-%m-%Y %H:%M:%M")) + " WIB")

st.subheader("Dempo Selatan")
ds_ = pd.DataFrame({
    "Jenis Anomali":[],
    "Sudah Dicek":[],
    "Belum Dicek":[],
    "Jumlah":[]
})
ds_ = ds_.astype({
    "Jenis Anomali":'string',
    "Sudah Dicek":'int32',
    "Belum Dicek":'int32',
    "Jumlah":'int32'
})
ds_.loc[len(ds_)] = ['Anomali 1', len(anomali_1.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == True) ]), len(anomali_1.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == False) ]), len(anomali_1.loc[lambda col: (col['kode_kec'] == 10)])]
ds_.loc[len(ds_)] = ['Anomali 2', len(anomali_2.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == True) ]), len(anomali_2.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == False) ]), len(anomali_2.loc[lambda col: (col['kode_kec'] == 10)])]
ds_.loc[len(ds_)] = ['Anomali 3', len(anomali_3.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == True) ]), len(anomali_3.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == False) ]), len(anomali_3.loc[lambda col: (col['kode_kec'] == 10)])]
ds_.loc[len(ds_)] = ['Anomali 4', len(anomali_4.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == True) ]), len(anomali_4.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == False) ]), len(anomali_4.loc[lambda col: (col['kode_kec'] == 10)])]
ds_.loc[len(ds_)] = ['Anomali 5', len(anomali_5.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == True) ]), len(anomali_5.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == False) ]), len(anomali_5.loc[lambda col: (col['kode_kec'] == 10)])]
ds_.loc[len(ds_)] = ['Anomali 6', len(anomali_6.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == True) ]), len(anomali_6.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == False) ]), len(anomali_6.loc[lambda col: (col['kode_kec'] == 10)])]
ds_.loc[len(ds_)] = ['Anomali 7', len(anomali_7.loc[lambda col: (col[' kode_kec'] == 10) & (col['sudah dicek'] == True) ]), len(anomali_7.loc[lambda col: (col[' kode_kec'] == 10) & (col['sudah dicek'] == False) ]), len(anomali_7.loc[lambda col: (col[' kode_kec'] == 10)])]
ds_.loc[len(ds_)] = ['Anomali 8', len(anomali_8.loc[lambda col: (col[' kode_kec'] == 10) & (col['sudah dicek'] == True) ]), len(anomali_8.loc[lambda col: (col[' kode_kec'] == 10) & (col['sudah dicek'] == False) ]), len(anomali_8.loc[lambda col: (col[' kode_kec'] == 10)])]
ds_.loc[len(ds_)] = ['Anomali 9', len(anomali_9.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == True) ]), len(anomali_9.loc[lambda col: (col['kode_kec'] == 10) & (col['sudah dicek'] == False) ]), len(anomali_9.loc[lambda col: (col['kode_kec'] == 10)])]
st.write(ds_)

st.subheader("Dempo Tengah")
dt_ = pd.DataFrame({
    "Jenis Anomali":[],
    "Sudah Dicek":[],
    "Belum Dicek":[],
    "Jumlah":[]
})
dt_ = dt_.astype({
    "Jenis Anomali":'string',
    "Sudah Dicek":'int32',
    "Belum Dicek":'int32',
    "Jumlah":'int32'
})
dt_.loc[len(dt_)] = ['Anomali 1', len(anomali_1.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == True) ]), len(anomali_1.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == False) ]), len(anomali_1.loc[lambda col: (col['kode_kec'] == 11)])]
dt_.loc[len(dt_)] = ['Anomali 2', len(anomali_2.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == True) ]), len(anomali_2.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == False) ]), len(anomali_2.loc[lambda col: (col['kode_kec'] == 11)])]
dt_.loc[len(dt_)] = ['Anomali 3', len(anomali_3.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == True) ]), len(anomali_3.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == False) ]), len(anomali_3.loc[lambda col: (col['kode_kec'] == 11)])]
dt_.loc[len(dt_)] = ['Anomali 4', len(anomali_4.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == True) ]), len(anomali_4.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == False) ]), len(anomali_4.loc[lambda col: (col['kode_kec'] == 11)])]
dt_.loc[len(dt_)] = ['Anomali 5', len(anomali_5.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == True) ]), len(anomali_5.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == False) ]), len(anomali_5.loc[lambda col: (col['kode_kec'] == 11)])]
dt_.loc[len(dt_)] = ['Anomali 6', len(anomali_6.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == True) ]), len(anomali_6.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == False) ]), len(anomali_6.loc[lambda col: (col['kode_kec'] == 11)])]
dt_.loc[len(dt_)] = ['Anomali 7', len(anomali_7.loc[lambda col: (col[' kode_kec'] == 11) & (col['sudah dicek'] == True) ]), len(anomali_7.loc[lambda col: (col[' kode_kec'] == 11) & (col['sudah dicek'] == False) ]), len(anomali_7.loc[lambda col: (col[' kode_kec'] == 11)])]
dt_.loc[len(dt_)] = ['Anomali 8', len(anomali_8.loc[lambda col: (col[' kode_kec'] == 11) & (col['sudah dicek'] == True) ]), len(anomali_8.loc[lambda col: (col[' kode_kec'] == 11) & (col['sudah dicek'] == False) ]), len(anomali_8.loc[lambda col: (col[' kode_kec'] == 11)])]
dt_.loc[len(dt_)] = ['Anomali 9', len(anomali_9.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == True) ]), len(anomali_9.loc[lambda col: (col['kode_kec'] == 11) & (col['sudah dicek'] == False) ]), len(anomali_9.loc[lambda col: (col['kode_kec'] == 11)])]
st.write(dt_)

st.subheader("Dempo Utara")
du_ = pd.DataFrame({
    "Jenis Anomali":[],
    "Sudah Dicek":[],
    "Belum Dicek":[],
    "Jumlah":[]
})
du_ = du_.astype({
    "Jenis Anomali":'string',
    "Sudah Dicek":'int32',
    "Belum Dicek":'int32',
    "Jumlah":'int32'
})
du_.loc[len(du_)] = ['Anomali 1', len(anomali_1.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == True) ]), len(anomali_1.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == False) ]), len(anomali_1.loc[lambda col: (col['kode_kec'] == 20)])]
du_.loc[len(du_)] = ['Anomali 2', len(anomali_2.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == True) ]), len(anomali_2.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == False) ]), len(anomali_2.loc[lambda col: (col['kode_kec'] == 20)])]
du_.loc[len(du_)] = ['Anomali 3', len(anomali_3.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == True) ]), len(anomali_3.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == False) ]), len(anomali_3.loc[lambda col: (col['kode_kec'] == 20)])]
du_.loc[len(du_)] = ['Anomali 4', len(anomali_4.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == True) ]), len(anomali_4.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == False) ]), len(anomali_4.loc[lambda col: (col['kode_kec'] == 20)])]
du_.loc[len(du_)] = ['Anomali 5', len(anomali_5.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == True) ]), len(anomali_5.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == False) ]), len(anomali_5.loc[lambda col: (col['kode_kec'] == 20)])]
du_.loc[len(du_)] = ['Anomali 6', len(anomali_6.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == True) ]), len(anomali_6.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == False) ]), len(anomali_6.loc[lambda col: (col['kode_kec'] == 20)])]
du_.loc[len(du_)] = ['Anomali 7', len(anomali_7.loc[lambda col: (col[' kode_kec'] == 20) & (col['sudah dicek'] == True) ]), len(anomali_7.loc[lambda col: (col[' kode_kec'] == 20) & (col['sudah dicek'] == False) ]), len(anomali_7.loc[lambda col: (col[' kode_kec'] == 20)])]
du_.loc[len(du_)] = ['Anomali 8', len(anomali_8.loc[lambda col: (col[' kode_kec'] == 20) & (col['sudah dicek'] == True) ]), len(anomali_8.loc[lambda col: (col[' kode_kec'] == 20) & (col['sudah dicek'] == False) ]), len(anomali_8.loc[lambda col: (col[' kode_kec'] == 20)])]
du_.loc[len(du_)] = ['Anomali 9', len(anomali_9.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == True) ]), len(anomali_9.loc[lambda col: (col['kode_kec'] == 20) & (col['sudah dicek'] == False) ]), len(anomali_9.loc[lambda col: (col['kode_kec'] == 20)])]
st.write(du_)

st.subheader("Pagar Alam Selatan")
pas_ = pd.DataFrame({
    "Jenis Anomali":[],
    "Sudah Dicek":[],
    "Belum Dicek":[],
    "Jumlah":[]
})
pas_ = pas_.astype({
    "Jenis Anomali":'string',
    "Sudah Dicek":'int32',
    "Belum Dicek":'int32',
    "Jumlah":'int32'
})
pas_.loc[len(pas_)] = ['Anomali 1', len(anomali_1.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == True) ]), len(anomali_1.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == False) ]), len(anomali_1.loc[lambda col: (col['kode_kec'] == 30)])]
pas_.loc[len(pas_)] = ['Anomali 2', len(anomali_2.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == True) ]), len(anomali_2.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == False) ]), len(anomali_2.loc[lambda col: (col['kode_kec'] == 30)])]
pas_.loc[len(pas_)] = ['Anomali 3', len(anomali_3.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == True) ]), len(anomali_3.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == False) ]), len(anomali_3.loc[lambda col: (col['kode_kec'] == 30)])]
pas_.loc[len(pas_)] = ['Anomali 4', len(anomali_4.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == True) ]), len(anomali_4.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == False) ]), len(anomali_4.loc[lambda col: (col['kode_kec'] == 30)])]
pas_.loc[len(pas_)] = ['Anomali 5', len(anomali_5.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == True) ]), len(anomali_5.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == False) ]), len(anomali_5.loc[lambda col: (col['kode_kec'] == 30)])]
pas_.loc[len(pas_)] = ['Anomali 6', len(anomali_6.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == True) ]), len(anomali_6.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == False) ]), len(anomali_6.loc[lambda col: (col['kode_kec'] == 30)])]
pas_.loc[len(pas_)] = ['Anomali 7', len(anomali_7.loc[lambda col: (col[' kode_kec'] == 30) & (col['sudah dicek'] == True) ]), len(anomali_7.loc[lambda col: (col[' kode_kec'] == 30) & (col['sudah dicek'] == False) ]), len(anomali_7.loc[lambda col: (col[' kode_kec'] == 30)])]
pas_.loc[len(pas_)] = ['Anomali 8', len(anomali_8.loc[lambda col: (col[' kode_kec'] == 30) & (col['sudah dicek'] == True) ]), len(anomali_8.loc[lambda col: (col[' kode_kec'] == 30) & (col['sudah dicek'] == False) ]), len(anomali_8.loc[lambda col: (col[' kode_kec'] == 30)])]
pas_.loc[len(pas_)] = ['Anomali 9', len(anomali_9.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == True) ]), len(anomali_9.loc[lambda col: (col['kode_kec'] == 30) & (col['sudah dicek'] == False) ]), len(anomali_9.loc[lambda col: (col['kode_kec'] == 30)])]
st.write(pas_)

st.subheader("Pagar Alam Utara")
pau_ = pd.DataFrame({
    "Jenis Anomali":[],
    "Sudah Dicek":[],
    "Belum Dicek":[],
    "Jumlah":[]
})
pau_ = pau_.astype({
    "Jenis Anomali":'string',
    "Sudah Dicek":'int32',
    "Belum Dicek":'int32',
    "Jumlah":'int32'
})
pau_.loc[len(pau_)] = ['Anomali 1', len(anomali_1.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == True) ]), len(anomali_1.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == False) ]), len(anomali_1.loc[lambda col: (col['kode_kec'] == 40)])]
pau_.loc[len(pau_)] = ['Anomali 2', len(anomali_2.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == True) ]), len(anomali_2.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == False) ]), len(anomali_2.loc[lambda col: (col['kode_kec'] == 40)])]
pau_.loc[len(pau_)] = ['Anomali 3', len(anomali_3.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == True) ]), len(anomali_3.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == False) ]), len(anomali_3.loc[lambda col: (col['kode_kec'] == 40)])]
pau_.loc[len(pau_)] = ['Anomali 4', len(anomali_4.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == True) ]), len(anomali_4.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == False) ]), len(anomali_4.loc[lambda col: (col['kode_kec'] == 40)])]
pau_.loc[len(pau_)] = ['Anomali 5', len(anomali_5.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == True) ]), len(anomali_5.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == False) ]), len(anomali_5.loc[lambda col: (col['kode_kec'] == 40)])]
pau_.loc[len(pau_)] = ['Anomali 6', len(anomali_6.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == True) ]), len(anomali_6.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == False) ]), len(anomali_6.loc[lambda col: (col['kode_kec'] == 40)])]
pau_.loc[len(pau_)] = ['Anomali 7', len(anomali_7.loc[lambda col: (col[' kode_kec'] == 40) & (col['sudah dicek'] == True) ]), len(anomali_7.loc[lambda col: (col[' kode_kec'] == 40) & (col['sudah dicek'] == False) ]), len(anomali_7.loc[lambda col: (col[' kode_kec'] == 40)])]
pau_.loc[len(pau_)] = ['Anomali 8', len(anomali_8.loc[lambda col: (col[' kode_kec'] == 40) & (col['sudah dicek'] == True) ]), len(anomali_8.loc[lambda col: (col[' kode_kec'] == 40) & (col['sudah dicek'] == False) ]), len(anomali_8.loc[lambda col: (col[' kode_kec'] == 40)])]
pau_.loc[len(pau_)] = ['Anomali 9', len(anomali_9.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == True) ]), len(anomali_9.loc[lambda col: (col['kode_kec'] == 40) & (col['sudah dicek'] == False) ]), len(anomali_9.loc[lambda col: (col['kode_kec'] == 40)])]
st.write(pau_)