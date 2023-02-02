#!/usr/bin/env python
# coding: utf-8

import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import style

animales = pd.read_csv('zoo.csv', sep = ',')

for i in range(0, len(animales)):
    if animales['class_type'][i] == 1:
        animales['class_type'][i] = 'Mammal'
    if animales['class_type'][i] == 2:
        animales['class_type'][i] = 'Bird'
    if animales['class_type'][i] == 3:
        animales['class_type'][i] = 'Reptile'
    if animales['class_type'][i] == 4:
        animales['class_type'][i] = 'Fish'
    if animales['class_type'][i] == 5:
        animales['class_type'][i] = 'Amphibian'
    if animales['class_type'][i] == 6:
        animales['class_type'][i] = 'Bug'
    if animales['class_type'][i] == 7:
        animales['class_type'][i] = 'Invertebrate'

plt.hist(animales['class_type'], width=0.5, color='blue')
plt.title('No. de Animales por Clase en el Zoo')