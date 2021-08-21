# pylint: disable=missing-module-docstring

__all__ = ['Chats']

from .conversation import Conversation
from .send_read_acknowledge import SendReadAcknowledge


class Chats(Conversation, SendReadAcknowledge):
    """ methods.chats """
