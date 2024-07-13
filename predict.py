import streamlit as st
import pickle
import pandas as pd

# Load Model Machine Learning
def load_model(file_path):
    try:
        with open(file_path, 'rb') as model_in:
            model = pickle.load(model_in)
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

# Define the prediction function
def prediksi_banjir(classifier, data):
    try:
        predictions = classifier.predict(data)
        return predictions
    except Exception as e:
        st.error(f"Error making predictions: {e}")
        return None

def map_status_banjir(predictions):
    status_banjir = {0: 'Tidak Banjir', 1: 'Banjir'}
    return [status_banjir.get(prediction, "Unknown") for prediction in predictions]

def app():
    # Judul dan Informasi mengenai Menu Prediksi
    st.title('Selamat Datang di Aplikasi Prediksi Banjir')

    # Load the trained classifier model from the file
    model_file_path = "model/cb_grid.pkl"  # Ganti dengan path model yang sesuai
    classifier = load_model(model_file_path)

    # Sidebar 
    with st.sidebar:
        st.subheader("Upload CSV File untuk Prediksi")
        # File uploader
        uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

        st.write("Jika Anda belum memiliki dataset, Anda dapat mengunduh contoh dataset di bawah ini.")
        df_example = pd.read_csv("data/df_time_series.csv")
        st.download_button(label="Unduh Contoh Dataset",
                           data=df_example.to_csv(index=False),
                           file_name='contoh_dataset.csv',
                           mime='text/csv')

    # Halaman Prediksi
    st.subheader("Prediksi Potensi Banjir di Kota Medan Menggunakan Algoritma CatBoost Classifier")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        # st.write("Dataset yang di-upload:")
        # st.dataframe(data.head(), use_container_width=True)

        if classifier:
            predictions = prediksi_banjir(classifier, data[['curah_hujan', 'suhu_udara', 'kelembapan_udara']])
            if predictions is not None:
                data['prediksi_status_banjir'] = map_status_banjir(predictions)
                st.write("Hasil Prediksi:")
                st.dataframe(data, use_container_width=True)
        else:
            st.error("Model classifier tidak berhasil di-load.")

    # Input parameters
    curah_hujan = st.number_input('Curah hujan (RR)', min_value=0.0, max_value=100.0, format="%.2f")
    suhu_udara = st.number_input('Suhu Udara Rata-Rata (Tvag)', min_value=20.0, max_value=40.0, format="%.2f")
    kelembapan_udara = st.number_input('Kelembapan Udara Rata-Rata (Rhavg)', min_value=50.0, max_value=100.0, format="%.2f")

    # Button to trigger prediction dengan key unik
    if st.button('Prediksi'):
        if classifier:
            prediction = prediksi_banjir(classifier, [[curah_hujan, suhu_udara, kelembapan_udara]])
            if prediction is not None:
                status_banjir = map_status_banjir(prediction)[0]
                if status_banjir == "Banjir":
                    st.error(f'Kondisi cuaca berpotensi: {status_banjir}')
                else:
                    st.success(f'Kondisi cuaca berpotensi: {status_banjir}')
        else:
            st.error("Model classifier tidak berhasil di-load.")
