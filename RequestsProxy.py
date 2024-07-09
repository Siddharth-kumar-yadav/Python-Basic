import requests

proxies = {# write here own proxy
  "http": "http://10.",
  "https": "https://10",
}

r= requests.get("https://api.ipify.org?format=json")
print(r.json())
