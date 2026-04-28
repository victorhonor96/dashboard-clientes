import pandas as pd

# carregar dados
df = pd.read_csv("clientes.csv")

print("=== DADOS ===")
print(df)

# idade média
media_idade = df["idade"].mean()
print("\nIdade média:", media_idade)

# salário médio
media_salario = df["salario"].mean()
print("Salário médio:", media_salario)

# clientes ativos
ativos = df[df["ativo"] == True]
print("\nClientes ativos:", len(ativos))

# maior salário
maior_salario = df["salario"].max()
print("Maior salário:", maior_salario)

# pessoa com maior salário
top = df[df["salario"] == maior_salario]
print("\nQuem ganha mais:")
print(top)

import pandas as pd
import matplotlib.pyplot as plt

# carregar dados
df = pd.read_csv("clientes.csv")

# 📊 Gráfico 1 — Salário por pessoa
df_ordenado = df.sort_values(by="salario", ascending=False)

plt.figure()
plt.bar(df_ordenado["nome"], df_ordenado["salario"])
plt.title("Salário (maior → menor)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 📊 Gráfico 2 — Distribuição de idades
plt.figure()
plt.hist(df["idade"], bins=5)
plt.title("Distribuição de Idade")
plt.xlabel("Idade")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.show()


# 📊 Gráfico 3 — Ativos vs Inativos
ativos = df["ativo"].value_counts()

plt.figure()
plt.pie(ativos, labels=["Ativos", "Inativos"], autopct="%1.1f%%")
plt.title("Clientes Ativos vs Inativos")
plt.show()

# 📊 Gráfico 4 - Quem está ativo
ativos = df[df["ativo"] == True]

df_ordenado = ativos.sort_values(by="salario", ascending=False)

plt.figure()
plt.bar(df_ordenado["nome"], df_ordenado["salario"])

media_salario = ativos["salario"].mean()
plt.axhline(media_salario, linestyle="--")
plt.title(f"Salários dos clientes ativos (média: {media_salario:.2f})")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 📊 Gráfico 5 - Quem não está ativo
inativos = df[df["ativo"] == False]
df_ordenado = inativos.sort_values(by="salario", ascending=False)
plt.figure()
plt.bar(df_ordenado["nome"], df_ordenado["salario"])
media_salario = inativos["salario"].mean()
plt.axhline(media_salario, linestyle="--")
plt.title(f"Salários dos clientes inativos (média: {media_salario:.2f})")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()