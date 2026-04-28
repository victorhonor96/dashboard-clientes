import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# features (entrada)
X = df[["idade", "ativo"]]

# alvo (o que queremos prever)
y = df["salario"]

# converter booleano pra número
X["ativo"] = X["ativo"].astype(int)

# dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# modelo
modelo = RandomForestRegressor()
modelo.fit(X_train, y_train)

# precisão
score = modelo.score(X_test, y_test)

st.metric("Acurácia do modelo", f"{score:.2f}")


# título
st.title("📊 Dashboard de Clientes")

# carregar dados
df = pd.read_csv("clientes.csv")

# mostrar dados
st.subheader("Dados")
st.write(df)

# filtro interativo
status = st.selectbox("Filtrar por status:", ["Todos", "Ativos", "Inativos"])

if status == "Ativos":
    df = df[df["ativo"] == True]
elif status == "Inativos":
    df = df[df["ativo"] == False]

# gráfico de salários


st.subheader("💰 Salário por cliente (interativo)")

df_ordenado = df.sort_values(by="salario", ascending=False)

fig = px.bar(
    df_ordenado,
    x="nome",
    y="salario",
    title="Salário por Cliente",
    text="salario"
)

st.plotly_chart(fig, use_container_width=True)

# média salarial
media = df["salario"].mean()
st.metric("Salário médio", f"{media:.2f}")

# comparação ativos vs inativos
st.subheader("📊 Comparação geral")

media_grupo = pd.read_csv("clientes.csv").groupby("ativo")["salario"].mean().reset_index()

media_grupo["ativo"] = media_grupo["ativo"].map({True: "Ativos", False: "Inativos"})

fig2 = px.bar(
    media_grupo,
    x="ativo",
    y="salario",
    text="salario",
    title="Salário médio por status"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("🔮 Prever salário")

idade_input = st.number_input("Idade", 18, 80, 30)
ativo_input = st.selectbox("Ativo?", ["Sim", "Não"])

ativo_num = 1 if ativo_input == "Sim" else 0

if st.button("Prever salário"):
    previsao = modelo.predict([[idade_input, ativo_num]])
    st.success(f"Salário previsto: R$ {previsao[0]:.2f}")