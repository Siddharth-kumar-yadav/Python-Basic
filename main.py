import requests

def fetchAndSaveToFile(url, path):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
        
        with open(path, "w", encoding="utf-8") as f:  # Specify UTF-8 encoding
            f.write(r.text)
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        
    except IOError as e:
        print(f"Error writing to file: {e}")

# Example usage
url = "https://timesofindia.indiatimes.com/city/patna"
fetchAndSaveToFile(url, "data/times.html")


