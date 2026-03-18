import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url, timeout=10)

print("Status code:", response.status_code)

if response.status_code != 200:
    print("Request error")
    raise SystemExit

data = response.json()

users = []
for user in data:
    users.append({
        "id": user["id"],
        "name": user["name"],
        "username": user["username"],
        "email": user["email"],
        "city": user["address"]["city"],
        "company": user["company"]["name"]
    })

df = pd.DataFrame(users)

print("\nUsers table:")
print(df)

print("\nUsers count:", len(df))
print("Unique cities:", df["city"].nunique())

print("\nUsers by city:")
print(df["city"].value_counts())

df.to_csv("users.csv", index=False, encoding="utf-8-sig")
print("\nSaved: users.csv")
