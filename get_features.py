#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:43:56 2021

@author: Natasha
"""

"""

Um die Feature 'Number of stopwords' zu implementieren, 
musste ich ein neues File mit der Funktion 'count_stopwords' erstellen
und 2 Zeilen in die Datei 'get_features' hinzufügen.

Also ich habe schon ein DataFrame mit punct. Features erstellt und dann 
ledeglich eine neue Spalte mit dem neuen Feature hinzugefügt.

"""

import pandas as pd
import click
from feature_class_punctuation import PunctFeatures
from Word_features import count_stopwords

#übergebe file Data_train.csv
@click.command()
@click.argument('data', required=True)

def main(data):

    df = pd.read_csv(data, usecols=('ID', 'text', 'label'))
    data_with_features = PunctFeatures(df).outputter()
    data_with_features['number_stopwords'] = data_with_features['text'].apply(count_stopwords)
    data_with_features['number_stopwords'] = data_with_features['number_stopwords'] / data_with_features['text_length']
    data_with_features.to_csv("Data_train_features.csv")

if __name__ == '__main__':
    main()
