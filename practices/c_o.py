import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

# params = { 
#     'id' : 3,
#     'userId' : 5,
#     }

payload = {
    "title": "New Post",
    "body": "This is a new post created via the API.",
    "userId": 1
}

new = {
    "title": "New",
    "body": "Updated but empty post created via the API",
    "userId": 1
}

#response = requests.post(url, json=payload)

response = requests.put(url, json=new)

response = requests.delete(url)

data = response.json()

# print(f'Requests url : {response.url}')
# print(f'Status code : {response.status_code}')
# print(f'Response Body : {response.json()}')

print(response.status_code)
print(data)
