import requests

class TestCookie():
    def test_check_cookie(self):

        response = requests.post("https://playground.learnqa.ru/api/homework_cookie")
        pars_cookie = dict(response.cookies)
        print(pars_cookie)
        check_actual_cookie = {'HomeWork': 'hw_value'}

        assert pars_cookie == check_actual_cookie
