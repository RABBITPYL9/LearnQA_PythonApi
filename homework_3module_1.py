class TestExample():

    def test_check_len(self):

        enter_text = input("Введите фразу короче 15 символов: ")

        assert len(enter_text) < 15
