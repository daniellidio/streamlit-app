import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np


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
        st.subheader("Quantidade de observações únicas no arquivo (por coluna):")
        st.write(df.nunique()) 
        st.subheader("Quantidade de observações nulas no arquivo (por coluna):")
        st.write(df.isna().sum())
        st.subheader("Escolha o tipo de gráfico para plotar:")
        select_graph = st.selectbox("Escolha o gráfico e depois selecione as variáveis que queira visualizar", ("", "Scatterplot", "Boxplot", "Histogram", "Correlation Heatmap"))
        if select_graph == "Scatterplot":
            st.markdown("Selecione as variáveis:")
            var_x = st.selectbox("Selecione a variável para o eixo x:", (df.columns))
            var_y = st.selectbox("Selecione a variável para o eixo y:", (df.columns))
            sns.scatterplot(x = df[var_x], y = df[var_y])
            st.pyplot()
            st.write("A correlação entre as duas variáveis é", (df[var_x].corr(df[var_y])).round(3))
        if select_graph == "Boxplot":
            st.markdown("Selecione a variável:")
            var = st.selectbox("Selecione uma variável:", (df.columns))
            if df.dtypes[var] == np.int64  or df.dtypes[var] == np.float64:
                sns.boxplot(x = df[var])
                st.pyplot()
            else:
                st.markdown("Essa variável não é numérica, escolha outra.")
        if select_graph == "Histogram":
            st.markdown("Selecione a variável:")
            var = st.selectbox("Selecione uma variável:", (df.columns))
            if df.dtypes[var] == np.int64  or df.dtypes[var] == np.float64:
                sns.distplot(df[var])
                st.pyplot()
            else:
                st.markdown("Essa variável não é numérica, escolha outra.")
        if select_graph == "Correlation Heatmap":
            corr = df.corr()
            sns.heatmap(corr, xticklabels = corr.columns, yticklabels = corr.columns, annot = True, linewidths = .5, cmap = "Blues")
            st.pyplot()


if __name__ == "__main__":
    main()
