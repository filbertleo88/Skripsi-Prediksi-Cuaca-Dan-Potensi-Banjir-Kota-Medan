import streamlit as st

def app():
    st.title("Tentang Kami")

    st.header("Deskripsi Projek")
    st.markdown("""
        Pembuatan dashboard ini merupakan persyaratan yang harus dipenuhi untuk menyelesaikan 
                program studi dan memperoleh gelar Sarjana Komputer dengan jurusan Sistem Informasi 
                di Universitas Sari Mutiara Indonesia. Projek ini merupakan tugas akhir atau skripsi
                yang dikerjakan oleh Filbert Leonardo dengan NIM 200416004.
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
        Kami menggunakan model CatBoost Classifier untuk memprediksi potensi banjir di kota Medan:
        - Accuracy Score = 0.95
        - Recall Score = 0.93
        - Precision Score = 0.96
        - F1 Score = 0.95
        """)
    with tab6:
        st.info("""
        Kami menggunakan model Long Short Term Memory untuk memperkirakan cuaca pada waktu kedepannya:
        - Variabel curah_hujan: MAE = 5.59, RMSE = 8.12 , MAPE = inf
        - Variabel suhu_udara: MAE = 1.03, RMSE = 1.26 , MAPE = 3.48
        - Variabel kelembapan_udara: MAE = 4.69, RMSE = 5.81, MAPE = 6.22
        """)

    st.subheader("Dataset yang Digunakan")
    st.markdown("""
    Kami menggunakan beberapa dataset dalam projek ini. Berikut adalah beberapa di antaranya:
    1. Data Cuaca Harian di Kota Medan - [BMKG](https://dataonline.bmkg.go.id/home)
    2. Data Bencana di Indonesia - [BNPB](https://dibi.bnpb.go.id/)
    """)

    st.subheader("Referensi Tambahan")
    st.markdown("""
        - **Proses Analisis:** [Link ke Colab]()
        - **GitHub Project:** [Link ke GitHub]()
        - **PowerPoint:** [Link ke PPT]()
    """)

    st.subheader("Kontak")
    st.markdown("""
        **Filbert Leonardo**
        - Email: [filbertleo88@gmail.com](mailto:filbertleo88@gmail.com) 
        - LinkedIn: [Filbert Leonardo](https://www.linkedin.com/in/filbert-leonardo/) 
    """)
    




