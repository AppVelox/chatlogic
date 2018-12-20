import pytest

from chatlogic.models.message import Button, Message, Keyboard
from chatlogic.models.incoming import IncomingMessage


class TestMessages:
    def test_Button(self):
        b = Button('test', 'test')
        with pytest.raises(TypeError):
            Button(1, '')
        with pytest.raises(TypeError):
            Button('', 1)
        assert b.to_dict() == {
            'text': 'test',
            'payload': 'test'
        }

    def test_Keyboard(self):
        b = Button('test', 'test')
        k = Keyboard([b])
        with pytest.raises(TypeError):
            Keyboard(1)
        assert k.to_dict() == [{
            'text': 'test',
            'payload': 'test'
        }]

    def test_message(self):
        b = Button('test', 'test')
        k = Keyboard([b])
        m = Message('test', k)
        with pytest.raises(TypeError):
            Message(1)
        with pytest.raises(TypeError):
            Message('', 1)
        assert m.to_dict() == {
            'text': 'test',
            'keyboard': [{
                'text': 'test',
                'payload': 'test'
            }]
        }


class TestIncoming:
    def test_IncomingMessage(self):
        IncomingMessage('', '', '', '', '')
        with pytest.raises(TypeError):
            IncomingMessage(1, '', '', '', '')
        with pytest.raises(TypeError):
            IncomingMessage('', 1, '', '', '')
        with pytest.raises(TypeError):
            IncomingMessage('', '', 1, '', '')
        with pytest.raises(TypeError):
            IncomingMessage('', '', '', 1, '')
        with pytest.raises(TypeError):
            IncomingMessage('', '', '', '', 1)
