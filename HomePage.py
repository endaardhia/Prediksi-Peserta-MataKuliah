import streamlit as st

st.set_page_config(
    page_title="Sistem Prediksi"
)

st.title("SELAMAT DATANG DI SISTEM PREDIKSI JUMLAH PESERTA MATA KULIAH")
st.subheader("Jurusan Informatika Universitas Tanjungpura")
st.sidebar.success("Select A Page Above")

matkul_link = '(https://informatika.untan.ac.id/kurikulum)'

st.write("Sistem Prediksi Jumlah Peserta Mata Kuliah ini akan membantu pengguna dalam memprediksi jumlah mahasiswa yang akan mengambil suatu mata kuliah tertentu")
st.write("Menu Model akan menampilkan perbandingan hasil prediksi dan nilai aktual jumlah peserta mata kuliah")
st.write("Menu Prediksi akan menampilkan hasil prediksi jumlah peserta mata kuliah")
st.write("__________________________________________________________________________")
st.write("""## Daftar Mata Kuliah Informatika""")
st.write(matkul_link)