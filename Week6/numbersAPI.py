#%%
import requests
from config import connectionString

#%%
baseUrl = connectionString['url']
# completeURL = f'{baseUrl}/17/trivia' #Debug examples
completeURL = f'{baseUrl}17/trivia?json' #The docs say you need the json parameter to get a json response.

response = requests.get(completeURL).json()
#%%

print(response['text'])

# %%


