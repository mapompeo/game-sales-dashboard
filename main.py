import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # Caminho do arquivo base
    base_path = "vgsales.csv"
    if not os.path.exists(base_path):
        print("Arquivo base não encontrado:", base_path)
        return

    # 1. Carrega o CSV
    df = pd.read_csv(base_path)


    print("Dimensões da base:", df.shape)
    print("Colunas da base:", df.columns.tolist())
    print("\nTipos de dados:\n", df.dtypes)


    df = df.dropna(subset=["Year", "Publisher", "Genre"]) 
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df = df.dropna(subset=["Year"]) 
    df["Year"] = df["Year"].astype(int)


    print("\nDepois da limpeza, dimensões:", df.shape)

   
    num_cols = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]

    cat_cols = ["Platform", "Genre", "Publisher"]

    # 5. Cálculo de médias e desvios padrão
    print("\nMédias das colunas de venda:")
    print(df[num_cols].mean())
    print("\nDesvios padrão das colunas de venda:")
    print(df[num_cols].std())



    filtro_simples = df[df["Year"] > 2010]
    filtro_simples.to_csv("filtrado_simples.csv", index=False)
    print("CSV filtrado simples salvo: filtrado_simples.csv")

    filtro_composto = df[
        (df["Genre"] == "Action") &
        (df["Year"] > 2010) &
        (df["Global_Sales"] > 1.0)
    ]
    filtro_composto.to_csv("filtrado_composto.csv", index=False)
    print("CSV filtrado composto salvo: filtrado_composto.csv")

    media_por_genero = df.groupby("Genre")["Global_Sales"].mean().sort_values(ascending=False)
    print("\nMédia de vendas globais por gênero:")
    print(media_por_genero.head(10))

  
    top10_genero = media_por_genero.head(10)
    plt.figure(figsize=(10,6))
    top10_genero.plot(kind="bar")
    plt.title("Média de Vendas Globais por Gênero (Top 10)")
    plt.ylabel("Média Global Sales (milhões)")
    plt.xlabel("Gênero")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("grafico_media_genero.png")
    plt.clf()
    print("Gráfico salvo: grafico_media_genero.png")

  
    contagem_plataforma = df["Platform"].value_counts().head(10)
    print("\nTop 10 plataformas por número de jogos:")
    print(contagem_plataforma)

    plt.figure(figsize=(10,6))
    contagem_plataforma.plot(kind="bar")
    plt.title("Número de Jogos por Plataforma (Top 10)")
    plt.ylabel("Contagem de Jogos")
    plt.xlabel("Plataforma")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("grafico_contagem_plataforma.png")
    plt.clf()
    print("Gráfico salvo: grafico_contagem_plataforma.png")

    media_por_editora = df.groupby("Publisher")["Global_Sales"].mean().sort_values(ascending=False).head(10)
    print("\nTop 10 editoras por média de vendas globais:")
    print(media_por_editora)

    plt.figure(figsize=(10,6))
    media_por_editora.plot(kind="bar")
    plt.title("Média de Vendas Globais por Editora (Top 10)")
    plt.ylabel("Média Global Sales (milhões)")
    plt.xlabel("Editora")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("grafico_media_editora.png")
    plt.clf()
    print("Gráfico salvo: grafico_media_editora.png")

    print("\nProcessamento concluído com sucesso.")

if __name__ == "__main__":
    main()
