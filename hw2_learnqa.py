import json
###example one with json
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
pars = json.loads(json_text)
print(pars["messages"][1]["message"])

###example2 not json(в ТЗ уже словарь, значение можно получить обратившись по ключу)

json_text2 = {"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}
print(json_text2["messages"][1]["message"])
