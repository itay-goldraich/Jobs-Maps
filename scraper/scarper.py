import requests
import pandas as pd
import os
import temp

def fetch_linkedin_jobs(search_term, geoid, page):
    #api_key = os.environ.get('SCRAPINGDOG_API_KEY')
    api_key = temp.api_key #Need to change this to proper github secret
    base_url = 'https://api.scrapingdog.com/linkedinjobs'
    params = {
        'api_key': api_key,
        'field': search_term,
        'geoid': geoid,
        'page': page,        
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception if response status is not 2xx
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

import os
import pandas as pd

def main(search_term, geoid):
    page = 1
    
    data_directory = 'data'
    os.makedirs(data_directory, exist_ok=True)
    
    all_job_data = []  # To store all job data
    
    while True:
        print()
        job_data = fetch_linkedin_jobs(search_term, geoid, page)
        
        if job_data:
            all_job_data.extend(job_data)
            page += 1
        else:
            print("No more job data to fetch. Exiting loop.")
            break

    if all_job_data:
        df = pd.DataFrame(all_job_data)
        csv_path = os.path.join(data_directory, 'linkedinjobs_all_data.csv')
        df.to_csv(csv_path, index=False, encoding='utf-8')
    else:
        print("Failed to fetch any job data.")

# Call the function to fetch and save all job data into a single CSV file
main('Python developer','101620260') #This call should come from the UI.
print("done")

