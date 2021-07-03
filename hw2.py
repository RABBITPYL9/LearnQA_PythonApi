import requests

class TestHeader():
    def test_check_header(self):
        
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        answer = dict(response.headers)
        print(response.headers)
        get_answer_value = answer["x-secret-homework-header"]
        check_value = 'Some secret value'
        
        assert get_answer_value == check_value
