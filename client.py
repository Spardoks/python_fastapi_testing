import requests

print("Hello World")

print("----")
print("POST")
response = requests.post(
    "http://127.0.0.1:8080/advertisement",
    json={
        "title": "test_title",
        "description": "test_description",
        "price": "100",
        "author": "test_author",
    },
)
print(response.status_code)
print(response.json())

print("----")
print("GET")
response = requests.get(
    "http://127.0.0.1:8080/advertisement/1",
)
print(response.status_code)
print(response.json())


print("----")
print("PATCH")
response = requests.patch(
    "http://127.0.0.1:8080/advertisement/1",
    json={
        "title": "test_title1",
        "description": "test_description1",
        "author": "test_author1",
    },
)
print(response.status_code)
print(response.json())


print("----")
print("GET")
response = requests.get(
    "http://127.0.0.1:8080/advertisement/1",
)
print(response.status_code)
print(response.json())


print("----")
print("GET query")
response = requests.get(
    "http://127.0.0.1:8080/advertisement?author=test_author1&title=test_title1",
)
print(response.status_code)
print(response.json())


print("----")
print("DELETE")
response = requests.delete(
    "http://127.0.0.1:8080/advertisement/1",
)
print(response.status_code)
print(response.json())