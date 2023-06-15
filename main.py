import streamlit as st
import pandas as pd
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
owners = ["Arthur Kuahara", "Eduardo Dias", "João Lucas","João Morais", "Othávio Ruddá"]
visualization = Vis()
visualization.readTexts()
# Página inicial
if selected_option == "Home":
    st.header("Bem-vindo ao trabalho de visualização de dados!")
    # st.write("Aqui você encontrará informações sobre nossos cursos, professores e muito mais.")

    st.subheader("Contribuintes:")
    for i in owners:
        st.write(i)

    st.subheader("Sumário")
    for i in menu_options:
        st.write("\t     -"+i)


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

# Página de contato
elif selected_option == "Dados":
    st.header("Dados Utilizados")
    st.write("descrevemos um pouco dos dados")


# Página de professores
elif selected_option == "Visualização 1":
    st.header("Visualização 1")
    st.write("primeira visualização")
    visualization.plotVis1()
    st.write(visualization.texts[0])

# Página de dados
elif selected_option == "Visualização 2":
    st.header("Visualização 3")
    st.write("terceira visualização")
    visualization.plotVis2()
    st.write(visualization.texts[1])


elif selected_option == "Visualização 3":
    st.header("Visualização 3")
    st.write("terceira visualização")
    visualization.plotVis3()
    st.write(visualization.texts[2])

elif selected_option == "Visualização 4":
    st.header("Visualização 3")
    st.write("terceira visualização")
    visualization.plotVis4()
    st.write(visualization.texts[3])

elif selected_option == "Visualização 5":
    st.header("Visualização 3")
    st.write("terceira visualização")
    visualization.plotVis5()
    st.write(visualization.texts[4])

elif selected_option == "Visualização 6":
    st.header("Visualização 3")
    st.write("terceira visualização")
    visualization.plotVis6()
    st.write(visualization.texts[5])