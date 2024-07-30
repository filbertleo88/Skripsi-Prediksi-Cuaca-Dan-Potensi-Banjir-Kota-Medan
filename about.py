import streamlit as st

def app():
    st.title("Tentang Kami")

    st.header("Deskripsi Projek")
    st.markdown("""
                Projek ini adalah penelitian yang dikerjakan oleh Filbert Leonardo (200416004) sebagai 
                bagian dari persyaratan untuk menyelesaikan program studi dan mendapatkan gelar Sarjana 
                Komputer di jurusan Sistem Informasi, Universitas Sari Mutiara Indonesia.
        """)

    tab1, tab2, tab3, tab4 = st.tabs(["Latar Belakang", "Permasalahan", "Tujuan", "Manfaat"])

    with tab1:
        st.info("""Perubahan iklim mempengaruhi pola cuaca di berbagai wilayah, sehingga sulit untuk 
                memprediksi cuaca. Dalam beberapa tahun terakhir, perubahan iklim telah memberikan 
                dampak signifikan terhadap curah hujan di Indonesia. Laporan BNPB mengungkapkan 10 orang 
                hilang, 204 tewas, 5.555 terluka, dan 5,35 juta dievakuasi karena banjir. Salah satunya 
                adalah Kota Medan, yang merupakan pusat provinsi Sumatera Utara dengan 2.494.512 penduduk,
                 mencakup 26.510 hektar dan rawan terhadap banjir karena lokasinya di dataran rendah di 
                pertemuan Sungai Babura dan Sungai Deli. Pada tahun 2022, Kota Medan mengalami 16 
                kejadian banjir yang menggusur 194.842 orang selama musim hujan menurut laporan BPS Sumut.
        """)
    with tab2:
        st.info("""Prediksi cuaca sangatlah penting untuk meningkatkan kewaspadaan dan persiapan 
                agar terhindar dari dampak buruk banjir. Dengan menggunakan 
                machine learning, kita dapat memprediksi pola cuaca serta potensi terjadi banjir. 
                Hal ini memungkinkan identifikasi dini potensi banjir dan memungkinkan tindakan pencegahan 
                dan mitigasi yang lebih efektif. Serta memungkinkan evakuasi yang lebih cepat dan tepat, 
                sehingga mempercepat penyebaran informasi tentang adanya potensi banjir kepada masyarakat.
        """)
    with tab3:
        st.info("""Penelitian ini bertujuan untuk menerapkan teknologi machine learning guna mendukung upaya 
                mitigasi banjir di Kota Medan. Penelitian ini berupaya untuk meningkatkan mitigasi 
                bencana banjir di Kota Medan dengan memberikan prediksi banjir dan prakiraan cuaca yang 
                lebih tepat melalui dashboard interaktif.  
        """)
    with tab4:
        st.info("""Dengan adanya penelitian ini, diharapkan manajemen risiko banjir dapat 
                ditingkatkan, sehingga respons terhadap bencana banjir menjadi lebih efisien dan 
                tepat waktu. Selain itu, dashboard interaktif juga akan meningkatkan keterlibatan 
                masyarakat dalam memahami dan mengatasi risiko banjir, serta memfasilitasi koordinasi 
                antar pihak terkait untuk mengambil tindakan preventif yang lebih efektif.
        """)

    st.subheader("Evaluasi Model")
    tab5, tab6 = st.tabs(["Model Prediction", "Model Forecast"])
    
    with tab5:
        st.info("""
        Menggunakan model CatBoost Classifier untuk memprediksi potensi banjir di kota Medan:
        - Accuracy Score = 0.96
        - Recall Score = 0.96
        - Precision Score = 0.96
        - F1 Score = 0.96
        """)
    with tab6:
        st.info("""
        Menggunakan model Long Short Term Memory untuk memprediksi cuaca pada hari selanjutnya:
        - Variabel curah_hujan: MAE = 6.10, R2 = 0.18, RMSE = 8.73 , MAPE = inf
        - Variabel suhu_udara: MAE = 1.00, R2 = 0.24, RMSE = 1.24 , MAPE = 3.48
        - Variabel kelembapan_udara: MAE = 4.53, R2 = 0.32, RMSE = 5.64, MAPE = 6.00
        """)

    st.subheader("Dataset yang Digunakan")
    st.markdown("""
    Kami menggunakan beberapa dataset dalam projek ini. Berikut adalah beberapa di antaranya:
    1. Data Cuaca Harian di Kota Medan - [BMKG](https://dataonline.bmkg.go.id/data_iklim)
    2. Data Bencana di Indonesia - [BNPB](https://dibi.bnpb.go.id/)
    """)

    st.subheader("Referensi Tambahan")
    st.markdown("""
        - **Proses Pembuatan Model:** [Link ke Colab](https://colab.research.google.com/drive/1w15YdHEOq1vsbp6qQOPjFzWweW-2P_q5?usp=sharing)
        - **GitHub Project:** [Link ke GitHub]()
        - **PowerPoint:** [Link ke PPT]()
    """)

    st.subheader("Kontak Developer")
    st.markdown("""
        **Filbert Leonardo**
        - Email: [filbertleo88@gmail.com](mailto:filbertleo88@gmail.com) 
        - LinkedIn: [Filbert Leonardo](https://www.linkedin.com/in/filbert-leonardo/) 
    """)
    




