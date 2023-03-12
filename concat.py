import os
import glob
import pandas as pd
    
os.chdir('./EVLAcsv')
    
extension = 'csv'
all_EV = glob.glob('E*.{}'.format(extension))
all_LA = glob.glob('L*.{}'.format(extension))

#df_EV15 = pd.read_csv("EV - 2015.csv")
#print(df_EV15)

# Combine all files in the list and export to .csv
    
df_concat_EV = pd.concat([pd.read_csv(f) for f in all_EV ], ignore_index=True)
print(df_concat_EV)

df_concat_LA = pd.concat([pd.read_csv(f) for f in all_LA ], ignore_index=True)
print(df_concat_LA)