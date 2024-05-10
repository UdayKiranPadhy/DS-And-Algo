import json

result = ""

instance_id = "showpad-en"
json_result = json.loads(result)
print("No. of user :- ", len(json_result['data']))
print("No of Super Admin :- ",
      len([user for user in json_result['data'] for instance in user['instances'] if
           instance['isSuperAdmin'] == True and instance['instanceId'] == instance_id]))
