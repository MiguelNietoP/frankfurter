import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
from datetime import datetime, timedelta

def app():
    
    # UTILIZAR LAS OTRAS OPCIONES QUE DA FRANKFURTER PARA MOSTRAR MÁS INFORMACIÓN
    # EN ESTA MISMA PESTAÑA, AÑADIR OTRA DEBAJO QUE PERMITA ACCEDER A LAS DEMÁS OPCIONES DE FRANKFUERTER
    
    st.title('CURRENCY CONVERTER')

    # st.markdown('<h1 style="font-size: 40px; text-align: justify;">CURRENCY CONVERTER</h1>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size: 20px; text-align: justify;">Currency converter and money value predictor</h1>', unsafe_allow_html=True)
    
    st_lottie(requests.get("https://lottie.host/5d6e1b3c-deb7-4145-ac9c-0513f0dab97f/332WhxMQk1.json").json(), height=250, key="Into1")
    
    options = st.sidebar.selectbox("Elija lo que quiere hacer",
                                   ['Latest', 'Historical'])
    
    if options == 'Latest':
    
        url = "https://api.frankfurter.app"
        
        endpoint = f"{url}/currencies"
        respond = requests.get(endpoint).json()
        
        currencies = respond
        
        # Damos formato a la lista de opciones de divisas que puede elegir el usuario
        currencies_formated = {f'{value} ({key})' : value for key, value in currencies.items()}

        from_currency=st.sidebar.selectbox("Elige Moneda a cambiar",
                                        currencies_formated.keys(),
                                        index=8)
            
        to_currency=st.sidebar.selectbox("Elige Moneda a recibir",
                                        currencies_formated.keys(),
                                        index=29)
        
        amount = st.sidebar.number_input(f'Ingresa la cantidad a convertir',
                                         min_value=1,
                                         max_value=1_000_000,
                                         step=1)

        # Invertimos los nombres largos por los cortos
        currencies = {value: key for key, value in currencies.items()}
        # Revertimos el formato
        from_currency = currencies_formated[from_currency]
        to_currency = currencies_formated[to_currency]
        # Pasamos de nombre largo a nombre corto
        from_currency = currencies[from_currency]
        to_currency = currencies[to_currency]
        
        init_date = st.sidebar.date_input(label='fecha inicial',
                                value=datetime.today()-timedelta(days=90),
                                min_value=datetime(year=1999, month=1, day=4),
                                max_value=datetime.today()-timedelta(days=10))
        final_date = st.sidebar.date_input(label='Fecha final',
                                value=datetime.today(),
                                min_value=datetime(year=1999, month=1, day=4)+timedelta(days=10),
                                max_value=datetime.today())
        
        init_date = datetime.strftime(init_date, '%Y-%m-%d')
        final_date = datetime.strftime(final_date, '%Y-%m-%d')
        
        # Validamos la opción de elegir la misma divisa
        if from_currency == to_currency: converted_value = amount
        else:
            endpoint = f'{url}/latest?amount={amount}&from={from_currency}&to={to_currency}'
            respond = requests.get(endpoint).json()
            converted_value = respond['rates'][to_currency]
            
            endpoint = f'{url}/{init_date}..{final_date}?from={from_currency}&to={to_currency}'
            respond = requests.get(endpoint).json()
            
            df = pd.DataFrame({'x': [datetime.strptime(x, '%Y-%m-%d') for x in respond['rates'].keys()],
                               'y': [respond['rates'][x][to_currency]*amount for x in respond['rates'].keys()]})
            
            df['y'] = df['y'].replace(0, np.nan)
            
            fig = px.line(x=df['x'], y=df['y'].interpolate(), color_discrete_sequence=['#384842'])
            
            st.plotly_chart(fig)
        
            
        st.header(f'El valor convertido es de: {converted_value} {to_currency}')
        
    elif options == 'Historical':
        
        st.dataframe(pd.read_parquet('Data/historical_original.parquet'))
        
        
        

if __name__ == "__main__":
    app()    
