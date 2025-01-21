# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

veriler = pd.read_csv("eksikveriler.csv")
print(veriler)

imputer = SimpleImputer(missing_values=np.nan,strategy="mean")

Yas  = veriler.iloc[:,1:4].values


imputer=imputer.fit(Yas[:,1:4])
Yas[:,1:4]=imputer.transform(Yas[:,1:4])
print(Yas)

