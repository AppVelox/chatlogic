class IncomingMessage:
    def __init__(self, type: str, text: str, platform: str, user_id: str, payload: str = None, *args, **kwargs):
        if not isinstance(type, str):
            raise TypeError('type must be an instance of str')
        if not isinstance(text, str):
            raise TypeError('text must be an instance of str')
        if not isinstance(platform, str):
            raise TypeError('platform must be an instance of str')
        if not isinstance(user_id, str):
            raise TypeError('user_id must be an instance of str')
        if payload is not None:
            if not isinstance(payload, str):
                raise TypeError('payload must be an instance of str')
        self.type = type
        self.text = text
        self.platform = platform
        self.user_id = user_id
        self.payload = payload
