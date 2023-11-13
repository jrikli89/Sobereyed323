import requests
import json

# Modified to include variable for api_key instead of hard-coded value
def get_droplets(api_key):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)

    if response.status_code == 200:
        return json.loads(response.text)['droplets']
    print(f"Error: {response.status_code}")
    # Return empty list when error occurs to maintain type consistency
    return []