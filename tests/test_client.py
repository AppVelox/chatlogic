import pytest

from chatlogic import LogicClient
from chatlogic.models.incoming import IncomingMessage
from chatlogic.models.message import Message


class TestClient:
    def test_init(self):
        with pytest.raises(TypeError):
            LogicClient(1)
        LogicClient('url')

    def test_process(self):
        c = LogicClient()
        with pytest.raises(TypeError):
            @c.add_handler(func=lambda x: True, type=1)
            def f(msg):
                pass

        @c.add_handler(func=lambda x: True, type='test')
        def f(msg):
            assert isinstance(msg, IncomingMessage)
            c.send_message(Message(''), '', '')
            with pytest.raises(TypeError):
                c.send_message(1, '', '')
            with pytest.raises(TypeError):
                c.send_message(Message(''), 1, '')
            with pytest.raises(TypeError):
                c.send_message(Message(''), '', 1)
        m_json = {
            'type': 'test',
            'text': 'test',
            'platform': 'test',
            'user_id': 'test',
            'payload': 'test',
        }
        c.process_json(m_json)
