# -*- coding: utf-8 -*-
"""

<p>Lab 2</p>
<p>Data Analysis and Visualization</p>
<p>202051166</p>
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# %matplotlib inline

Jkcsv = pd.read_csv('JK-Allopathic-Outpatient_attendance-May-2019.csv')

Jkcsv.head(7)

Jkcsv.info()

"""### Question 1:
Compute total patient attendance for all district for all four range group and plot the bar
diagram. Set the bar plot parameters for better visualization.
"""

patient = Jkcsv[['District','No. of facilities by performance - 1 to 100','No. of facilities by performance - 101 to 500','No. of facilities by performance - 501 to 1000','No. of facilities by performance - >1000']].copy()

patient_attendance = patient.groupby(['District'],as_index=False).sum()

"""### Question 1
Compute total patient attendance for all district for all four range group and plot the bar
diagram. Set the bar plot parameters for better visualization.
"""

districts = patient_attendance['District']

y1 = patient_attendance['No. of facilities by performance - 1 to 100']
y2 = patient_attendance['No. of facilities by performance - 101 to 500']
y3 = patient_attendance['No. of facilities by performance - 501 to 1000']
y4 = patient_attendance['No. of facilities by performance - >1000']


x_axis = np.arange(len(districts))

plt.bar(x_axis-0.3,y1,0.2,label="1 - 100")
plt.bar(x_axis-0.1,y2,0.2,label="101 - 500")
plt.bar(x_axis+0.1,y3,0.2,label="501 - 1000")
plt.bar(x_axis+0.3,y4,0.2,label="above 1000")

plt.xticks(x_axis,districts)
plt.xlabel("Districts")
plt.ylabel("patients")
plt.title("Patient attendance")
plt.legend()

"""### Question 2
Compute total patient attendance for all district for each Facility Type (DH, CHC and SC) for all four range groups and plot the staked bar diagram of three. Set the bar plot parameters for better visualization.
"""

Jkcsv.head()

PA = Jkcsv[['District','Facility Type','No. of facilities by performance - 1 to 100','No. of facilities by performance - 101 to 500','No. of facilities by performance - 501 to 1000','No. of facilities by performance - >1000']].copy()
PA.head()

total_facility_attendace = PA.groupby(['Facility Type'],as_index=False).sum()
total_facility_attendace

PA

facilities = Jkcsv['Facility Type'].unique()
fig=total_facility_attendace.plot(kind='bar',stacked=True)
fig.legend(loc='upper left')
plt.xlabel("Facility Type")
plt.ylabel("patients")
plt.xticks([0,1,2],facilities)

"""### Question 4
Plot group bar plot for Performance - Overall Average of different Facility Type (DH, CHC and
SC) of Anantnag, Jammu, Poonch, Reasi and Udhampur.
"""

index = Jkcsv['District'].isin(["Anantnag",'Jammu','Poonch','Reasi','Udhampur'])
PA_districts = Jkcsv[index]

PA_districts.head()

info = PA_districts[['District','Facility Type','Performance - Overall Average **']].copy()
info.head()

performance_plot = sns.barplot(data=data,hue='Facility Type',x='Performance - Overall Average **',y='District')

"""### Question 4
Present dot plot for Performance - Maximum of any 20 different district. Performance - Maxi
mum for different Facility Type should be combined appropriately using a aggregation function
for each district.
"""

# first finding all unique districts
districts = Jkcsv['District'].unique()
districts

selected_districts = Jkcsv[Jkcsv['District'].isin(['Anantnag', 'Badgam', 'Bandipora', 'Baramula', 'Doda', 'Ganderbal',
       'Jammu', 'Kargil', 'Kathua', 'Kishtwar', 'Kulgam', 'Kupwara',
       'Leh Ladakh', 'Poonch', 'Pulwama', 'Rajouri', 'Ramban', 'Reasi',
       'Samba', 'Shopian'])]
selected_districts.head()

selected_districts = selected_districts.groupby('District').sum()
selected_districts.head()

dot_plot = sns.scatterplot(x=selected_districts['Performance - Maximum'],y=selected_districts.index)

"""<h3>Fifa player profile</h3>"""

# loading fifa dataset
fifa_PA = pd.read_csv('Fifa_player_football_data.csv')
fifa_.head(10)

"""### Question 1
Present Age of various football players as histogram and kernel density plots. Set appropriate
parameters of the plot.
"""

#histplot
present_age = fifa_PA['Age']
age_plot = sns.histplot(present_age,bins=[10,15,20,25,30,35,40,45,50])

#kde plot for 
age_plot_kde = sns.kdeplot(present_age)

"""### Question 2
Present Age of various Football players as Kernel Density plots for each of FC Barcelona,
Chelsea, Juventus and Real Madrid Clubs. Set appropriate parameters of the plot.
"""

# Kernel Density Plot for gievn clubs
present_age = fifa_PA['Club'].isin(['FC Barcelona','Chelsea','Juventus','Real Madrid'])
present = fifa_PA[present_age]

present_age_group = present[['Age','Club']].copy()
present_age_group

kde_club_plot = sns.kdeplot(x=present_age_group['Age'],hue=present_age_group['Club'])

fifa_PA['Preferred Foot']

"""### Question 3
Plot Value of players as Stacked Histogram Preferred Foot wise (right and left).
"""

foot_df = fifa_PA[['Preferred Foot']].value_counts()
foot_df

#plotting stacked plot for foot of players
# we are plotting directly using the above count of Preferred foot
plt.bar(["Foot"],13949)
plt.bar(["Foot"],4211)
plt.legend(['Right','Left'])

"""### Question 4
Check distribution of International Reputation using Q-Q plot.
"""

from statsmodels.graphics.gofplots import qqplot

qqplot(fifa_PA["International Reputation"],line='s')
plt.show()