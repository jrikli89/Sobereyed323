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


def deploy_application() -> None:
    # Initialize digitalocean api key
    api_key = 'your_digitalocean_api_key'
  
    # Create a new droplet
    new_droplet_payload = {
      "name": "smodal-app-droplet",
      "region": "nyc3",
      "size": "s-1vcpu-1gb",
      "image": "docker-18-04",
      "ssh_keys": None,
      "backups": False,
      "ipv6": True,
      "user_data": None,
      "private_networking": None,
      "volumes": None,
      "tags": [
        "web"
      ]
    }
    
    headers = {
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {api_key}'
    }
    
    create_droplet_res = requests.post(
      'https://api.digitalocean.com/v2/droplets', 
      headers=headers, 
      data=json.dumps(new_droplet_payload)
    )
  
    if create_droplet_res.status_code != 202:
        print('Failed to create droplet.')
        return
  
    print('Successfully created droplet. Deploying application...')
  
    # Deploy application using necessary command
    # Replace 'your_deployment_command' with your actual deploy command
    os.system('your_deployment_command')

    print('Application deployed successfully.')
