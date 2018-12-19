class Button:
    def __init__(self, text, payload):
        pass

    def to_dict(self):
        """
        Преобразует объект в словарь
        """


class Keyboard:
    def __init__(self, buttons: list):
        pass

    def to_dict(self):
        """
        Преобразует объект в словарь
        """


class Message:
    def __init__(self, text: str, keyboard: Keyboard, *args, **kwargs):
        pass

    def to_dict(self):
        """
        Преобразует объект в словарь
        """