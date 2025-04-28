import streamlit as st
from pages import contexto
from db import get_client

st.set_page_config(page_title="DataHub – Actividad 1", layout="wide")
st.sidebar.title("Menú")
page = st.sidebar.selectbox("Secciones", ["Inicio", "Contexto Big Data", "CRUD de Ejemplo"])

if page == "Inicio":
    st.title("Sistema DataHub – INFB6052")
    st.write("""**Bienvenido.**
Este prototipo demostrativo está construido con Streamlit y MongoDB.
Use el menú lateral para navegar por las secciones.
""")
elif page == "Contexto Big Data":
    contexto.render()
else:
    st.title("CRUD – Colección `registros`")
    db = get_client()["datahub"]["registros"]
    option = st.radio("Acción", ["Crear", "Leer", "Actualizar", "Eliminar"], horizontal=True)
    if option == "Crear":
        nombre = st.text_input("Nombre")
        valor = st.number_input("Valor", step=1)
        if st.button("Guardar"):
            db.insert_one({"nombre": nombre, "valor": valor})
            st.success("Registro creado")
    elif option == "Leer":
        docs = list(db.find({}, {"_id":0}))
        st.write(docs)
    elif option == "Actualizar":
        nombre = st.text_input("Nombre del registro a actualizar")
        nuevo_valor = st.number_input("Nuevo valor", step=1)
        if st.button("Actualizar"):
            db.update_one({"nombre": nombre}, {"$set": {"valor": nuevo_valor}})
            st.success("Actualizado")
    else:
        nombre = st.text_input("Nombre del registro a eliminar")
        if st.button("Eliminar"):
            db.delete_one({"nombre": nombre})
            st.success("Eliminado")
