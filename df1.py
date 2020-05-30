import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("datafile_1.csv") #reading the data from file 'datafile_1.csv'

# first plot (cropwise)
fig,axs = plt.subplots(figsize=(10,6))
crop_wise_yield = data.groupby(['Crop']).sum()['Yield (Quintal/ Hectare) ']
plt.plot(crop_wise_yield, label = 'Yield (Quintal/ Hectare)')
crop_wise_production = data.groupby(['Crop']).sum()['Cost of Production (`/Quintal) C2']/10
plt.plot(crop_wise_production, label = 'Cost of Production (`/Quintal) C2')
plt.xticks(rotation ='vertical')
plt.legend()
plt.show()


# second plot (statewise)
state_crop_yield = data.groupby(['State'])
index = list(state_crop_yield.indices.keys())
state_crop_yield.sum()[['Cost of Production (`/Quintal) C2', 'Yield (Quintal/ Hectare) ']].plot(kind='bar',figsize=(12,7))

plt.show()