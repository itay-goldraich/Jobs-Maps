import requests
import user_input as ui
import pandas as pd

target_url= ui.target_url
resp = requests.get(target_url).json()

print(resp)

df = pd.DataFrame(resp)
df.to_csv('linkedinjobs.csv', index=False, encoding='utf-8')
