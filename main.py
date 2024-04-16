import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


#UNDERSTANDING THE DATASET

models = pd.read_csv('data/faces.csv')
print(models.shape)  # (262, 4) 262 righe per 4 colonne
print(models.info)
print(models.dtypes)

#DATASET CLEANING

print(f'Are there any duplicate values in the dataset? {models.duplicated().values.any()}')
print(f'Are there any NaN values in the dataset? {models.isna().values.any()}')
#Checking for columns that have NaN values.
print(models.isna().sum())

print(models.head(10))



#DATA VISUALIZATION
model_count = models['model'].value_counts()
print(model_count)
plt.figure(figsize=(10, 6))
model_count.head(10).plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Top 10 Modelle con più Copertine di Riviste')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Estrai l'anno dalla colonna 'date'
models['year'] = pd.to_datetime(models['date']).dt.year

# Trova l'hex più comune per ogni anno
most_common_hex_per_year = models.groupby('year')['tone'].agg(lambda x: x.value_counts().index[0])

# Converti l'indice in interi
most_common_hex_per_year.index = most_common_hex_per_year.index.astype(int)

# Crea il grafico a dispersione migliorato per mostrare il colore hex più comune per ogni anno
plt.figure(figsize=(12, 8))
plt.scatter(most_common_hex_per_year.index, most_common_hex_per_year, color=most_common_hex_per_year, s=100, alpha=0.7)
plt.title('Colore skin tone più presente per anno')
plt.xlabel('Anno')
plt.ylabel('Valore Hex')
plt.grid(True, axis='x')

# Ruota i valori sull'asse x per migliorare la leggibilità e aggiungi spazi tra i valori
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.15)

plt.tight_layout()

# Mostra il grafico
plt.show()