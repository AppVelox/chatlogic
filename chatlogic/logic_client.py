from .models.incoming import IncomingMessage
from .models.message import Message


class LogicClient:
    def __init__(self):
        self.handlers = []

    def add_handler(self, func=None, type: str = None):
        if not isinstance(type, str):
            raise TypeError('type must be an instance of str')

        def add(handler):
            self.handlers.append({'handler': handler, 'func': func, 'type': type})
            return handler

        return add

    def process_json(self, json_msg: dict):
        if not isinstance(json_msg, dict):
            raise TypeError('json_msg must be an instance of dict')
        incoming = IncomingMessage(**json_msg)
        for handler in self.handlers:
            if handler['type']:
                if handler['type'] != incoming.type:
                    continue
            if handler['func']:
                if not handler['func'](incoming):
                    continue
            handler['handler'](incoming)
            return

    def send_message(self, message: Message, user_id: str, platform: str):
        data = {
            **{
                'user_id': user_id,
                'platform': platform,
            },
            **message.to_dict()
        }
