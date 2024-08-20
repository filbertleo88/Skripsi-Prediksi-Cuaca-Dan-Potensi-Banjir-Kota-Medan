# Prediksi Cuaca dan Potensi Banjir di Kota Medan Menggunakan CatBoost dan LSTM
Projek ini adalah penelitian yang dikerjakan oleh Filbert Leonardo (200416004) sebagai bagian dari persyaratan untuk menyelesaikan program studi dan mendapatkan gelar Sarjana Komputer di jurusan Sistem Informasi, Universitas Sari Mutiara Indonesia.

## Table of Contents
- [Tentang Aplikasi](#tentang_aplikasi)
- [Fitur Utama](#fitur_utama)
- [Struktur Proyek](#struktur_proyek)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Sumber Data](#sumber_data)
- [Pembuatan Model Prediksi](#pembuatan_model_prediksi)
- [Dashboard](#dashboard)

## Tentang Aplikasi
Aplikasi ini merupakan dashboard web interaktif yang dibangun menggunakan Streamlit. Dashboard ini menyediakan prediksi cuaca dan potensi banjir dengan mengintegrasikan model AI yang telah dikembangkan menggunakan metode CatBoost dan LSTM. Tujuan utama dari aplikasi ini adalah untuk meningkatkan mitigasi banjir dan kesiapsiagaan terhadap kondisi cuaca ekstrem melalui akses informasi yang akurat.

Dashboard ini memungkinkan pengguna untuk:
- Melihat prakiraan cuaca harian yang mencakup curah hujan, suhu udara, dan kelembapan udara.
- Mengetahui potensi banjir berdasarkan prediksi model AI, membantu dalam pengambilan tindakan preventif.
- Mengakses visualisasi data yang membantu dalam memahami tren dan pola cuaca serta potensi banjir.

## Fitur Utama
- **Prediksi Cuaca**: Menampilkan prakiraan cuaca harian menggunakan model LSTM.
- **Prediksi Potensi Banjir**: Menyediakan informasi tentang kemungkinan terjadinya banjir dengan model CatBoost.
- **Visualisasi Data**: Grafik dan chart yang intuitif untuk memudahkan pemahaman data.
- **Antarmuka User-Friendly**: Mudah digunakan oleh masyarakat umum dan aparat setempat.

## Struktur Proyek
- `data/`: Berisi dataset cuaca dan bencana.
- `notebook/`: Berisi Jupyter Notebooks untuk eksplorasi data dan pengembangan model.
- `model/`: Berisi model yang telah dilatih dan disimpan.
- `main.py`: Aplikasi dashboard Streamlit.
- `README.md`: Dokumentasi proyek.

## Instalasi
1. Clone repository ini.
    ```bash
    git clone https://github.com/filbertleo88/Skripsi-Prediksi-Cuaca-Dan-Potensi-Banjir-Kota-Medan.git
    ```
2. Masuk ke direktori proyek.
    ```bash
    cd Skripsi-Prediksi-Cuaca-Dan-Potensi-Banjir-Kota-Medan
    ```
3. Instal dependencies.
    ```bash
    pip install -r requirements.txt
    ```

## Penggunaan
1. Jalankan aplikasi Streamlit.
    ```bash
    streamlit run app.py
    ```
2. Buka browser dan akses `http://localhost:8501` untuk menggunakan dashboard.

## Sumber Data
- Dataset Cuaca: [Data Online BMKG](https://dataonline.bmkg.go.id/home)
- Dataset Bencana: [Geoportal Data Bencana Indonesia BNPB](https://gis.bnpb.go.id/)

## Pembuatan Model Prediksi [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1w15YdHEOq1vsbp6qQOPjFzWweW-2P_q5?usp=sharing)
- Model prediksi cuaca menggunakan LSTM dikembangkan untuk mengidentifikasi pola cuaca berdasarkan data historis.
- Model prediksi potensi banjir menggunakan CatBoost dikembangkan untuk memprediksi kemungkinan terjadinya banjir berdasarkan kondisi cuaca.

## Dashboard [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://prediksi-cuaca-dan-banjir-kota-medan.streamlit.app/)
Dashboard ini dibuat dengan Streamlit untuk menyediakan antarmuka yang interaktif dan mudah digunakan.

Dengan adanya dashboard ini, diharapkan dapat membantu masyarakat dan pemerintah setempat dalam memitigasi risiko banjir dan mempersiapkan diri terhadap kondisi cuaca ekstrem.