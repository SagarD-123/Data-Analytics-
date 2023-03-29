# -*- coding: utf-8 -*-
"""

**Assignment 05 **

**Sagar Deware (202051166)**
"""

!pip install squarify
!pip install joypy

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms
from statsmodels.graphics.mosaicplot import mosaic
from joypy import joyplot 
import squarify 
import plotly.express as px

"""Merge the data frames containing Egg and Milk production. Present the information in the merged data frame using any two appropriate plots.

DATA REPRESENTATION
"""

Egg_csv=pd.read_csv(r"Egg_Production_2007_2012.csv")
Milk_csv=pd.read_csv(r"Milk_Production_2007_2012.csv")
Egg_csv.rename(columns={'2007-08 (In lakh nos.)': '2007-08','2008-09 (In lakh nos.)': '2008-09','2009-10 (In lakh nos.)': '2009-10','2010-11 (In lakh nos.)': '2010-11','2011-12 (In lakh nos.)': '2011-12'}, inplace=True)

merge_csv = (pd.concat([Egg_csv, Milk_csv], axis=1, keys=('Eggs','Milk'))
         .swaplevel(1,0, axis=1)
         .sort_index(axis=1, level=1))
del merge_csv["States/Uts"]
column=df_1["States/Uts"]
merge_csv["States/Uts"]=column
merge_csv=merge_csv.set_index('States/Uts')
merge_csv=merge_csv.stack()
merge_csv = merge_csv.rename_axis(['States/Uts','Item'])
merge_csv = merge_csv.drop("Total")

merge_csv["Total"] = merge_csv.sum(axis=1)
Total_csv=merge_csv["Total"]
Total_csv=Total_csv.iloc[0:18].unstack()
df1_total_array=Total_csv.to_numpy().T

"""FOLLWING ARE METHODS USED TO REPRESENT THE DATA IN GOOD WAY:
1.NESTED -PIE CHART
2.TREE MAP
3.PARELLEL SETS

NESTED PIE-CHART
"""

fig, ax = plt.subplots()
size = 0.3
cmap=plt.get_cmap("tab20c")
outer_colors = cmap([1,2,3])
inner_colors = cmap([4,5, 6, 7, 8,9])
outerlabels=df1_total.columns.tolist()
innerlabels=df1_total.index.tolist()
l2=ax.pie(df1_total_array.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))
l1=ax.pie(df1_total_array.sum(axis=1), radius=1, colors=outer_colors, labels =outerlabels,
       wedgeprops=dict(width=size, edgecolor='w'))
ax.legend(innerlabels,loc=(1,0.5))
ax.set(aspect="equal", title='Pie plot with ax.pie')
plt.show()

"""TREE MAP"""

df = df1.reset_index()
df=df[0:12]
fig = px.treemap(df, path=["States/Uts","Item"], values="Total")
fig.show()

"""PARELLEL SETS"""

data1 = df.set_index(['States/Uts',"Item"])
data1=data1.stack()
data1=data1.reset_index()
data1.columns=["States/Uts","Item","Year","Measure"]

fig = px.parallel_categories(data1,dimensions=['States/Uts','Item',"Year"],color="Measure")
fig.show()