# pages/contexto.py
import streamlit as st

def render():
    st.title("Contexto Big Data")
    st.markdown("""
    ## ¿Qué es Big Data?
    Big Data se refiere a conjuntos de datos que son tan grandes o complejos que las aplicaciones de procesamiento de datos tradicionales no son adecuadas para tratarlos. 

    ### Características principales:
    - **Volumen**: Grandes cantidades de datos.
    - **Velocidad**: Rápida generación y procesamiento de datos.
    - **Variedad**: Diversos tipos de datos estructurados y no estructurados.
holaaaaa soy gayyy
    ## Casos Reales de Uso
    1. **Sector Salud**: 
       - Predicción de enfermedades mediante análisis de grandes volúmenes de registros médicos.
       - Fuente: Provost & Fawcett, *Data Science for Business*.

    2. **Retail**:
       - Personalización de ofertas en tiempo real mediante análisis de comportamiento de compra.
       - Fuente: Marr, *Big Data in Practice*.

    ## Importancia de Big Data
    Big Data permite a las organizaciones tomar decisiones basadas en evidencias, mejorar la eficiencia operativa y ofrecer mejores servicios a sus usuarios.
    """)
