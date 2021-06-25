import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

more_redir = response.history #узнаем кол-во редиректов
print(more_redir)

first_redir = response.history[0] #редирект первый
second_redir = response.history[1] #редирект второй
three_redir = response.history[2] #редирект третий

print(first_redir.url + ' Это первый' + ' редирект')
print(second_redir.url + ' Это второй' + ' редирект')
print(three_redir.url + ' Это третий' + ' редирект(итоговый)')
