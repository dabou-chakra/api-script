import requests

# Secret API key
API_KEY ="b7140816ec2875064ee5e6cb34486e80"

def fetch_data(endpoint):
    url = f"https://api.example.com/{endpoint}"
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    endpoint = 'data'
    try:
        data = fetch_data(endpoint)
        print(data)
    except Exception as e:
        print(e)
