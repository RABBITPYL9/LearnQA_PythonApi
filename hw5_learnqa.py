import requests
import json
import time

element = "token"
element_seconds = "seconds"
element1 = "status"

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job") #запрос на получение токена
saved_answer1 = response1.text #сохраняем ответ(в данный момент тип строки)
parsed_string_to_dict = json.loads(saved_answer1) #переводим в словарь
if element and element_seconds in parsed_string_to_dict: #делаем проверку на наличие ответа с токеном p.s конструкцию можно заменить assert
    print("Токен найден, сохраняем")
    get_token = parsed_string_to_dict["token"] #получаем токен в переменную из словаря
    get_seconds = parsed_string_to_dict["seconds"] #получаем время в секундах
    print("Время до готовности задачи найдено")
    print(get_seconds)
else:
    print("ОШИБКА!Токен не найден")

response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job?token=" + get_token) #запрос с токеном и проверка статуса
saved_answer2 = response2.text # сохраняем ответ
parsed_string_to_dict1 = json.loads(saved_answer2) #переводим в словарь
if element1 in parsed_string_to_dict1: #делаем проверку на наличие ответа со статусом
    get_status_job = parsed_string_to_dict1["status"] #получаем статус задачи
    print("Получили ответ о готовности задачи" + ' состояние' + ' задачи: ' + get_status_job)
else:
    print("ОШИБКА!")


time.sleep(get_seconds)

resultatik = {"result":"42","status":"Job is ready"} #будем сравнивать этот словарь с полученным ответом
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job?token=" + get_token) # запрос после ожидания готовности задачи
saved_answer3 = response3.text #сохраняем ответ
parsed_string_to_dict3 = json.loads(saved_answer3)
assert parsed_string_to_dict3 == resultatik
print("Проверели успешо что задача готова")
