
import httpx

base_url = "https://dummyjson.com/"

content = "recipes/meal-type/snack"

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

for recipe in content["recipes"]:
    print(recipe["difficulty"])
