import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tratamentos import Vis
from PIL import Image

# Configurações de página
st.set_page_config(
    page_title="Visualização de Dados",
    page_icon="🎓",
    layout="wide"
)

# Título e cabeçalho
st.title("Visualização de Dados")
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
        "Contribuição": ["Desenvolveu a visualização 5 e participou do desenvolvimento do  design do site e do processo de deploy do sistema web.",
                         "Desenvolveu a visualização 1 e 6 e participou do processo de deploy do sistema web.",
                         "Desenvolveu a visualização 4, participou do desenvolvimento da visualização 6 e participou do processo de deploy do sistema web.",
                         "Desenvolveu a visualização 3 e participou do desenvolvimento do  design do site e do processo de deploy do sistema web.",
                         "Desenvolveu a visualização 2 e participou do desenvolvimento do  design do site e do processo de deploy do sistema web."]
    }
    cursos_df = pd.DataFrame(contributions)
    cursos_df = cursos_df.reset_index(drop=True)
    st.dataframe(cursos_df)

# Página de contato
elif selected_option == "Dados":
    st.header("Dados Utilizados")
    arquivo = open('texts/dados.txt', 'r', encoding='utf-8')
    text = arquivo.read()
    arquivo.close()
    st.write(text)


# Página de professores
elif selected_option == "Visualização 1":
    st.header("Visualização 1")
    visualization.plotVis1()
    st.write(visualization.texts[0])

# Página de dados
elif selected_option == "Visualização 2":
    st.header("Visualização 2")
    visualization.plotVis2()
    st.write(visualization.texts[1])


elif selected_option == "Visualização 3":
    st.header("Visualização 3")
    visualization.plotVis3()
    st.write(visualization.texts[2])

elif selected_option == "Visualização 4":
    st.header("Visualização 4")
    visualization.plotVis4()
    st.write(visualization.texts[3])

elif selected_option == "Visualização 5":
    st.header("Visualização 5")
    visualization.plotVis5()
    visualization.plotVis6()
    st.write(visualization.texts[5])
    
elif selected_option == "Visualização 6":
    st.header("Visualização 6")
    visualization.plotVis7()
    st.write(visualization.texts[6])