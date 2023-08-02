import streamlit as st
import pandas as pd
import numpy as np
#import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import string

st.markdown("<h2 style='text-align: center;'>Prediksi Jumlah Peserta Mata Kuliah</h2>",unsafe_allow_html=True)
st.sidebar.success("Select A Page Above")

from datetime import date
tanggal = date.today()
ambiltahunprediksi = tanggal.year
tahun_prediksi = st.number_input('Masukkan tahun prediksi', min_value=0, value=ambiltahunprediksi)
mhs_default = st.number_input('Masukkan Kapasitas Mahasiswa PerKelas', min_value=0)

uploaded_file = st.file_uploader("Pilih file csv")
if uploaded_file is not None:
    dataupload = pd.read_csv(uploaded_file)
    dataupload.style.highlight_null(null_color='red')
    st.write("DataFrame yang di unggah ")
    st.write(dataupload)

    df = dataupload.drop(columns=['mutu','nilai','sks','kode_mk'])

    #transformasi tahun akademik
    df["tahun_akademik"] = df["tahun_akademik"].replace(to_replace = "^2010/", value = 2010, regex=True)
    df["tahun_akademik"] = df["tahun_akademik"].replace(to_replace = "^2011/", value = 2011, regex=True)
    df["tahun_akademik"] = df["tahun_akademik"].replace(to_replace = "^2012/", value = 2012, regex=True)
    df["tahun_akademik"] = df["tahun_akademik"].replace(to_replace = "^2013/", value = 2013, regex=True)
    df["tahun_akademik"] = df["tahun_akademik"].replace(to_replace = "^2014/", value = 2014, regex=True)
    df["tahun_akademik"] = df["tahun_akademik"].replace(to_replace = "^2015/", value = 2015, regex=True)
    df["tahun_akademik"] = df["tahun_akademik"].replace(to_replace = "^2016/", value = 2016, regex=True)
    df["tahun_akademik"] = df["tahun_akademik"].replace(to_replace = "^2017/", value = 2017, regex=True)
    df["tahun_akademik"] = df["tahun_akademik"].replace(to_replace = "^2018/", value = 2018, regex=True)
    df["tahun_akademik"] = df["tahun_akademik"].replace(to_replace = "^2019/", value = 2019, regex=True)
    df["tahun_akademik"] = df["tahun_akademik"].replace(to_replace = "^2020/", value = 2020, regex=True)
    df["tahun_akademik"] = df["tahun_akademik"].replace(to_replace = "^2021/", value = 2021, regex=True)

    #Drop tahun akademik yang tidak digunakan
    dfx = df.drop(df[df.tahun_akademik == (2010)].index)
    dfx = dfx.drop(dfx[dfx.tahun_akademik == (2011)].index)
    dfx = dfx.drop(dfx[dfx.tahun_akademik == (2012)].index)
    dfx = dfx.drop(dfx[dfx.tahun_akademik == (2013)].index)
    dfx = dfx.drop(dfx[dfx.tahun_akademik == (2014)].index)
    dfx = dfx.drop(dfx[dfx.tahun_akademik == (2015)].index)
    dfx = dfx.drop(dfx[dfx.tahun_akademik == (2016)].index)
    dfx = dfx.drop(dfx[dfx.tahun_akademik == (2021)].index)

    #menghilangkan tanda baca
    dfx["nama_matkul"] = dfx["nama_matkul"].str.lower()
    dfx["nama_matkul"] = dfx["nama_matkul"].str.translate(str.maketrans(string.punctuation," " *len(string.punctuation)))

    #Replace nama matkul
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "pendidikan pancasila", value = "pancasila", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "pancasila", value = "pendidikan pancasila", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "pendidikan agama", value = "agama", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "pendidikan  agama", value = "agama", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "agama", value = "pendidikan agama", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "probabilitas  dan statistik", value = "probabilitas dan statistik", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "matematika  dasar ii", value = "matematika dasar ii", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "organisasi  dan arsitektur komputer", value = "organisasi dan arsitektur komputer", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "struktur  data  dan algoritma", value = "struktur data dan algoritma", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "pemrograman  berorientasi objek", value = "pemrograman berorientasi objek", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "analisis  dan  perancangan sistem", value = "analisis perancangan sistem", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "kerja  praktik", value = "kerja praktik", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "tugas akhir 1  proposal", value = "tugas akhir 1 proposal", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "keamanan  informasi  dan jaringan", value = "keamanan informasi dan jaringan", regex = True)
    dfx["nama_matkul"] = dfx["nama_matkul"].replace(to_replace = "proyek perangkat lunak *", value = "proyek perangkat lunak*")
    dfx["nama_matkul"] = dfx["nama_matkul"].str.replace("\(sig\)","1")

    #Menghilangkan spasi setelah dan sebelum karakter
    dfx["nama_matkul"] = dfx["nama_matkul"].str.strip()

    #menghapus mata kuliah pilihan
    dfx = dfx.drop(dfx[dfx.nama_matkul == ("manajemen rantai pasok  pl")].index)
    dfx = dfx.drop(dfx[dfx.nama_matkul == ("pemrograman perangkat bergerak  pl")].index)
    dfx = dfx.drop(dfx[dfx.nama_matkul == ("sig ii  pl")].index)
    dfx = dfx.drop(dfx[dfx.nama_matkul == ("data mining  pl")].index)
    dfx = dfx.drop(dfx[dfx.nama_matkul == ("komputasi awan  pl")].index)
    dfx = dfx.drop(dfx[dfx.nama_matkul == ("kriptografi  pl")].index)
    dfx = dfx.drop(dfx[dfx.nama_matkul == ("pengolahan citra digital  pl")].index)
    dfx = dfx.drop(dfx[dfx.nama_matkul == ("forensik digital  pl")].index)

    #Feature Costraction (Membuat kolom baru jumlah mahasiswa)
    jumlah = dfx.groupby(["tahun_akademik", "nama_matkul"]).size().reset_index(name="jumlah_mhs")

    # Using pandas.concat() to append a row
    new_row = pd.DataFrame({'tahun_akademik':2017, 'nama_matkul':'manajemen proyek perangkat lunak', 'jumlah_mhs':0}, index=[14])
    jumlah = pd.concat([new_row,jumlah.loc[:]]).reset_index(drop=True)
    #print (jumlah)

    jumlah = jumlah.sort_values(by=["tahun_akademik","nama_matkul"], ascending=True)
    jumlah = jumlah.reset_index()
    jumlah = jumlah.drop(columns=['index'])
    jumlah2 = jumlah.sort_values(by=["nama_matkul"], ascending=True)
    jumlah2['tahun_akademik'] = jumlah2['tahun_akademik'].astype(str)
    st.write("--------------------------------------------------------------------------------------")
    st.write("Data Frame Jumlah Peserta Mata Kuliah PerTahun")
    st.write(jumlah2)


    #Buat kolom id_matkul
    i = len(jumlah['nama_matkul'].unique())
    count = len(jumlah['tahun_akademik'].unique()) + 1

    dfs = pd.DataFrame()  # Create an empty DataFrame
    for k in range(1, count):
        for j in range(1, i + 1):
            dfs = dfs.append(pd.DataFrame({'id_matkul': [j]}), ignore_index=True)
            
    jumlah['id_matkul']=dfs

    @st.cache_data
    def convert_df(jumlah):
        return jumlah.to_csv(index=False).encode('utf-8')

    csv_jumlah = convert_df(jumlah)

    st.download_button(
        "Download Jumlah Peserta Mata Kuliah",
        csv_jumlah,
        "JumlahPesertaMataKuliah.csv",
        "text/csv",
        key='download-csvjumlah'
        )
    

    #Menambah kolom qtr dan ktgr
    #tambah quarter
    jumlah['qtr1'] = jumlah.index+1
    jumlah['qtr2'] = jumlah['qtr1']**2
    jumlah['qtr3'] = jumlah['qtr1']**3
    jumlah['qtr4'] = jumlah['qtr1']**4

    #id_matkul is integer, want to make it to string
    jumlah['ktgr'] = jumlah['id_matkul'].astype(str)

    data = pd.get_dummies(jumlah, prefix = ['ktgr'], columns=['ktgr'], drop_first=True)

    #Data Frame baru untuk testing
    dt = data["nama_matkul"].unique()
    dt = pd.DataFrame(dt)
    dt = dt.rename(columns={0: 'nama_matkul'})
    dt['id_matkul'] = dt.index+1

    a = tahun_prediksi
    for b, kode in enumerate(dt['nama_matkul']): 
        dti = (data.iloc[-1]['tahun_akademik'])+1
        dt['tahun_akademik'] = dti   

    training = data.loc[data['tahun_akademik'] != a]

    #dataframe qtr dan ktgr baru untuk testing
    c = (training.iloc[-1]['qtr1'])+1
    dt['qtr1'] = dt.index+c
    dt['qtr2'] = dt['qtr1']**2
    dt['qtr3'] = dt['qtr1']**3
    dt['qtr4'] = dt['qtr1']**4

    dt['ktgr'] = dt['id_matkul'].astype(str)
    dt = pd.get_dummies(dt, prefix = ['ktgr'], columns=['ktgr'], drop_first=True)

    #data testing dan x testing
    if a in data['tahun_akademik']:
        testing = data.loc[data['tahun_akademik'] == a]
        x_test = testing.drop(columns=['nama_matkul', 'id_matkul', 'tahun_akademik','jumlah_mhs'])
    else:
        testing = dt
        x_test = testing.drop(columns=['nama_matkul', 'id_matkul', 'tahun_akademik'])

    #memisahkan variabel x dan y training
    x_train = training.drop(columns=['nama_matkul', 'id_matkul', 'tahun_akademik','jumlah_mhs'])
    y_train = training['jumlah_mhs']

    #Modelling
    model = LinearRegression()
    model.fit(x_train, y_train)

    #konstanta regresi
    #x2 = sm.add_constant(x_train)
    x2 = pd.DataFrame(x_train)
    x2.insert(0, 'const', '1')

    #koefisien regresi 
    #est = sm.OLS(y_train, x2)
    #est2 = est.fit()

    #prediksi y value
    y_predict = model.predict(x_test)

    #jumlah kelas
    #default = 30
    jumlah_kelas = (np.round(abs(y_predict / mhs_default))).astype(int)

    #dataframe predict dan actual
    hasil_prediksi = pd.DataFrame({'Mata Kuliah': data.nama_matkul.unique(),'Prediksi Jumlah Mahasiswa Mengambil': (np.round(y_predict)),'Prediksi Jumlah Kelas Dibuka': jumlah_kelas})
    hasil_prediksi.sort_index()
    st.write("--------------------------------------------------------------------------------------")
    st.write("Prediksi Jumlah Peserta Mata Kuliah Pada ",tahun_prediksi)
    st.write(hasil_prediksi)

    @st.cache_data
    def convert_df(hasil_prediksi):
        return hasil_prediksi.to_csv(index=False).encode('utf-8')

    csv_prediksi = convert_df(hasil_prediksi)

    st.download_button(
        "Download Hasil Prediksi",
        csv_prediksi,
        "HasilPrediksi.csv",
        "text/csv",
        key='download-csv'
        )
