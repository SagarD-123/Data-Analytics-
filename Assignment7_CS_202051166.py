# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l74-uX23FDlzebkSFw6qA32XlHVNxNUa

# **Lab Assignment 07**

**Sagar Deware(202051166)**
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
import seaborn as sns
from google.colab import drive
sns.set(rc={'figure.figsize':(12,8)})

filepath="weight-height.csv"
data=pd.read_csv(filepath)
data.head()

"""1. Perform Random Sampling by choosing 1000 samples from data. Compute the sample mean
and population mean (from whole data) and then compute the error between both mean.
"""

population_mean = round(data['Height'].mean(),3)
print(population_mean)

random_sample = data.sample(n=1000).sort_index()
print(random_sample)

sample_mean = round(random_sample['Height'].mean(),3)
print(sample_mean)

# creating dictionary for error calculation
abs_error = {'sample_mean':[sample_mean],
           'population_mean':population_mean}

# Transform into a data frame
abs_error = pd.DataFrame(abs_error, index=['Simple Random Sampling'])
abs_error['abs_error'] = abs(abs_error['population_mean'] - abs_error['sample_mean'])

# Sort data 
abs_error.sort_values(by='abs_error')
print(abs_error)

"""2. Perform Systematic Sampling by choosing 1000 samples from data. Compute the sample
mean and population mean (from whole data) and then compute the error between both mean.
"""

def systematic_sampling(df, step):
    
    indexes = np.arange(0,1000, step=step)
    sample = df.iloc[indexes]
    return sample
    
# systematic sample and mean
systematic_sample = systematic_sampling(data, 1)
systematic_mean = round(systematic_sample['Height'].mean(),3)

# View sampled data frame
print(systematic_sample)

abs_error = {'systematic_mean':[systematic_mean],
           'population_mean':population_mean}

# Transform into a data frame
abs_error = pd.DataFrame(abs_error, index=[' Systematic Sampling'])
abs_error['abs_error'] = abs(abs_error['population_mean'] - abs_error['systematic_mean'])

#sort
abs_error.sort_values(by='abs_error')
print(abs_error)

"""3. Perform Stratified Sampling by choosing 1000 samples from data. Compute the sample mean
and population mean (from whole data) and then compute the error between both mean.
"""

# split criteria
split = StratifiedShuffleSplit(n_splits=1, test_size=1000)
print(split)

# Perform data frame split
for x, y in split.split(data, data['Gender']):
    stratified_random_sample = data.iloc[y]

stratified_random_sample_mean = round(stratified_random_sample['Height'].mean(),3)
print(stratified_random_sample)

abs_error = {'stratified_mean':[stratified_random_sample_mean],
           'population_mean':population_mean}

# Transform into a data frame
abs_error = pd.DataFrame(abs_error, index=[' Stratified Sampling'])
abs_error['abs_error'] = abs(abs_error['population_mean'] - abs_error['stratified_mean'])

# Sort
abs_error.sort_values(by='abs_error')
print(abs_error)