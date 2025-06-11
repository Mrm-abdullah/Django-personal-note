import requests
import json

# URL = "http://127.0.0.1:8000/rest/"

# response = requests.get(url=URL)
# data = response.json()
# print(data)

URL = "http://127.0.0.1:8000/restcreate/"

# create

# data = {
#     'teacher_name': 'Abdul khalek',
#     'course_name': 'english',
#     'course_durationss': 3,
#     'seat': 20
# }

# json_data = json.dumps(data)
# response = requests.post(url=URL, data = json_data)
# data = response.json()
# print(data)

# update

# data = {
#     'id': 6,
#     'teacher_name': 'tumiiiii',
#     'course_name': 'ami'
# }

# json_data = json.dumps(data)
# r = requests.put(url=URL, data = json_data)
# data = r.json()
# print(data)

# delete
data = {
    'id': 2,
}

json_data = json.dumps(data)
r = requests.delete(url=URL, data = json_data)
data = r.json()
print(data)