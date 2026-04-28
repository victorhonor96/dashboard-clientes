import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
st.subheader("💰 Salário por cliente")

df_ordenado = df.sort_values(by="salario", ascending=False)

fig, ax = plt.subplots()
ax.bar(df_ordenado["nome"], df_ordenado["salario"])
plt.xticks(rotation=45)

st.pyplot(fig)

# média salarial
media = df["salario"].mean()
st.metric("Salário médio", f"{media:.2f}")

# comparação ativos vs inativos
st.subheader("📊 Comparação geral")

media_grupo = pd.read_csv("clientes.csv").groupby("ativo")["salario"].mean()

st.bar_chart(media_grupo)