class LogicClient:
    def __init__(self):
        self.handlers = []

    def add_handler(self, func, type: str = None):
        def add(handler):
            """
            Регистрирует новый хэндлер
            """

        return add

    def process_json(self, json_msg):
        """
        Преобразует сообщение в объект Message
        Выбирает нужный хэндлер и передает туда этот объект
        """

    def send_message(self, message: Message, user_id: str, platform: str):
        """
        Отправляет сообщение
        """
