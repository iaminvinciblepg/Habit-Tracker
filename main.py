import requests
from datetime import datetime

pixela_endpoint="https://pixe.la/v1/users"
username="spwider2011"
token="OPMKNYJK"
graph_id="graph1"

user_params={
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
graph_params={
    "id":graph_id,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"momiji",
}
day= datetime(year=2025,month=8,day=27)
pixel_params={
    "date":day.strftime("%Y%m%d"),
    "quantity":input("How many kilometers are there"),
}
update_params={
    "quantity":"7"
}
headers={"X-USER-TOKEN":token}

'''To cerate a user'''
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

'''To create a graph'''
# graph_endpoint=f"{pixela_endpoint}/{username}/graphs"
# response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)

'''To create a pixel'''
graphpixel_endpoint=f"{pixela_endpoint}/{username}/graphs/{graph_id}"
response=requests.post(url=graphpixel_endpoint,json=pixel_params,headers=headers)
print(response.text)

'''To update a pixel'''
# updatepixel_endpoint=f"{pixela_endpoint}/{username}/graphs/{graph_id}/{day.strftime("%Y%m%d")}"
# response=requests.put(url=updatepixel_endpoint,json=update_params,headers=headers)
# print(response.text)

'''To delete a pixel'''
# deletepixel_endpoint=f"{pixela_endpoint}/{username}/graphs/{graph_id}/{day.strftime("%Y%m%d")}"
# response=requests.delete(url=deletepixel_endpoint,headers=headers)
# print(response.text)


