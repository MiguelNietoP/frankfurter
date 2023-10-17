import streamlit as st
from streamlit_lottie import st_lottie
import requests

def app():
    st.title('CURRENCY CONVERTER')

    # st.markdown('<h1 style="font-size: 40px; text-align: justify;">CURRENCY CONVERTER</h1>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size: 20px; text-align: justify;">Currency converter and money value predictor</h1>', unsafe_allow_html=True)
    
    st_lottie(requests.get("https://lottie.host/5d6e1b3c-deb7-4145-ac9c-0513f0dab97f/332WhxMQk1.json").json(), height=250, key="Into1")
    
    url = "https://api.frankfurter.app"
    
    endpoint = f"{url}/currencies"
    respond = requests.get(endpoint).json()
    
    currencies = respond
    # currencies = {value: key for key, value in respond.items()}

    from_currency=st.sidebar.selectbox("Elige Moneda a cambiar",
                                       currencies.keys(),
                                       placeholder='Euro')
    
    to_currency=st.sidebar.selectbox("Elige Moneda a recibir",
                                     currencies.keys(),
                                     placeholder='United States Dollar')
    
    amount = st.number_input('Ingresa la cantidad a convertir', min_value=1, max_value=1_000_000, step=1)
    
    endpoint = f'{url}/latest?amount={amount}&from={from_currency}&to={to_currency}'
    respond = requests.get(endpoint).json()
    
    st.write(respond)
    
    # converted_value = respond['amount']
    
    # st.write(converted_value)
    
    # if Ciudad == "EURO":

    #     st.write('<div style="text-align: justify;"> Escoge las características de tu vivienda en Madrid para obtener un precio .</div>', unsafe_allow_html=True)  
    #     # Slider de selección m2.
    #     st.slider("Selecciona los metros cuadrados de tu vivienda:", min_value=0, max_value=300, value=75, step=1)    

    # elif Ciudad == "DOLLAR":


if __name__ == "__main__":
    app()    
