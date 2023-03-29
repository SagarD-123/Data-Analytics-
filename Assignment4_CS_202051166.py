# -*- coding: utf-8 -*-
"""
#                                    Lab Assignment-4 
### Name -Sagar Deware
### ID - 202051166
### Section - 2

### Import statements
"""

pip install joypy

import pandas as pd
import seaborn as sns
import numpy as np
import IPython
import matplotlib.pyplot as plt
from matplotlib import transforms
from statsmodels.graphics.gofplots import qqplot
from joypy import joyplot
from IPython.display import display

Egg_CsvFile=pd.read_csv(r"Egg_Production_2007_2012.csv")
Milk_CsvFile=pd.read_csv(r"Milk_Production_2007_2012.csv")
Egg_CsvFile.rename(columns={'2007-08 (In lakh nos.)': '2007-08','2008-09 (In lakh nos.)': '2008-09','2009-10 (In lakh nos.)': '2009-10','2010-11 (In lakh nos.)': '2010-11','2011-12 (In lakh nos.)': '2011-12'}, inplace=True)

"""### Task - 1

#### Method - 1
"""

Merge_CsvFile = (pd.concat([Egg_CsvFile, Milk_CsvFile], axis=1, keys=('Eggs','Milk'))
         .swaplevel(0,1, axis=1)
         .sort_index(axis=1, level=0))
del Merge_CsvFile["States/Uts"]
column=Egg_CsvFile["States/Uts"]
Merge_CsvFile["States/Uts"]=column
Merge_CsvFile=Merge_CsvFile.set_index("States/Uts")
Merge_CsvFile=pd.DataFrame(Merge_CsvFile)
display(Merge_CsvFile)

"""### Task - 2"""

MilkChart=Milk_CsvFile[["States/Uts","2007-08"]]
list=["Gujarat", "Kerala", "Andhra Pradesh", "Uttar Pradesh" ," Punjab"]
MilkChart=MilkChart.loc[(MilkChart['States/Uts'] ==list[0])|(MilkChart['States/Uts'] ==list[1])|(MilkChart['States/Uts'] ==list[2])|(MilkChart['States/Uts'] ==list[3])|(MilkChart['States/Uts'] ==list[4])]
colors = sns.color_palette('pastel')[0:5]
label=MilkChart["States/Uts"].tolist()
plt.pie(MilkChart['2007-08'].tolist(), labels=label,colors = colors, autopct='%.0f%%',shadow = 'True',
        startangle = 90,
        textprops = {'color': 'Black','fontsize':16},
        wedgeprops = {'linewidth': 3},
        rotatelabels = 'true')
plt.show()

"""### Task - 3"""

AllYearData=Milk_CsvFile.loc[(Milk_CsvFile['States/Uts'] ==list[0])|(Milk_CsvFile['States/Uts'] ==list[1])|(Milk_CsvFile['States/Uts'] ==list[2])|(Milk_CsvFile['States/Uts'] ==list[3])|(Milk_CsvFile['States/Uts'] ==list[4])]
label=AllYearData["States/Uts"].tolist()
AllYearData=AllYearData.T
colors = sns.color_palette('pastel')[0:5]
fig, axes = plt.subplots(2,3,figsize=(12,12))
axes[0,0].pie(AllYearData.iloc[1].tolist(),labels=label,colors = colors, autopct='%.0f%%',textprops={'fontsize': 8})
axes[0,0].set_title("2007-08")
axes[0,1].pie(AllYearData.iloc[2].tolist(),labels=label,colors = colors, autopct='%.0f%%',textprops={'fontsize': 8})
axes[0,1].set_title("2008-09")
axes[0,2].pie(AllYearData.iloc[3].tolist(),labels=label,colors = colors, autopct='%.0f%%',textprops={'fontsize': 8})
axes[0,2].set_title("2009-10")
axes[1,0].pie(AllYearData.iloc[4].tolist(),labels=label,colors = colors, autopct='%.0f%%',textprops={'fontsize': 8})
axes[1,0].set_title("2010-11")
axes[1,1].pie(AllYearData.iloc[5].tolist(),labels=label,colors = colors, autopct='%.0f%%',textprops={'fontsize': 8})
axes[1,1].set_title("2011-12")
axes[1][2].set_visible(False)
plt.show()

"""### Task - 4"""

IndexFile=Egg_CsvFile.set_index("States/Uts")
SubNumEgg=IndexFile.div(IndexFile.sum(axis=1),axis=0)
ax=SubNumEgg.plot(kind='bar', stacked=True)
plt.legend(loc=(1.02,0))