import streamlit as st 
# import plotly_express as px 
import pandas as pd
import plotly.graph_objects as go

#config
st.set_option('deprecation.showfileUploaderEncoding', False)

#title
st.title('Aplikasi Konturing Mandiri')
st.write('Web App untuk Konturing')

#sidebar
st.sidebar.subheader("Pengaturan")

#uploadedfile
uploaded_file = st.sidebar.file_uploader(label="Unggah CSV nya bos", type=['csv'])

global df

if uploaded_file is not None:
    print(uploaded_file)
    print('Ke Uploaded Nih')
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(st.write('Error Nih Bro'))


global numeric_columns
try:
    st.write(df)
    df.apply(pd.to_numeric)
    print(df.info())
    numeric_columns = list(df.select_dtypes(['float','int64']).columns)
    print(numeric_columns)
except Exception as e:
    print(e)
    st.write('## Please Upload File Nya Atulah')



#select widget
chart_select = st.sidebar.selectbox(
    label="Mau Ngapain?",
    options=['Konturing','Konturang']
)

if chart_select == 'Konturing':
    st.sidebar.subheader("Pilih Kolomnya")
    try:
        x_values = st.sidebar.selectbox('X Axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y Axis', options=numeric_columns)
        z_values = st.sidebar.selectbox('Z Axis', options=numeric_columns)
        # plot = px.scatter(data_frame=df, x=x_values, y=y_values)
        plot = go.Figure()
        plot.add_trace(go.Contour(x=df[x_values], y=df[y_values], z=df[z_values] ))
        plot.add_trace(go.Scatter(x=df[x_values], y=df[y_values], mode='markers', text=df[z_values]))
        plot.update_layout(title='Peta Kontur', template='plotly_white')
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Konturang':
    st.write('## Kagak ada konturang!')
