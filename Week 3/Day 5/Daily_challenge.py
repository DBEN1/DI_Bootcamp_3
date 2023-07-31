
import requests
import time

def get_load_time(url):
     start_time = time.time()
     response = requests.get(url)
     end_time = time.time()

     # Ensure the request was successful
     # The script checks if response.status_code == 200 to make sure the request was successful
     #  before it calculates the time difference. If the status code is not 200, 
     # it means there was some sort of error and the request didn't succeed, 
     # so the script returns None
     if response.status_code == 200:
         return end_time - start_time
     else:
         return None

 # Test with several sites
websites = ['https://www.google.com', 'https://www.ynet.co.il', 'https://www.danbenguira.com']
for site in websites:
     load_time = get_load_time(site)
     if load_time is not None:
         print(f'Load time for {site} is {load_time} seconds.')
     else:
         print(f'Failed to load {site}.')
