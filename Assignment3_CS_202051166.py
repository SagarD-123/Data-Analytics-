# -*- coding: utf-8 -*-

**CS/IT 312 : Data Analytics and Visualization**

**Sagar Deware (202051166)**


pip install joypy

# Commented out IPython magic to ensure Python compatibility.

# importing all the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from joypy import joyplot 
import seaborn as sns
# %matplotlib inline 
# for plotting graph against the code

# importing dataset 
csvFile = pd.read_csv('grains_production_india_from_2001_to_2017.csv')
csvFile.head()

cerealsFile = csvFile[[
'Year', 'Food Grains (Cereals) - Rice (000 tonnes)',
       'Food Grains (Cereals) - Jowar (000 tonnes)',
       'Food Grains (Cereals) - Bajra (000 tonnes)',
       'Food Grains (Cereals) - Maize (000 tonnes)',
       'Food Grains (Cereals) - Ragi (000 tonnes)',
       'Food Grains (Cereals) - Small Millets (000 tonnes)',
       'Food Grains (Cereals) - Wheat (000 tonnes)',
       'Food Grains (Cereals) - Barley (000 tonnes)',
]].copy()

cerealsFile.head()

cereals_point_plot = sns.pointplot(data=cerealsFile)

cereals_box_plot = sns.boxplot(data = cerealsFile)

pulsesFile = csvFile[['Food Grains (Pulses) - Gram (000 tonnes)','Food Grains (Pulses) - Tur (000 tonnes)','Food Grains (Pulses) - Other Pulses (000 tonnes)']]
pulsesFile

plot = sns.violinplot(data=pulsesFile['Food Grains (Pulses) - Gram (000 tonnes)'])

pulses_voilin_plot = sns.violinplot(data=pulsesFile)

sns.stripplot(data=pulsesFile,color='0.3')
sns.violinplot(data=pulsesFile)

pulses_box_plot = sns.boxplot(data = pulsesFile)

oilseedsFile = csvFile[['Oilseeds - Ground-nuts (000 tonnes)',
       'Oilseeds - Sesamum (000 tonnes)',
       'Oilseeds - Rapeseed and Mustard (000 tonnes)',
       'Oilseeds - Linseed (000 tonnes)',
       'Oilseeds - Castor seed (000 tonnes)']]

plt.subplots(figsize=(7,7))
oilseed_strip_plot = sns.stripplot(data=oilseedsFile)

oilseed_joy_plot = joyplot(oilseedsFile,overlap=0,grid=True,color='Red')

oil_seed_hist_joy_plot = joyplot(data=oilseedsFile,overlap=0,hist=True,color='Yellow')