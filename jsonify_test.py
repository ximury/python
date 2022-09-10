import json

from flask import jsonify

is_success = True
message = "Request Success"
data = {
    "timeline": ['2022.04.22', '2022.04.23', '2022.04.24', '2022.04.25', '2022.04.26', '2022.04.27', '2022.04.28'],
    "userOnline": [17.63, 14.74, 9.29, 10.39, 15.2, 0.37, 0.6],
    "hostOnline": [],
}
data = json.dumps(data)
print(data)
response_dict = {
    "success": is_success,
    "data": data,
    "msg": message,
}
print((response_dict))
