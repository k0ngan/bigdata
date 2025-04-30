# home.py
import streamlit as st
from pages import contexto
from db import get_client
import pandas as pd # Añade esta importación
# Configuracion inicial de la pagina
st.set_page_config(page_title="DataHub – Actividad 1", layout="wide")

# Menu lateral
st.sidebar.title("Menú de Navegación")
page = st.sidebar.selectbox("Secciones", ["Inicio", "Contexto Big Data", "CRUD de Ejemplo"])

if page == "Inicio":
    st.title("Sistema DataHub – INFB6052")
    st.image("https://webbetel-2.s3.us-east-2.amazonaws.com/game/bigdata33.jpeg", use_column_width=True)
    st.markdown("""
    **Bienvenido al Sistema DataHub.**

    Este prototipo demostrativo está construido utilizando Streamlit y MongoDB. 

    Navegue entre las secciones para explorar conceptos de Big Data y la gestión básica de datos.

    **Bibliografía:**
    - Provost, F., & Fawcett, T. (2013). *Data Science for Business.* O'Reilly Media.
    - Marr, B. (2016). *Big Data in Practice.* Wiley.
    """)

elif page == "Contexto Big Data":
    contexto.render()

else:
    st.title("CRUD de Ejemplo - Colección `registros`")
    db = get_client()["datahub"]["registros"]

    # Seleccion de operacion CRUD
    option = st.radio("Acción", ["Crear", "Leer", "Actualizar", "Eliminar"], horizontal=True)

    if option == "Crear":
        nombre = st.text_input("Nombre")
        valor = st.number_input("Valor", step=1)
        if st.button("Guardar"):
            db.insert_one({"nombre": nombre, "valor": valor})
            st.success("Registro creado exitosamente")

    elif option == "Leer":
        st.subheader("Registros en la Base de Datos")
        docs = list(db.find({}, {"_id": 0}))

        if docs: # Verifica si hay documentos antes de mostrar
            # Mostrar los datos en formato tabla
            st.write("Datos en formato tabla:")
            st.write(docs)

            # --- Añadir Visualización ---
            st.subheader("Visualización de Datos")

            # Convertir los datos a un DataFrame de pandas
            # Asegúrate de que la estructura de tus documentos en MongoDB sea consistente
            # Por ejemplo, si tienen campos 'nombre' y 'valor'
            df = pd.DataFrame(docs)

            # Ejemplo de gráfico: Gráfico de barras del 'valor' por 'nombre'
            # Asegúrate de que las columnas 'nombre' y 'valor' existan en tus documentos
            if 'nombre' in df.columns and 'valor' in df.columns:
                st.bar_chart(df.set_index('nombre')['valor'])
                st.write("Gráfico de barras del valor por nombre.")
            else:
                st.warning("No se encuentran las columnas 'nombre' o 'valor' para visualizar.")

            # Puedes añadir otros tipos de gráficos si tienen otros tipos de datos numéricos o categóricos
            # Ejemplo:
            # st.line_chart(df['valor'])
            # st.area_chart(df.set_index('nombre')['valor'])


        else:
            st.info("No hay registros en la base de datos para mostrar.")

    elif option == "Actualizar":
        nombre = st.text_input("Nombre del registro a actualizar")
        nuevo_valor = st.number_input("Nuevo valor", step=1)
        if st.button("Actualizar"):
            db.update_one({"nombre": nombre}, {"$set": {"valor": nuevo_valor}})
            st.success("Registro actualizado exitosamente")

    else:  # Eliminar
        nombre = st.text_input("Nombre del registro a eliminar")
        if st.button("Eliminar"):
            db.delete_one({"nombre": nombre})
            st.success("Registro eliminado exitosamente")
