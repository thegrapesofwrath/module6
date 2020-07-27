#%%
from config import nytConnectionDictionary
import requests

#%%
baseUrl = nytConnectionDictionary["baseURL"]
apiKey = nytConnectionDictionary["apiKey"]
endPoint = "articlesearch.json"
queryString = ""
beginDate="" #optional
endDate = "" #optional


requestURL = f"{baseUrl}/{endPoint}?q={queryString}&api-key={apiKey}"

if beginDate != "":
    requestURL = requestURL + f"&begin_date={beginDate}"
if endDate != "":
    requestURL = requestURL + f"&end_date={endDate}"

#%%
class requestError(Exception):
    def __init__(self,expression, message):
        self.expression = expression
        self.message = message

#%%
responseJson = None
try:
    response = requests.get(requestURL)
    if response.status_code == 200:
        # print(response.json())
        responseJson = response.json()
    else:
        raise requestError("The response status code is:",response.status_code)
except requestError as theError:
    print(f"{theError.expression} : {theError.message}")


        

# %%
print(response.status_code)

# %%
print(responseJson)

# %%
responseJson["response"]["docs"][0]["abstract"]

# %%
