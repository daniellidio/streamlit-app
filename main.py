import streamlit as st
import pandas as pd


def main():
    st.image('logo.png')
    st.title("App para análise de dados.")
    file = st.file_uploader("Escolha um arquivo .csv para iniciar a análise:", type = 'csv')
    if file is not None:
        df = pd.read_csv(file)
        st.header("Informações básicas do arquivo:")
        st.subheader("Número de linhas:")
        st.write(df.shape[0])
        st.subheader("Número de colunas:")
        st.write(df.shape[1])
        st.subheader("Nome das colunas e tipos de dados por coluna:")
        st.write(df.dtypes)
        st.subheader("Descrição geral das colunas:")
        st.write(df.describe())
        st.subheader("Linhas iniciais e finais:")
        slider_head = st.slider("Escolha quantas linhas iniciais do dataframe você quer visualizar:", 1, 20)
        st.dataframe(df.head(slider_head))
        slider_tail = st.slider("Escolha quantas linhas finais do dataframe você quer visualizar:", 1, 20)
        st.dataframe(df.tail(slider_tail))
        


if __name__ == "__main__":
    main()