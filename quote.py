import requests

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()[0]
            return f'"{data["q"]}" — {data["a"]}'
        else:
            return "Couldn't fetch quote at the moment."
    except Exception as e:
        return f"Error: {e}"
