class Button:
    def __init__(self, text: str, payload: str):
        if not isinstance(text, str):
            raise TypeError('text must be an instance of str')
        if not isinstance(payload, str):
            raise TypeError('payload must be an instance of str')
        self.text = text
        self.payload = payload

    def to_dict(self):
        return {
            'text': self.text,
            'payload': self.payload
        }


class Keyboard:
    def __init__(self, buttons: list):
        if not isinstance(buttons, list):
            raise TypeError('buttons must be an instance of list')
        self.buttons = buttons

    def to_dict(self):
        return [x.to_dict() for x in self.buttons]


class Message:
    def __init__(self, text: str, keyboard: Keyboard = None, *args, **kwargs):
        if not isinstance(text, str):
            raise TypeError('text must be an instance of str')
        if keyboard is not None:
            if not isinstance(keyboard, Keyboard):
                raise TypeError('keyboard must be an instance of Keyboard')
        self.text = text
        self.keyboard = keyboard

    def to_dict(self):
        res = {
            'text': self.text,
        }
        if self.keyboard:
            res['keyboard'] = self.keyboard.to_dict()
        return res