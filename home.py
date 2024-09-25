import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def load_data(file_path, index_col=None):
    # index_col akan diabaikan jika None
    df = pd.read_csv(file_path, index_col=index_col)
    return df

def app():
    # Judul dan Informasi mengenai Dasboard
    st.title("Dashboard Prediksi Banjir di Kota Medan :thunder_cloud_and_rain:")
    st.write("""Memahami pola cuaca di Indonesia adalah kunci untuk mengetahui penyebab dan dampak banjir. 
             Tingginya curah hujan selama musim hujan secara signifikan berkontribusi pada terjadinya banjir 
             yang sering dan parah. Oleh karena itu, pemantauan cuaca yang tepat dan perbaikan infrastruktur 
             sangat diperlukan untuk mengurangi dampak banjir dan melindungi masyarakat. Di sinilah peran 
             proyek yang saya bangun untuk memprediksi banjir di kota Medan menjadi sangat penting. Dengan 
             menggunakan teknologi canggih seperti AI untuk menganalisis data cuaca dan memprediksi kemungkinan 
             terjadinya banjir, saya bertujuan untuk memberikan peringatan dini dan meningkatkan kesiapsiagaan 
             bencana, yang pada akhirnya akan melindungi warga kota Medan.
            """
    )

    with st.expander("Cuaca"):
        st.write("""
        Indonesia, sebagai negara kepulauan yang terletak di sepanjang garis khatulistiwa, memiliki iklim tropis 
                 dengan kelembapan tinggi dan suhu berkisar antara 26°C hingga 30°C sepanjang tahun. Cuaca di 
                 Indonesia sangat dipengaruhi oleh dua musim utama: musim kemarau (April hingga Oktober) dan 
                 musim hujan (November hingga Maret).

        - **Musim Kemarau**: Pada periode ini, cuaca umumnya panas dan kering. Namun, karena keragaman geografis, 
                 beberapa daerah masih mungkin mengalami hujan sesekali.
        - **Musim Hujan**: Ditandai dengan curah hujan yang tinggi, badai petir, dan kelembapan tinggi, musim hujan 
                 dapat menyebabkan perubahan cuaca yang signifikan dan tantangan.
        """)

    with st.expander("Banjir"):
        st.write("""
        Banjir adalah masalah umum dan serius di banyak bagian Indonesia, terutama selama musim hujan. Hujan yang 
                 sering dan lebat sering kali membanjiri sistem drainase, menyebabkan sungai meluap dan 
                 menenggelamkan daerah perkotaan dan pedesaan.

        #### Penyebab Banjir di Indonesia
        1. **Curah Hujan Tinggi**: Penyebab utama banjir selama musim hujan.
        2. **Sistem Drainase yang Buruk**: Infrastruktur yang tidak memadai di daerah perkotaan gagal menangani 
                 volume air.
        3. **Deforestasi**: Mengurangi kemampuan tanah untuk menyerap air hujan, yang mengakibatkan peningkatan 
                 aliran permukaan.
        4. **Urbanisasi**: Perkembangan yang cepat mengurangi permukaan yang dapat menyerap air, memperburuk 
                 risiko banjir.

        ### Dampak Banjir
        Banjir memiliki dampak yang menghancurkan pada masyarakat, infrastruktur, dan ekonomi.

        - **Kerugian Ekonomi**: Pada tahun 2020, Jakarta sendiri mengalami kerugian ekonomi yang diperkirakan 
                 sekitar IDR 32 triliun (sekitar USD 2,3 miliar) akibat banjir.
        - **Korban Jiwa**: Banjir sering menyebabkan korban jiwa yang signifikan. Misalnya, pada Januari 2020, 
                 banjir di Jakarta menyebabkan 66 kematian.
        - **Pengungsian**: Ribuan orang mengungsi dari rumah mereka setiap tahun akibat banjir parah. Pada tahun 
                 2021, banjir membuat lebih dari 200.000 penduduk mengungsi di seluruh negeri.
        """)

    # Load Dataset
    df = load_data("data/df_classifier.csv")
    df['tanggal'] = pd.to_datetime(df['tanggal'])
    df.set_index('tanggal', inplace=True)

    st.divider()
    # Menampilkan Data Historis Banjir
    st.subheader("Data Historis Banjir")
    st.dataframe(df, use_container_width=True)
    url1 = "https://dataonline.bmkg.go.id/home"
    url2 = "https://gis.bnpb.go.id/"
    st.caption("Data cuaca dapat diperoleh dari BMKG [Data Online](%s)" % url1)
    st.caption("Data bencana dapat diperoleh dari BPBD [Geoportal Bencana Indonesia](%s)" % url2)

    st.divider()
    # Menampilkan penjelasan dari struktur data
    st.subheader("Deskripsi Variabel Dataset")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Tanggal", "Curah Hujan (RR)", "Suhu Udara Rata-Rata (Tavg)",
                                             "Kelembapan Udara Rata-Rata (RH_avg)", "Status Banjir"])

    with tab1:
        st.info("""Data ini mencatat tanggal dan waktu pengamatan dilakukan, penting untuk mengetahui 
        pola kejadian banjir dan tren musiman.""")

    with tab2:
        st.info("""Data ini menunjukkan jumlah curah hujan yang tercatat pada periode tertentu, 
        menjadi indikator utama untuk memprediksi potensi banjir.""")

    with tab3:
        st.info("""Data ini mencatat suhu udara rata-rata pada saat pengamatan, suhu yang ekstrem dapat mempengaruhi 
        intensitas dan durasi hujan, berkontribusi terhadap risiko banjir.""")

    with tab4:
        st.info("""Data ini menunjukkan tingkat kelembapan udara rata-rata selama periode pengamatan, 
        kelembapan tinggi meningkatkan potensi hujan lebat yang dapat menyebabkan banjir.""")

    with tab5:
        st.info("""Data ini mencatat status banjir berdasarkan kondisi cuaca yang ada, 
        penting untuk mengidentifikasi wilayah yang terdampak dan merencanakan mitigasi bencana.""")
          