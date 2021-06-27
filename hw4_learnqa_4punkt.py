import requests
import json

good_answer = {"success":"!"}

###В данном примере использую try, exception(зная верный ответ от сервера), хотя правильней обойтись проверкой статус кода и проверкой структуры ответа

examples_method = ["GET", "POST", "HEAD", "PUT", "DELETE"]

"""
Алгоритм программы такой:
из доступых методов запроса, которые указаны в списке examples_method, по скольку положительный ответ приходит с типом строки(формат как у словаря),
то программа попробует его перевести в словарь используя json, если получается, и сравнивает его со словарем корректного ответа,то значит запрос корректный,
если же приходит другой ответ, то здесь понятно что запрос не корректный, в этом случае срабатывает исключение
"""

for i in examples_method:
    if i == "GET":
        response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={"method":"GET"})
        saved_answer = response.text
        try:
            decoded = json.loads(saved_answer)
            if decoded == good_answer:
                print("запрос GET корректный")
        except json.decoder.JSONDecodeError:
            print("запрос GET не корректный")
    elif i == "POST":
        response1 = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method":"POST"})
        saved_answer1 = response1.text
        try:
            decoded1 = json.loads(saved_answer1)
            if decoded1 == good_answer:
                print("запрос POST корректный")
        except json.decoder.JSONDecodeError:
            print("запрос POST не корректный")
    elif i == "HEAD":
        response2 = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method":"HEAD"})
        saved_answer2 = response2.text
        try:
            decoded2 = json.loads(saved_answer2)
            if decoded2 == good_answer:
                print("запрос head корректный")
        except json.decoder.JSONDecodeError:
            print("запрос head не корректный")

    elif i == "PUT":
        response3 = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method":"PUT"})
        saved_answer3 = response3.text
        try:
            decoded3 = json.loads(saved_answer3)
            if decoded3 == good_answer:
                print("запрос PUT корректный")
        except json.decoder.JSONDecodeError:
            print("запрос PUT не корректный")


    elif i == "DELETE":
        response4 = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method":"DELETE"})
        saved_answer4 = response4.text
        try:
            decoded4 = json.loads(saved_answer4)
            if decoded4 == good_answer:
                print("запрос DELETE корректный")
        except json.decoder.JSONDecodeError:
            print("запрос DELETE не корректный")
