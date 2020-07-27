#%%
import requests
import json
from config import spaceXConnectionString
#%%
baseURL = spaceXConnectionString['url']
endPoint = 'launchpads'
optionalSiteID = 'vafb_slc_4e'

requestURL = f'{baseURL}/{endPoint}'

if optionalSiteID != '':
    requestURL = requestURL + f'/{optionalSiteID}'

#%%
spaceXResponse = requests.get(requestURL).json()
#%%
# print(spaceXResponse[0])

# for i in range(0,len(spaceXResponse)):
#     print(spaceXResponse[i]['name'])


# %%
print(json.dumps(spaceXResponse))

##Single

