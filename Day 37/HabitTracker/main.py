import requests
import datetime as dt
import os

USERNAME = "yannick"
GRAPH_iD = "graph1"
TOKEN = os.environ.get("PIXELA_API_KEY")

# 1. Run this once to create the user account:
# user_config = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url="https://pixe.la/v1/users", json=user_config)

# 2. Create a graph definition:
# headers = {"X-USER-TOKEN": TOKEN}
# graph_config = {
#     "id": GRAPH_iD,
#     "name": "Stretching Graph",
#     "unit": "Min",
#     "type": "int",
#     "color": "shibafu",
# }
# response = requests.post(url=F"https://pixe.la/v1/users/{USERNAME}/graphs", json=graph_config, headers=headers)

# 3. Add a Pixel to a certain date:
# headers = {"X-USER-TOKEN": TOKEN}
# pixel_config = {
#     "date": dt.date.today().strftime("%Y%m%d"),
#     "quantity": "2",
# }
# response = requests.post(url=F"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_iD}",
#                          json=pixel_config,
#                          headers=headers)

# 4. Update the pixel value for a certain data:
# headers = {"X-USER-TOKEN": TOKEN}
# pixel_config = {"quantity": "10"}
# response = requests.put(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_iD}"
#                             f"/{dt.date.today().strftime('%Y%m%d')}", json=pixel_config, headers=headers)

# 5. Delete the pixels for a given day:
headers = {"X-USER-TOKEN": TOKEN}
response = requests.delete(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_iD}"
                               f"/{dt.date.today().strftime('%Y%m%d')}", headers=headers)
print(response.text)
