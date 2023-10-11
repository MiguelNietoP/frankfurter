#Importamos las librerias necesarias.
import streamlit as st
import pandas as pd
import matplotlib as plt
import plotly.express as px
from streamlit_lottie import st_lottie  #Libreria necesaria para trabajar con lotties archivos json animados
import requests
from streamlit_option_menu import option_menu    #Libreria necesaria para trabajar con lotties archivos json animados
from datetime import date,datetime

#Importamos funciones de codigo en otros archivos
from APP import app
from autores import Autores

# Cargamos los DataFrames necesarios para el proyecto. Tengo todos los del EDA.


#df_precios = pd.read_csv("DF/Precios por mes.csv")




#Creamos el marco de trabajo de Streamlit.

def main():

    st.set_page_config(
    page_title="CAMBIO DE DIVISA",
    page_icon=":€",
    )

    # Creamos un MENÚ.
    opcion=st.sidebar.selectbox("Menú", 
                                ["APP",
                                 "AUTORES"])
   
    ####################################  APP #######################################################
    #################################################################################################
    #################################################################################################

    if opcion == 'APP':
        app()

    #################################### AUTORES ####################################################
    #################################################################################################
    #################################################################################################
    

    elif opcion == 'AUTORES':  
        Autores()

    
    
    ############################# CERRAMOS ESTRUCTURA DEL MODELO ########################
    ############################################################################################
    ############################################################################################

if __name__ == "__main__":
    main()