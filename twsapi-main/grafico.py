import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ler o arquivo de análise
df = pd.read_csv('analise.csv')

# Ordenar por alavancagem
df_sorted = df.sort_values(by='alavancagem')

# Seaborn settings
sns.set_style("whitegrid")
plt.figure(figsize=(15,10))

# Plotar todas as alavancagens
sns.barplot(x='codigo_conta', y='alavancagem', data=df_sorted, palette='viridis')

# Linha média de alavancagem
mean_alavancagem = df_sorted['alavancagem'].mean()
plt.axhline(mean_alavancagem, color='red', linestyle='dashed', linewidth=1, label=f'Média: {mean_alavancagem:.2f}')

# Identificando os top 5 mais e menos alavancados
top_5 = df_sorted.tail(5)
bottom_5 = df_sorted.head(5)

for index, value in enumerate(top_5['alavancagem']):
    plt.text(top_5['codigo_conta'].index[index], value + 0.02, 'Top ' + str(5 - index), color='black', ha="center")
    
for index, value in enumerate(bottom_5['alavancagem']):
    plt.text(bottom_5['codigo_conta'].index[index], value + 0.02, 'Bottom ' + str(index + 1), color='black', ha="center")

# Ajustar labels e títulos
plt.xticks(rotation=90)
plt.ylabel('Alavancagem')
plt.xlabel('Código de Conta')
plt.title('Alavancagem por Código de Conta')
plt.legend()

# Mostrar o gráfico
plt.tight_layout()
plt.show()
