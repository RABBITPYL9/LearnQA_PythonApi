import json.decoder

from requests import Response

class BaseCase:
    def get_answer(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"response is not JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response not have '{name}'"

        return response_as_dict[name]
