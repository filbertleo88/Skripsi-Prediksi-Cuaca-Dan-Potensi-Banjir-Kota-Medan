import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from keras.models import load_model as keras_model
from sklearn.preprocessing import MinMaxScaler

# Function to load data
def load_data(file_path, index_col=None):
    df = pd.read_csv(file_path, index_col=index_col)
    return df

# Function to load machine learning model
def load_model(file_path):
    try:
        with open(file_path, 'rb') as model_in:
            model = pickle.load(model_in)
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

# Function to convert series to supervised learning format
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if isinstance(data, list) else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [(f'var{j+1}(t-{i})') for j in range(n_vars)]
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [(f'var{j+1}(t)') for j in range(n_vars)]
        else:
            names += [(f'var{j+1}(t+{i})') for j in range(n_vars)]
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    if dropnan:
        agg.dropna(inplace=True)
    return agg

# Function to plot original and forecasted data
def plot_forecast(df, forecast_df):
    for column in df.columns:
        fig = make_subplots(rows=1, cols=1, shared_xaxes=True)
        fig.add_trace(go.Scatter(x=df.index, y=df[column], mode='lines', name='Historikal', line=dict(color='cyan')), row=1, col=1)
        fig.add_trace(go.Scatter(x=forecast_df.index, y=forecast_df[column], mode='lines', name='Prakiraan', line=dict(color='magenta')), row=1, col=1)
        
        if not df.empty and not forecast_df.empty:
            fig.add_trace(go.Scatter(x=[df.index[-1], forecast_df.index[0]],
                                     y=[df[column].iloc[-1], forecast_df[column].iloc[0]],
                                     mode='lines', line=dict(color='magenta'), showlegend=False), row=1, col=1)
            
            fig.update_layout(
                title=f'Historikal vs Prakiraan {column}',
                xaxis_title='Date',
                yaxis_title=column,
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1, label="1m", step="month", stepmode="backward"),
                            dict(count=6, label="6m", step="month", stepmode="backward"),
                            dict(step="all")
                        ])
                    ),
                    rangeslider=dict(visible=True),
                    type="date"
                )
            )
            st.plotly_chart(fig, use_container_width=True)

def prediksi_banjir(classifier, curah_hujan, suhu_udara, kelembapan_udara):
    if classifier is not None:
        prediction = classifier.predict([[curah_hujan, suhu_udara, kelembapan_udara]])
        return prediction[0]
    else:
        raise ValueError("The classifier model is not loaded.")

def map_status_banjir(prediction):
    status_banjir = {0: 'Tidak Banjir', 1: 'Banjir'}
    return status_banjir.get(prediction, "Unknown")

def app():
    st.title('Selamat Datang di Aplikasi Peramalan Cuaca')
    st.subheader('Prediksi Time Series Cuaca di Kota Medan Menggunakan Algoritma Long Short Term Memory')

    # Load data
    filepath = 'data/df_time_series.csv'
    df = load_data(filepath)
    df['tanggal'] = pd.to_datetime(df['tanggal'], format='%Y-%m-%d')
    df.set_index('tanggal', inplace=True)

    # Load models
    lstm_model = keras_model('model/best_model.h5')
    classifier = load_model("model/cb_grid.pkl")

    st.dataframe(df, use_container_width=True)

    if lstm_model:
        n_forecast_days = st.number_input('Jumlah hari yang ingin diprediksi', min_value=1, max_value=30, value=30)

        if st.button('Prediksi'):
            with st.spinner('Melakukan prediksi...'):
                scaler = MinMaxScaler()
                df_scaled = scaler.fit_transform(df)
                n_days = 3
                n_features = df.shape[1]
                test_data_supervised = series_to_supervised(df_scaled, n_days, 1)
                test_data_sequences = test_data_supervised.values[:, :n_days * n_features]

                forecast = []
                for i in range(n_forecast_days):
                    seq = test_data_sequences[i].reshape((1, n_days, n_features))
                    predicted = lstm_model.predict(seq)
                    forecast.append(predicted[0])

                forecast_array = np.array(forecast)
                forecast_inverse = scaler.inverse_transform(forecast_array)
                forecast_inverse = np.abs(forecast_inverse)
                forecast_inverse = np.round(forecast_inverse, 2)

                date_range = pd.date_range(start=df.index[-1], periods=n_forecast_days + 1)
                forecast_df = pd.DataFrame(forecast_inverse, index=date_range[1:], columns=df.columns)

                st.subheader("Data Prakiraan Cuaca")
                plot_forecast(df, forecast_df)

                forecast_df['status_banjir'] = forecast_df.apply(
                    lambda row: map_status_banjir(prediksi_banjir(classifier, row['curah_hujan'], row['suhu_udara'], row['kelembapan_udara'])), axis=1)

                st.subheader("Data Prakiraan Cuaca dengan Potensi Banjir")
                st.dataframe(forecast_df, use_container_width=True)
