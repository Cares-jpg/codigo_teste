import requests

def get_ip():
    response = requests.get("https://api.ipify.org?format=json")
    print("Seu IP público é:", response.json()["ip"])

if __name__ == "__main__":
    get_ip()
