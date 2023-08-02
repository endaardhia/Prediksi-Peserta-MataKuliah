import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

st.markdown("<h2 style='text-align: center;'>Model Prediksi </h2>",unsafe_allow_html=True)
st.sidebar.success("Select A Page Above")

from datetime import date
tanggal = date.today()
ambiltahun = tanggal.year
tahun = st.number_input('Masukkan tahun prediksi', min_value=0, value=ambiltahun)
mhs_default = st.number_input('Masukkan Kapasitas Mahasiswa PerKelas', min_value=0)

uploaded_model = st.file_uploader("Pilih file csv")
if uploaded_model is not None:
    modelupload = pd.read_csv(uploaded_model)
    #modelupload.style.highlight_null(null_color='red')
    st.write("DataFrame yang di unggah ")
    string = modelupload.sort_values(by=["tahun_akademik","nama_matkul"], ascending=True)
    string['tahun_akademik'] = modelupload['tahun_akademik'].astype(str)
    st.write(string)

    md = modelupload

    #tambah quarter
    md['qtr1'] = md.index+1
    md['qtr2'] = md['qtr1']**2
    md['qtr3'] = md['qtr1']**3
    md['qtr4'] = md['qtr1']**4

    md['ktgr'] = md['id_matkul'].astype(str)
    md = pd.get_dummies(md, prefix = ['ktgr'], columns=['ktgr'], drop_first=True)

    #PEMODELAN

    a=tahun
    training = md.loc[md['tahun_akademik'] != tahun]
    testing = md.loc[md['tahun_akademik'] == tahun]

    training = training.drop(columns=['tahun_akademik','id_matkul','nama_matkul'])
    testing = testing.drop(columns=['tahun_akademik','id_matkul','nama_matkul'])

    #variabel x dan y
    y_train = training['jumlah_mhs']
    x_train = training.drop(columns=['jumlah_mhs'])

    y_test = testing['jumlah_mhs']
    x_test = testing.drop(columns=['jumlah_mhs'])


    model = LinearRegression()
    model.fit(x_train, y_train)
    LinearRegression()

    #tambah konstanta regresi
    x2 = sm.add_constant(x_train)

    #prediksi y value
    y_predict = model.predict(x_test)

    #Eror
    eror = abs(((y_test-y_predict)/(y_test))*100)
    nilai_selisih = np.round(abs(y_test-y_predict))
    nilai_selisih = nilai_selisih.astype(int)

    selisih = (y_test > y_predict).apply(lambda x: "kurang " if x else "lebih ")

    selisih_str = selisih.astype(str)
    nilai_selisih_str = nilai_selisih.astype(str)

    #jumlah kelas
    #default = 30
    jumlah_kelas = (np.round(abs(y_predict / mhs_default))).astype(int)

    #dataframe predict dan actual
    hasil = pd.DataFrame({'Mata Kuliah': md.nama_matkul.unique(),'Jumlah Mahasiswa Sebenarnya': y_test,'Prediksi Jumlah Mahasiswa': (np.round(y_predict)).astype(int),'Hasil Prediksi':selisih_str + nilai_selisih_str + " orang",'Eror (%)':eror,'Prediksi Jumlah Kelas':jumlah_kelas})
    hasil.sort_index()
    st.write("--------------------------------------------------------------------------------------")
    st.write("Perbandingan Hasil Prediksi dan Data Aktual Peserta Mata Kuliah Tahun ",tahun)
    st.write(hasil)
