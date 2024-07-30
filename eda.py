import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from scipy.stats import pearsonr, kendalltau

def load_data(file_path, index_col=None):
    # index_col akan diabaikan jika None
    df = pd.read_csv(file_path, index_col=index_col)
    return df

def app():
    # Judul dan Informasi mengenai Menu EDA
    st.title('Dasboard Kondisi Cuaca Kota Medan (2020 - 2024) ')
    
    # Load data
    df = load_data("data/df_classifier.csv")
    df['tanggal'] = pd.to_datetime(df['tanggal'])

    parameters = ['curah_hujan', 'suhu_udara', 'kelembapan_udara']

    # Dictionary to map categories to their respective colors
    category_colors = {
        "Tidak": "#00FF00",     # Green
        "Ya": "#FF0000"             # Red
    }

#====================================================================

    # Sidebar untuk filter
    with st.sidebar:

        st.header('Filters')

        selected_category = st.selectbox('Pilih Status Banjir',
                                        ['Overall Category'] + list(df['status_banjir'].unique()), index=0)      
        
        start_date = st.date_input('Tanggal Mulai', min(df['tanggal']).date(),
                                        min_value=pd.to_datetime('2020-01-01').date(),
                                        max_value=pd.to_datetime('2024-06-30').date())
        end_date = st.date_input('Tanggal Berakhir', max(df['tanggal']).date(),
                                        min_value=pd.to_datetime('2020-01-01').date(),
                                        max_value=pd.to_datetime('2024-06-30').date())
    

    start_datetime = pd.to_datetime(start_date).date()
    end_datetime = pd.to_datetime(end_date).date()
    df['tanggal'] = df['tanggal'].dt.date

#============================================================================================
    
    # Opsi Kategori
    if selected_category == 'Overall Category':
        # filtered_data = df.loc[start_date:end_date]
        filtered_data = df[(df['tanggal'] >= start_datetime) & (df['tanggal'] <= end_datetime)]
    else:
        filtered_data = df[(df['status_banjir'] == selected_category) &
                    (df['tanggal'] >= start_datetime) & (df['tanggal'] <= end_datetime)]

## Total Days of Status Banjir
    st.write(f"**Kejadian Banjir - {selected_category}**")
    category_counts = filtered_data.groupby('status_banjir')['tanggal'].nunique()
    cols = st.columns(2)
    for index, (category, count) in enumerate(category_counts.items()):
        formatted_count = "{:,}".format(count)  # Format count with commas for thousands
        col = cols[index % 2]  # Cycle through the columns (2 columns)
        
        # Get the color for the current category
        color = category_colors[category]
        
        # Display the metric with custom color
        col.markdown(f"""
            <div style="color:{color};">
                <h3>{category}</h3>
                <p>{formatted_count} Hari</p>
            </div>
        """, unsafe_allow_html=True)

## Distribution of status_banjir
    # Calculate counts for each category and set the custom order
    custom_category_order = ["Tidak", "Ya"]
    category_counts = filtered_data['status_banjir'].value_counts().reset_index()
    category_counts.columns = ['status_banjir', 'Count']
    category_counts['status_banjir'] = pd.Categorical(category_counts['status_banjir'], categories=custom_category_order, ordered=True)
    category_counts = category_counts.sort_values('status_banjir')

    # Create a pie chart with custom colors
    fig = px.pie(
        category_counts, 
        values='Count', 
        names='status_banjir', 
        title='Persentase Kejadian Banjir',
        color='status_banjir',
        color_discrete_map=category_colors
    )

    st.plotly_chart(fig, use_container_width=True)

#==================================================================
## Time Series of Weather

    col1, col2 = st.columns(2)
    with col1:
        selected_parameter = st.selectbox('Pilih Parameter Cuaca', parameters)
    with col2:
        frequency_options = {
            'Harian': 'D',
            'Mingguan': 'W',
            'Bulanan': 'M',
            'Tahunan': 'Y'
        }
        selected_frequency_label = st.selectbox('Pilih Frekuensi Waktu', list(frequency_options.keys()))
        selected_frequency = frequency_options[selected_frequency_label]

    # Set 'tanggal' column as the index
    datetime_data = filtered_data.copy()
    datetime_data['tanggal'] = pd.to_datetime(datetime_data['tanggal'])
    datetime_data.set_index('tanggal', inplace=True)
    datetime_data = datetime_data.drop(columns=['status_banjir'],axis=1)

    # Resample the data based on the selected frequency
    datetime_data_resampled = datetime_data.resample(selected_frequency).mean().reset_index()

    # Plot the chart for the selected districts
    fig = px.line(datetime_data_resampled, x='tanggal', y=selected_parameter,
                title=f'Tingkat {selected_parameter} {selected_frequency_label} Selama Periode Waktu Tertentu')

    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(visible=True),
            type="date"
        )
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)
#==================================================================
## Correlation of Weather

    # Display Scatter Plot
    col1, col2 = st.columns(2)
    with col1:
        selected_parameter1 = st.selectbox('Pilih Parameter 1', parameters)
    with col2:
        selected_parameter2 = st.selectbox('Pilih Parameter 2', parameters)

    st.subheader("Korelasi Antar Parameter Cuaca")
    col1, col2 = st.columns([3, 1])
    with col1:
        # Display Scatter Plot with color mapping
        fig_scatter = px.scatter(filtered_data, x=selected_parameter1, y=selected_parameter2,
                                color='status_banjir', color_discrete_map=category_colors,
                                title=f'{selected_parameter1} vs. {selected_parameter2} Correlation')

        st.plotly_chart(fig_scatter, use_container_width=True)
        st.caption('Korelasi Antar Parameter Cuaca dengan *Pearson Correlation Coefficient*')
    
    with col2:
        # Calculate Pearson correlation coefficient
        corr_part = pearsonr(filtered_data[selected_parameter1], filtered_data[selected_parameter2])
        percent = round(corr_part[0] * 100, 2)

        if percent > 50:
            percent_status = 'Korelasi Tinggi'
        elif percent > 30:
            percent_status = 'Korelasi Menengah'
        else:
            percent_status = 'Korelasi Rendah'

        st.markdown(f'##### Korelasi antara {selected_parameter1} dengan {selected_parameter2}')
        st.subheader(f'{percent}%')
        st.markdown(f'##### ***{percent_status}***')
        
#==================================================================
# Weather Parameter Correlation with status_banjir

    filtered_data['status_banjir'] = filtered_data['status_banjir'].map({
        'Tidak':0,
        'Ya':1,
    })

    particle = []
    score = []

    df_score = pd.DataFrame()

    for parameter in parameters:
        tau, p_value = kendalltau(filtered_data[parameter], filtered_data['status_banjir'])
        particle.append(parameter)
        score.append(abs(tau))

    df_score['Particle'] = particle
    df_score['Score'] = score

    st.subheader('Jenis Parameter Cuaca yang Mempengaruhi Kejadian Banjir')
    col1, col2 = st.columns([3, 1])

    with col1:
        fig = go.Figure(data=[go.Pie(labels=particle, 
                                    values=score, 
                                    textinfo='label+percent', 
                                    pull=[0, 0, 0, 0, 0, 0.1])])
        fig.update_layout(
            title='Korelasi Parameter Cuaca terhadap Kejadian Banjir',
            title_font_size=20
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.write('''Parameter Cuaca yang paling mempengaruhi terjadinya 
                 kejadian banjir di Medan yaitu **curah_hujan**''')
        
#==================================================================




