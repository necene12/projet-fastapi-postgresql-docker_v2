#!/usr/bin/python
#!python
import pandas as pd
df = pd.read_csv('https://query.data.world/s/b6r62f3bsjalbhxttweer2cqzszmbv')
df = df[['id', 'prices.amountMax', 'prices.amountMin', 'prices.availability','prices.condition', 'prices.currency', 'prices.dateSeen',
'prices.isSale', 'prices.merchant', 'prices.shipping',
'prices.sourceURLs', 'asins', 'brand', 'categories', 'dateAdded',
'dateUpdated', 'ean', 'imageURLs', 'keys', 'manufacturer',
'manufacturerNumber', 'name', 'primaryCategories', 'sourceURLs', 'upc','weight']]
# néttoyage des valeurs nulles
df['prices.shipping'] = df['prices.shipping'].fillna('')
df['ean'] = df['ean'].fillna('')
df['manufacturer'] = df['manufacturer'].fillna('')
#écriture du fichier csv source qui sera inséré dans la base de données
df.to_csv('bdd.csv', sep=";", index=False)
print("le fichier source bdd.csv a été généré avec succès")
