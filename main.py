import requests
from datetime import date
import arrow

USERNAME = "tasin"
TOKEN = "koniniaiiianinfijio"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph89"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
#
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Minute",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


pixel_data = {
    "date": date.today().strftime("%Y%m%d"),
    "quantity": input("How many minutes have you done coding today? ")
}

response = requests.post(url=post_pixel_endpoint,json= pixel_data,headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.today().strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "89"
}


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.today().strftime('%Y%m%d')}"

