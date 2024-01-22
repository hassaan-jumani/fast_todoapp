import requests

r = requests.post(f"http://127.0.0.1:8000/create" , json={'name':'as','description':'as'})
print(r.json())
