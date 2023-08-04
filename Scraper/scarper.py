import requests
import pandas as pd
import os
import temp

def fetch_linkedin_jobs(search_term, geoid, page):
    api_key = os.environ.get('SCRAPINGDOG_API_KEY')
    api_key = temp.api_key #Need to fix this secrets problem
    base_url = 'https://api.scrapingdog.com/linkedinjobs'
    params = {
        'api_key': api_key,
        'field': search_term,
        'geoid': geoid,
        'page': page,        
        'fields': 'company_name,description,job_title,location,post_date,link',
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception if response status is not 2xx
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def temp_until_web_call():
    search_term = 'Python (Programming Language)'
    geoid = '101620260' #Tel Aviv
    page = 1
    
    job_data = fetch_linkedin_jobs(search_term, geoid, page)
    
    if job_data:
        df = pd.DataFrame(job_data)
        data_directory = 'data'
        os.makedirs(data_directory, exist_ok=True)

        csv_path = os.path.join(data_directory, 'linkedinjobs.csv')
        df.to_csv(csv_path, index=False, encoding='utf-8')
    else:
        print("Failed to fetch job data.")

temp_until_web_call()
print("done")

