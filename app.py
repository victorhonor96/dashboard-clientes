import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

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