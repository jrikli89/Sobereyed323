import requests
import json

def get_droplets(api_key):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)

    if response.status_code == 200:
        return json.loads(response.text)['droplets']
    print(f"Error: {response.status_code}")
    return None