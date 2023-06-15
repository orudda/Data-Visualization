import streamlit as st
import pandas as pd
import os
try:
    import matplotlib
except ImportError:
    os.system("pip install matplotlib")
try:
    import seaborn
except ImportError:
    os.system("pip install seaborn")
import matplotlib.pyplot as plt
import seaborn as sns
from tratamentos import Vis

# Configurações de página
st.set_page_config(
    page_title="Visualiação de Dados",
    page_icon="🎓",
    layout="wide"
)

# Título e cabeçalho
st.title("Visualiação de Dados")
# st.markdown("Bem-vindos ao site da Escola XYZ!")

# Menu de navegação
menu_options = ["Home", "Contribuições", "Dados", "Visualização 1", "Visualização 2", "Visualização 3", "Visualização 4", "Visualização 5", "Visualização 6"]
selected_option = st.sidebar.selectbox("Navegação", menu_options)

#Contribuintes
owners = ["Arthur kunavara", "Eduardo Dias", "João Lucas","João Morais", "Othávio Ruddá"]

# Página inicial
if selected_option == "Home":
    st.header("Bem-vindo ao trabalho de visualização de dados!")
    # st.write("Aqui você encontrará informações sobre nossos cursos, professores e muito mais.")

    st.subheader("Contribuintes:")
    for i in owners:
        st.write(i)

    st.subheader("Sumário")
    for i in menu_options:
        st.write(i)


elif selected_option == "Contribuições":
    st.header("Contribuições")
    st.write("Nessa página descrevemos as contribuições de cada aluno")

   
    contributions = {
        "Contribuinte": owners,
        # "contribuição": owners,
        "Contribuição": ["5,6","4","1","2","3"],
    }
    cursos_df = pd.DataFrame(contributions)
    cursos_df = cursos_df.reset_index(drop=True)
    st.dataframe(cursos_df)

# Página de professores
elif selected_option == "Visualização 1":
    st.header("Visualização 1")
    st.write("primeira visualização")
    visualization = Vis()
    visualization.plotVis1()



# Página de contato
elif selected_option == "Dados":
    st.header("Dados Utilizados")
    st.write("descrevemos um pouco dos dados")

# Página de dados
elif selected_option == "Visualização 2":
    st.header("Visualização 3")
    st.write("terceira visualização")
    visualization = Vis()
    visualization.plotVis2()


elif selected_option == "Visualização 3":
    st.header("Visualização 3")
    st.write("terceira visualização")
    visualization = Vis()
    visualization.plotVis3()

elif selected_option == "Visualização 4":
    st.header("Visualização 3")
    st.write("terceira visualização")
    visualization = Vis()
    visualization.plotVis4()

elif selected_option == "Visualização 5":
    st.header("Visualização 3")
    st.write("terceira visualização")
    visualization = Vis()
    visualization.plotVis5()

elif selected_option == "Visualização 6":
    st.header("Visualização 3")
    st.write("terceira visualização")
    visualization = Vis()
    visualization.plotVis6()