
# Import required packages
import pandas as pd
import numpy as np
import math

# Read csv file and store it to data frame
data_df = pd.read_csv("https://d3n0h9tb65y8q.cloudfront.net/public_assets/assets/000/002/000/original/input_data.csv?1638532904")


# replace null/nan values with zero
data_df['dataPoints'] = data_df['dataPoints'].fillna(0) 

# replace negative infinite values with -1
data_df.replace(-np.inf, -1, inplace=True)

# replace positive infinite values with 1
data_df.replace(np.inf, 1, inplace=True)

# replace all values above 50 with their respective sqrt values
data_df[data_df['dataPoints']>=50] = round(data_df[data_df['dataPoints']>=50].apply(np.sqrt), 2)

# load the final output to a csv file
data_df.to_csv('output.csv')

