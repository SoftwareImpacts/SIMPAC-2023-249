######################################## CLASSIFICATION ########################################

import atlantic as atl
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore", category=Warning) #-> For a clean console

#source_data="https://www.kaggle.com/datasets/surekharamireddy/fraudulent-claim-on-cars-physical-damage"

url="https://raw.githubusercontent.com/TsLu1s/Atlantic/main/data/Fraudulent_Claim_Cars_class.csv"
data= pd.read_csv(url) # Dataframe Loading Example

target_col="fraud"
data[target_col]=data[target_col].astype('category')

data.dtypes
data.isna().sum()

train,test = train_test_split(data, train_size=0.8)

# Option 1 - Simple Option
fit_atl = atl.fit_processing(dataset=train,      # dataset:pd.DataFrame, target:str="Target_Column"
                             target=target_col,  # split_ratio:float=0.75 [0.5,0.95[ 
                             split_ratio=0.9)

# Option 2 - Customizable Option
fit_atl = atl.fit_processing(dataset=train,             # dataset:pd.DataFrame, 
                             target=target_col,         # target:str="Target_Column"
                             split_ratio=0.9,          # split_ratio:float=0.75, total_vi:float=0.98 [0.5,1]
                             total_vi=0.98,             # h2o_fs_models:int [1,50], encoding_fs:bool=True\False
                             h2o_fs_models=7,           # vif_ratio:float=10.0 [3,30]
                             encoding_fs=True,
                             vif_ratio=10.0)

# Transform Data Processing
train=atl.data_processing(dataset=train,
                          fit_atl=fit_atl)

test=atl.data_processing(dataset=test,
                         fit_atl=fit_atl)

# Export Atlantic Preprocessing Metadata
import pickle 
output = open("fit_atl.pkl", 'wb')
pickle.dump(fit_atl, output)

