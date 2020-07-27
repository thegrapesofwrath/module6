# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#Dependencies
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %%
#list of tv show titles to query
tv_shows = ["Altered Carbon", "Grey's Anatomy", "This is Us", "The Flash", "Vikings", "Shameless", "Arrow", "Peaky Blinders", "Dirk Gently"]

# make iterative requests to TVmaze search endpoint

baseUrl = "http://api.tvmaze.com/singlesearch/shows?q="


# %%


ratingsDictionary = {} # "title" : "rating"
#%%
class customError(Exception):
    def __init__(self,expression,message):
        self.expression = expression
        self.message = message
        

#%%
for show in tv_shows:
    try:
        requestURL = baseUrl + show
        response = requests.get(requestURL)
        responseJson = response.json()
        if response.status_code == 200:
            print(responseJson)
            title = show
            rating = responseJson["rating"]["average"]
            ratingsDictionary[title] = [rating]
            badAssignment = nonExistentVariable
        else:
            raise customError("The status code is:",response.status_code)
    except customError as aVariableName:
        print(f'{aVariableName.expression} {aVariableName.message}')
    except NameError as e:
        print(e)
    except Exception as e:
        print(f"Final case of errors if not handled previously : {e}")



#%%
# create dataframe
tvRatingsDF = pd.DataFrame({
    "title" : list(ratingsDictionary.keys()),
    "rating" : list(ratingsDictionary.values())
})

# %%
# use matplotlib to create a bar chart from the dataframe

plt.bar([x for x in range(0,len(tvRatingsDF))],tvRatingsDF["rating"])


# %%
tvRatingsDF.plot()

# %%
