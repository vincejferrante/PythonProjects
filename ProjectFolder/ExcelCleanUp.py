# import required libraries
import numpy as np
import pandas as pd
  
# Calling the Dataframe and pasting file location into code
Mydataframe = pd.read_excel (r' ')

# Removing all the spaces in the column headers
Mydataframe.columns = Mydataframe.columns.str.replace(' ','_')

# Replace all empty places with null and then remove all null values column with dropna function.
Mydataframe['Opposite_Account_'] = np.nan
display(Mydataframe)

# Applying the method   
nan_value = float("NaN")
Mydataframe.replace(0, nan_value, inplace=True)
Mydataframe.replace("", nan_value, inplace=True)

#droping the na  
Mydataframe.dropna(how='all', axis=1, inplace=True)
  
# show the dataframe
display(Mydataframe)
