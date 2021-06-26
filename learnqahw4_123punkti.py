import requests

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response1.text) #Wrong method provided пункт первый

response3 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type?method=HEAD")
print(response3.text) #пустой вывод пункт второй

response4 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type?method=PUT")
print(response4.text) #{"success":"!"} третий пункт
