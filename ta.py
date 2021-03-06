# -*- coding: utf-8 -*-
"""TA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PWasWYG-J8REl5WG1qiAgQ_DUAMbLZrZ

# Instalasi Library

Bagian ini berisi code untuk instalasi library mlxtend untuk ASSOCIATION RULE yang akan dirancang.
"""

!pip install mlxtend

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

"""Membaca data set yang berisi nilai mahasiswa yang menjadi syarat pre-quisite MK Pilihan"""

df = pd.read_csv('dt_set.csv')
print(df)

