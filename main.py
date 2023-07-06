import streamlit as st
import pickle


# Membaca Model
model = pickle.load(open('Stroke_Model.sav', 'rb'))


st.title("Prediksi Penyakit Stroke Dengan Algoritma Random Forest")
st.subheader("Jawablah Beberapa Pertanyaan Dibawah Ini Dahulu!")
col1, col2 = st.columns(2)

def validasi(input, value):
    if input == value:
        return 1
    else :
        return 0

with col1 :
    jenis_kelamin = st.selectbox('Apa jenis kelamin Anda?',('-','Laki - Laki', 'Perempuan'))
    jenis_kelamin = validasi(jenis_kelamin, 'Laki - Laki')
with col2 :
    umur = st.number_input('Berapa Umur Anda?', 0)

with col1 :
    hipertensi = st.selectbox('Apakah Anda Pernah Menderita Hipertensi?',('-','Pernah', 'Tidak'))
    hipertensi = validasi(hipertensi, 'Pernah')
with col2 :
    sakit_jantung = st.selectbox('Apakah Anda Pernah Sakit Jantung?',('-','Iya', 'Tidak'))
    sakit_jantung = validasi(sakit_jantung, 'Iya')

with col1 :
    menikah = st.selectbox('Apakah Anda Sudah Menikah?',('-','Sudah', 'Belum'))
    menikah = validasi(menikah, 'Sudah')
with col2 :
    tipe_pekerjaan = st.selectbox('Apa Pekerjaan Anda?',('-','Tidak Pernah Bekerja', 'Anak - Anak', 'Pekerjaan Pemerintah', 'Wiraswasta', 'Swasta'))
    if tipe_pekerjaan == 'Tidak Pernah Bekerja' :
        tipe_pekerjaan = 0
    elif tipe_pekerjaan == 'Anak - Anak' :
        tipe_pekerjaan = 1
    elif tipe_pekerjaan == 'Pekerjaan Pemerintah' :
        tipe_pekerjaan = 2
    elif tipe_pekerjaan == 'Wiraswasta' :
        tipe_pekerjaan = 3
    else :
        tipe_pekerjaan = 4

with col1 :
    area = st.selectbox('Dimanakah Anda Tinggal?',('-','Kota', 'Desa'))
    area = validasi(area, 'Kota')
with col2 :
    gula_darah = st.number_input('Berapa Rata-Rata Gula Darah Anda?', 0)

with col1 :
    berat = st.number_input('Berapa Berat Badan Anda?', 0)
with col2 :
    merokok = st.selectbox('Apakah Anda Merokok?',('-','Iya', 'Tidak'))
    merokok = validasi(merokok, 'Iya')



if st.button('Prediksi') :
    # Diaknosis
    diaknosis = ''

    # Menjalankan Model
    prediksi = model.predict([[jenis_kelamin, umur, hipertensi, sakit_jantung, menikah, tipe_pekerjaan, area, gula_darah, berat, merokok]])

    if(prediksi[0] != 0) :
        diaknosis = 'Anda Tidak Terkena Stroke'
    else :
        diaknosis = 'Anda Terkena Stroke'

    st.success(diaknosis)
