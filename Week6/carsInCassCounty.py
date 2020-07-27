#%%
# from Stats import Report
# from StatsModule.Stats import Report

from StatsModule.Report.Stats import Report
import matplotlib.pyplot as plt
import numpy as np
import math

#%%
carsInCassCounty = [1432,9634,15959,7853,3828] #Index corresponds to household size per vehicles available.
carsPerHousehold = [x for x in range(0,len(carsInCassCounty))]

plt.plot(carsPerHousehold,carsInCassCounty)
carsReport = Report(carsPerHousehold,carsInCassCounty)
print(carsReport)

# %%

