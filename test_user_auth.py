import requests
import pytest


class TestUserAuth:
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password':'1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header"
        assert "user_id" in response1.json(), "no user id in the response"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_from_auth_method = response1.json()["user_id"]

    def test_auth_user(self):
    
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token":self.token},
            cookies={"auth_sid":self.auth_sid}
        )

        assert "user_id" in response2.json(), "there no user id in second response"
        user_id_in_check_method = response2.json()["user_id"]
        assert self.user_id_from_auth_method == user_id_in_check_method, "user id !="

    
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative__auth_check(self, condition):

        if condition == "no_cookie":
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth",
            headers= {"x-csrf-token":self.token} 
            )

        else:
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth",
            cookies={"auth_sid":self.auth_sid} 
            )

        assert "user_id" in response2.json(), "no user id in second response"
        #assert "user_id" in self.response2.json(), "no user id in second response"
        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_check_method == 0, f"user {condition}"
