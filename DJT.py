#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:39:21 2017

@author: wellingtonjohnson
"""

import pandas as pd
import seaborn as sn
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../Desktop/Data/expenditures.csv')

df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)

df = df[df['Amount']>0]

df_50k_plus = df[df['Amount']>=50000]

sn.stripplot(x='Amount',y='Purpose',data=df_50k_plus,jitter=True,linewidth=1)

sn.stripplot(x='Amount',y='Payee state',data=df,jitter=True,linewidth=1)