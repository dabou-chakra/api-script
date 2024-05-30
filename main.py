import requests

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
